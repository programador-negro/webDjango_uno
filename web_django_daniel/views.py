from django.http import HttpResponse
import datetime

#forma 2 de mostrar un template facil.
from django.template import Template, Context, loader
# forma 3 de mostrar un template mas facil.
from django.shortcuts import render
#-----------------------------------------------------

def mensaje(request):
    return HttpResponse("<h1>Esto es un mensaje desde Django</h1>")
#-----------------------------------------------------

def la_fecha(request):
    fecha_y_hora = datetime.datetime.now()
    doc = """
    <h1 style = 'color: blue;'>
        La fecha y hora actual son: %s
            </h1>""" % fecha_y_hora
    return HttpResponse(doc)
#-----------------------------------------------------
# Pasar parametros por la URL
def calcularEdad(request, edad, year):
    if year > 2020:
        edadr = edad
        fyear = year - 2020
        edadfin = edadr + fyear

        return HttpResponse("Tu edad sera de: %s"%edadfin)
    else:
        return HttpResponse("El año debe ser mayor a 2020")
#-----------------------------------------------------

# Vista con template o plantilla
def view_index(request):
    nombre = "Jack Daniel"
    date = datetime.datetime.now()
    ciudades = ["cartagena","medellin","bogota","barranquilla","cali"]
    paises = []

    # directorio del archivo
    index_template = open("C:/Users/user/Documents/Programacion/Python/proyectosSerios/web_django_daniel/templates/index.html")

    # lectura del archivo
    doc_Template = Template(index_template.read())

    # cierre del archivo
    index_template.close()

    # contexto que contiene los elementos dinamicos para enviar a el template
    # contexto tambien pue estar vacio si no hay datos que enviar al template
    contxt = Context({"nombre":nombre,"dia":date,"ciudades":ciudades,"paises":paises})

    # renderizado del archivo
    doc = doc_Template.render(contxt)
    return HttpResponse(doc)
#-----------------------------------------------------

# Cargador o LOADER para mostrar template facilmente.
# PRIMERO:
#se configura en el archivo settings.py > TEMPLATES > DIRS [ruta-de-la-carpeta-templates]
# from django.templates import loader
def view_index_loader(request):

    nombre = "Jack Daniel"
    date = datetime.datetime.now()
    ciudades = ["cartagena","medellin","bogota","barranquilla","cali"]
    paises = []
    # Se usa el loader o cargador con el nombre del archivo html
    doc_templ = loader.get_template('index.html')
    # ya no es necesario usar un contexto sino solamente un diccionario
    # si se usa un contexto podria causar ERROR
    contxt = {"nombre":nombre,"dia":date,"ciudades":ciudades,"paises":paises}
    # renderizado del archivo
    doc = doc_templ.render(contxt)
    return HttpResponse(doc)
#-----------------------------------------------------

# SHORCUT para mostrar un template mas facil
# from django.shortcuts import render
def view_index_shortcut(request):

    nombre = "Jack Daniel"
    date = datetime.datetime.now()
    ciudades = ["cartagena","medellin","bogota","barranquilla","cali"]
    paises = []
    return render(request,'index.html',{"nombre":nombre,"dia":date,"ciudades":ciudades,"paises":paises})
#-----------------------------------------------------

# Herencia de plantillas
def vista_herencias(request):
    return render(request, "plantillahija.html")
