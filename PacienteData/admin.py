from django.contrib import admin

# Register your models here.

from .models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

#admin.site.register(Paciente)

class PacienrteResource(resources.ModelResource):
	class Meta:
		model = Paciente


class PacienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):

	search_fields = ['num_document','nombre','apePaterno','apeMaterno','sexo','celular','fechaPrimeraDosis','fechaSegundaDosis']
	list_display = ('num_document','nombre','apePaterno','apeMaterno','sexo','celular','fechaPrimeraDosis','fechaSegundaDosis')
#	ordering = ['dni']

	resource_class = PacienrteResource


admin.site.register(Paciente, PacienteAdmin)
