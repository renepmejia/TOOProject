from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import reciever

# Create your models here.
class Escuela(models.Model):
	cod_escuela= models.CharField(max_length=5, primary_key=True)
	nombre_escuela= models.CharField(max_length=50)

class Director(models.Model):
	id_director= models.CharField(max_length=5, primary_key=True)
	nombre_d= models.CharField(max_length=60, blank=False)
	apellido_d= models.CharField(max_length=60, blank=False)
	dui_di= models.CharField(max_length=9, null=False, blank=False)
	fech_nac= models.DateField()

class Docente(models.Model):
	codigo_doc= models.CharField(max_length=10, primary_key=True)
	dui_do= models.CharField(max_length=9, null=False, blank=False)
	nombre_do= models.CharField(max_length=50, blank=False)
	apellido_do= models.CharField(max_length=50, blank=False)
	fech_nac_do= models.DateField()
	estado= models.BooleanField()
	email= models.EmailField()
	contrasenha= models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.nombreDo

class Asignatura(models.Model):
	codigo_asig= models.CharField(max_length=10, primary_key=True)
	nombre_asig= models.CharField(max_length=20)
	uv= models.IntegerField()
	tipo= models.CharField(max_length=20)
	prerrequisito= models.CharField(max_length=20)

	def __str__(self):
		return self.nombreAsig

class Carrera(models.Model):
	codigo= models.CharField(max_length=5, primary_key=True)
	nombre_carrera= models.CharField(max_length=20, blank=False)

class Pensum(models.Model):
	id_pensum= models.CharField(max_length=10)
	nombre_pensum= models.CharField(max_length=10)
	anho= models.IntegerField()

class Edificio(models.Model):
	id_edificio= models.CharField(max_length=5, primary_key=True)
	nom_edi= models.CharField(max_length=20, blank=False)
	ubicacion= models.CharField(max_length=50)
	cant_locales= models.IntegerField()

class Local(models.Model):
	id_local= models.CharField(max_length=5, primary_key=True)
	nombre_local= models.CharField(max_length= 5, blank=False)

class REserva(models.Model):
	id_res= models.CharField(max_length=5, primary_key=True)
	estado= models.BooleanField()
	fecha= models.DateField()
	hora= models.TimeField()

"""class Perfil(models.Model):
	usuario= models.OneToOneField(User, on_delete= models.CASCADE)
	email= models.EmailField(max_length=50)

	def __str__(self):
		return self.usuario.username

def crear_usuario_perfil(sender, instance, created, **kwargs):
	if created:
		Perfil.objects.created(usuario=instance)

def guardar_usuario_perfil(sender, instance, **kwargs):
	instance.Perfil.save()
"""
