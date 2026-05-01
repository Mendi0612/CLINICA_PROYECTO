from django.shortcuts import render
from django.http import HttpResponse


def gestion_cita(request):
    return HttpResponse("""
    

    <html>
        <link rel="stylesheet" href="{% static 'gestion_cita/style.css'%}">
    <head>
        <title>Sistema Historia Clínica</title>
<style>

        body{
            font-family: Arial, Helvetica, sans-serif;
            margin:0;
            background:#f4f4f4;
        }

        /* MENU */
        .menu{
            background:#eaeaea;
            padding:15px 40px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }

        .menu a{
            text-decoration:none;
            margin-left:25px;
            color:#333;
            font-weight:bold;
        }

        /* SECCION PRINCIPAL */
        .principal{
            display:flex;
            align-items:center;
            justify-content:space-between;
            padding:80px;
            background:white;
        }

        .texto{
            width:50%;
        }

        .texto h1{
            font-size:45px;
            margin-bottom:20px;
        }

        .texto p{
            color:#555;
            line-height:1.6;
        }

        .botones-citas{
            display:flex;
            flex-direction:column;
            gap:15px;
            margin-top:15px;
        }

        .btn-cita{
            padding:15px;
            font-size:16px;
            border:none;
            border-radius:8px;
            background-color:#3498db;
            color:white;
            cursor:pointer;
            transition:0.3s;
        }

        .btn-cita:hover{
            background-color:#2980b9;
        }

        .cancelar{
            background-color:#e74c3c;
        }

        .cancelar:hover{
            background-color:#c0392b;
        }
      

        .contenedor{
            background:white;
            width:700px;
            margin:40px auto;
            padding:30px;
            border-radius:10px;
            box-shadow:0px 0px 10px rgba(0,0,0,0.1);
        }

        h2{
            color:#333;
        }

        ul{
            line-height:1.8;
        }

        </style>
        

    </head>


    <body>

       
        <div class="menu">

            <div>
                <b>Clinica_Proyecto</b>
            </div>

            <div>
                <a href="#">Inicio</a>
                <a href="#">Pacientes</a>
                <a href="#">Historia Clinica</a>
                <a href="#">farmacia</a>
                <a href="#">facturacion</a>
            </div>

        </div>


               
        <div class="contenedor">

            <h2>Gestion de Citas</h2>

            <p>
            Bienvenido al modulo de gestion de citas.
            </p>

            <p>
            Desde este modulo se pueden administrar todas las citas de los pacientes.
            </p>

            <p>
            Seleccione alguna de las opciones para su requerimiento:
            </p>

            <div class="botones-citas">

                <a href="/asignacion/" class="btn-cita" style="text-align:center; text-decoration:none;">Asignacion de citas medicas</a>

                <button class="btn-cita">Consulta de citas programadas</button>

                <button class="btn-cita">Modificacion de citas medicas</button>

    <button class="btn-cita cancelar">Cancelacion de citas medicas</button>

</div>

        </div>


    </body>

    </html>


    """)

def modulo(request):
    data = {
        "usuario": "Sebastian",
        "edad": 27,
        "citas": [
            {
                "medico": "Diego Rodriguez",
                "hora": "10:00 AM",
                "estado": "Disponible"
            },
            {
                "medico": "Laura Gomez",
                "hora": "10:20 AM",
                "estado": "Disponible"
            },
            {
                "medico": "Camilo Sanchez",
                "hora": "11:00 AM",
                "estado": "No disponible"
            },
            
        ]
    }
    return render(request, "Modulo.html", data)