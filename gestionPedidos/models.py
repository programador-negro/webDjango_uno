from django.db import models

# Create your models here.
class Clientes(models.Model):
	nombre = models.CharField(max_length=30)
	direccion=models.CharField(max_length=50)
	email=models.EmailField()
	telefono=models.CharField(max_length=10)
class Articulos(models.Model):
	nombre = models.CharField(max_length=30)
	seccion = models.CharField(max_length=30)
	precio=models.IntegerField()
class Pedidos(models.Model):
	numero = models.IntegerField()
	fecha=models.DateField()
	entregado=models.BooleanField()

'''
NOTA IMPORTANTE:
despues de crear las tablas deben ejecutarse los siguientes comandos para crear las tablas.

# para establecer la app en django
python manage.py makemigrations

# para checkear si todo se creo correctamente
python manage.py check 'nombre-la-app'

# para establecer las tablas en django
python manage.py sqlmigrate 'nombre-la-app' 'codigo-de-migracion'

# para actualizar todo el proyecto
python manage.py migrate
'''