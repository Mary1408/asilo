from django.contrib import admin
from .models import *



class PuestoAdmin(admin.ModelAdmin):

	search_fields = ['nombrePuesto', 'especialidad']
	list_filter = ['nombrePuesto', 'especialidad' ]
	list_display = ['nombrePuesto', 'especialidad' ]


class EmpleadoAdmin(admin.ModelAdmin):

	search_fields = ['nombreCompleto', 'puesto']
	list_filter = ['puesto']
	list_display = ['nombreCompleto', 'genero', 'puesto' ]



class DetMedicamentoInline(admin.TabularInline):
	model = DetalleMedicamento
	extra = 1

class MedicamentoAdmin(admin.ModelAdmin):
	inlines = [DetMedicamentoInline]
	search_fields = ['nombre', 'precio','presentacion']
	list_filter = ['nombre','presentacion']
	list_display = ['nombre', 'presentacion', 'precio', 'descuento']


class FarmaciaAdmin(admin.ModelAdmin):

	list_display = ['encargado']


class LaboratorioAdmin(admin.ModelAdmin):

	list_display = ['encargado']



admin.site.register(Puesto, PuestoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Farmacia, FarmaciaAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
