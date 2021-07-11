from django.db import models

from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey


class Paciente(models.Model):
	tipo_document = (
		('1','DNI'),
		('2','Carnet de Extrangeria'),
		)
	tipo_doc = models.CharField(max_length=1, choices=tipo_document)
	num_document = models.CharField(max_length=9)
	nombre = models.CharField(max_length=100, blank=True, null=True)
	apePaterno = models.CharField(max_length=100, blank=True, null=True)
	apeMaterno = models.CharField(max_length=100, blank=True, null=True)
	sexos = (
		('0','FEMENINO'),
		('1','MASCULINO'),
		)
	sexo = models.CharField(max_length=1, choices=sexos, blank=True)
	celular = models.CharField(max_length=9, blank=True, null=True, null=True)
	userDiresa  =  UserForeignKey(auto_user = True, related_name = "Paciente")
	fechaPrimeraDosis = models.DateField(blank=True, null=True)
	fechaSegundaDosis = models.DateField(blank=True, null=True)



	def __str__(self):
		return self.nombre
