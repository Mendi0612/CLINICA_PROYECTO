from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import Usuario


def usuario(request):

    mensaje = ""

    if request.method == 'POST':

        correo = request.POST['usuario']
        password = request.POST['password']

        try:

            # Buscar usuario por correo
            user = Usuario.objects.get(correo=correo)

            # Verificar contraseña
            if check_password(password, user.password):

                return redirect('/MenuPrincipal/')

            else:
                mensaje = "Contraseña incorrecta"

        except Usuario.DoesNotExist:

            mensaje = "El usuario no existe"

    return render(request, "Login.html", {
        'mensaje': mensaje
    })

def Registro(request):

    if request.method == 'POST':

        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        documento = request.POST['Documento']
        correo = request.POST['correo']
        edad = request.POST['edad']
        password = request.POST['password']
        confirmar = request.POST['confirmar']

        
        if password == confirmar:

            Usuario.objects.create(
                nombre=nombre,
                apellido=apellido,
                documento=documento,
                correo=correo,
                edad=edad,
                password=make_password(password)
            )

            return redirect('/Login/')

    return render(request, "Registro.html")

def MenuPrincipal(request):
    return render(request, "MenuInicio.html")

def inicio(request):
    return render(request, 'inicio.html')
