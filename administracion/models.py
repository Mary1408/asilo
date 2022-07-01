from django.db import models


# Clase Paciente

GENERO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

class Paciente(models.Model):

    dpi = models.CharField('DPI del Paciente', max_length= 13, null=True)
    nombreCompleto = models.CharField('Nombre completo del Paciente',
        max_length=50,null=False)
    genero = models.CharField('Genero',
        max_length = 1, choices=GENERO_CHOICES, default = 'M', null= False)
    fechaNacimiento = models.DateField('fecha nacimiento')
    telefonoFamiliar = models.PositiveIntegerField('Telefono del familiar', null=False)
    correoFamiliar = models.CharField('Direccion de correo del Familiar',
        max_length=50,null=True)

    def __str__(self):
        try:
            return '%s' %(self.nombreCompleto)
        except:
            return self.nombreCompleto


    class Meta:
        db_table = 'paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


# Clase medico

class Medico(models.Model):

    nombreCompleto = models.CharField('Nombre completo del Medico',
        max_length=50,null=False)
    genero = models.CharField('Genero',
        max_length = 1, choices=GENERO_CHOICES, default = 'M', null= False)


    def __str__(self):
        try:
            return '%s' %(self.nombreCompleto)
        except:
            return self.nombreCompleto


    class Meta:
        db_table = 'medico'
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'



#Clase Entradas

# Clase tipo de entrada del asilo (Donaciones o Cobro a familiares).
# No se usa CHOISE por si llegan a existir mas tipos de entradas

class TipoEntrada(models.Model):

    nombreTipo = models.CharField('Tipo de Entrada', max_length=50)

    def __str__(self):
        return self.nombreTipo

    class Meta:
        db_table = 'tipo_entrada'
        verbose_name = 'Tipo de entrada'
        verbose_name_plural = 'Tipos de entradas'

# Clase entrada

class Entradas(models.Model):

    tipoEntrada = models.ForeignKey(TipoEntrada,
        on_delete=models.CASCADE,null=False)
    enteAcreditador = models.CharField('Ente Acreditador',
        max_length=50,null=False)
    descripcionEntrada = models.CharField('Motivo del ingreso monetario',
        max_length=200,null=False)
    

    def __str__(self):
        try:
            return '%s %s' %(self.tipoEntrada, self.enteAcreditador)
        except:
            return self.enteAcreditador


    class Meta:
        db_table = 'entradas'
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

#Clase Entradas

# Clase tipo de salida del asilo (Gastos o Pago a Fundacion).
# No se usa CHOISE por si llegan a existir mas tipos de salidas

class TipoSalida(models.Model):

    nombreTipo = models.CharField('Tipo de Salida', max_length=50)

    def __str__(self):
        return self.nombreTipo

    class Meta:
        db_table = 'tipo_salida'
        verbose_name = 'Tipo de salida'
        verbose_name_plural = 'Tipos de salidas'

# Clase salidas

class Salidas(models.Model):

    tipoSalida = models.ForeignKey(TipoSalida,
        on_delete=models.CASCADE,null=False)
    enteDebitador = models.CharField('Ente Debitador',
        max_length=50,null=False)
    descripcionSalida = models.CharField('Motivo de la salida monetaria',
        max_length=200,null=False)
    

    def __str__(self):
        try:
            return '%s %s' %(self.tipoSalida, self.enteDebitador)
        except:
            return self.enteDebitador


    class Meta:
        db_table = 'salidas'
        verbose_name = 'Salida'
        verbose_name_plural = 'Salidas'
