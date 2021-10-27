from django.db import models

# Create your models here.
class Escuela(models.Model):
	nombreEs: models.CharField(max_length=50)
	codEscuela: models.CharField(max_length=5, primary_key=True)

class Director(models.Model):
	idDirector: models.CharField(max_length=5, primary_key=True)
	nombreD: models.CharField(max_length=60, blank=False)
	apellidoD: models.CharField(max_length=60, blank=False)
	duiDi: models.CharField(max_length=9, null=False, blank=False)
	fech_nac: models.DateField()

class Docente(models.Model):
	codigoDoc: models.CharField(max_length=10, primary_key=True)
	duiDo: models.CharField(max_length=9, null=False, blank=False)
	nombreDo: models.CharField(max_length=50, blank=False)
	apellidoDo: models.CharField(max_length=50, blank=False)
	fech_nac_do: models.DateField()
	estado: models.BooleanField()
	email: models.EmailField()
	contrasenha: models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.nombreDo

class Asignatura(models.Model):
	codigoAsig: models.CharField(max_length=10, primary_key=True)
	nombreAsig: models.CharField(max_length=20)
	uv: models.IntegerField(max_length=2)
	tipo: models.CharField(max_length=20)
	prerrequisito: models.CharField(max_length=20)

	def __str__(self):
		return self.nombreAsig

class Carrera(models.Model):
	codigo: models.CharField(max_length=5, primary_key=True)
	nombreCarrera: models.CharField(max_length=20, blank=False)

class Pensum(models.Model):
	id_pensum: models.CharField(max_length=10)
	nombrePensum: models.CharField(max_length=10)
	anho: models.IntegerField(max_length=4)

class Edificio(models.Model):
	id_Edificio: models.CharField(max_length=5, primary_key=True)
	nom_Edi: models.CharField(max_length=20, blank=False)
	ubicacion: models.CharField(max_length=50)
	cant_locales: models.IntegerField()

class Local(models.Model):
	id_Local: models.CharField(max_length=5, primary_key=True)
	nombre_local: models.CharField(max_length= 5, blank=False)

class REserva(models.Model):
	id_res: models.CharField(max_length=5, primary_key=True)
	estado: models.BooleanField()
	fecha: models.DateField()
	hora: models.TimeField()


