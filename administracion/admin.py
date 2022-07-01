from django.contrib import admin
from .models import *

class PacienteAdmin(admin.ModelAdmin):

    search_fields = ['dpi', 'nombreCompleto']
    list_filter = ['genero']
    list_display = ['dpi', 'nombreCompleto', 'telefonoFamiliar']

class MedicoAdmin(admin.ModelAdmin):

    search_fields = ['nombreCompleto']
    list_filter = ['genero']
    list_display = ['nombreCompleto', 'genero']


class TipoEntradaAdmin(admin.ModelAdmin):

    search_fields = ['nombreTipo']
    list_filter = ['nombreTipo']
    list_display = ['nombreTipo']


class EntradasAdmin(admin.ModelAdmin):

    search_fields = ['tipoEntrada', 'enteAcreditador']
    list_filter = ['tipoEntrada']
    list_display = ['tipoEntrada', 'enteAcreditador']

class TipoSalidaAdmin(admin.ModelAdmin):

    search_fields = ['nombreTipo']
    list_filter = ['nombreTipo']
    list_display = ['nombreTipo']


class SalidasAdmin(admin.ModelAdmin):

    search_fields = ['tipoSalida', 'enteDebitador']
    list_filter = ['tipoSalida']
    list_display = ['tipoSalida', 'enteDebitador']


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Entradas, EntradasAdmin)
admin.site.register(TipoEntrada, TipoEntradaAdmin)
admin.site.register(Salidas, SalidasAdmin)
admin.site.register(TipoSalida, TipoSalidaAdmin)