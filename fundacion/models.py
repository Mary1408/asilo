from django.db import models
# Clase Paciente

GENERO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)


class Puesto(models.Model):

    nombrePuesto = models.CharField('Puesto', max_length=50)
    especialidad = models.CharField('Especialidad', max_length=50)

    def __str__(self):
        try:
            return '%s %s' %(self.nombrePuesto, self.especialidad)
        except:
            return self.nombrePuesto

    class Meta:
        db_table = 'puesto'
        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'


class Empleado(models.Model):

    nombreCompleto = models.CharField('Nombre completo del Empleado',
        max_length=50,null=False)
    genero = models.CharField('Genero',
        max_length = 1, choices=GENERO_CHOICES, default = 'M', null= False)
    puesto = models.ForeignKey(Puesto,
        on_delete=models.CASCADE,null=False)


    def __str__(self):
        try:
            return '%s %s' %(self.nombreCompleto, self.puesto)
        except:
            return self.nombreCompleto


    class Meta:
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'





class Medicamento(models.Model):

    nombre = models.CharField('Nombre del medicamento',
        max_length=50,null=False)
    presentacion = models.CharField('Presentacion',
        max_length=50,null=False)
    precio = models.DecimalField('Precio de Venta',
        max_digits=7, decimal_places=2, null=False)
    descuento = models.DecimalField('Descuento',
        max_digits=7, decimal_places=2, null=False)

    def __str__(self):
        try:
            return '%s %s' %(self.nombre)
        except:
            return self.nombre


    class Meta:
        db_table = 'medicamento'
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'


class DetalleMedicamento(models.Model):
    medicamento=models.ForeignKey(Medicamento, on_delete=models.CASCADE,
        null=False)
    lote=models.CharField('Codigo del lote del producto',
        null=False, blank=False, max_length=50)
    ubicacion=models.CharField('Ubicacion del lote',
        null=False, blank=False, max_length=50)
    fechavencimiento=models.DateField('Fecha de vencimiento',
        null=True, blank=True)

    class Meta:
        db_table = 'detalle_medicamento'
        verbose_name = 'Detalle del medicamento'
        verbose_name_plural = 'Detalle de los medicamentos'


class Farmacia(models.Model):
    encargado=models.ForeignKey(Empleado, on_delete=models.CASCADE,
        null=False)
    medicamento=models.ForeignKey(Medicamento, on_delete=models.CASCADE,
        null=False)


    class Meta:
        db_table = 'farmacia'
        verbose_name = 'Farmacia'
        verbose_name_plural = 'Farmacias'



class Laboratorio(models.Model):
    encargado=models.ForeignKey(Empleado, on_delete=models.CASCADE,
        null=False)
    tipoExamen=models.CharField('Tipo de Examen',
        null=False, blank=False, max_length=100)


    class Meta:
        db_table = 'laboratorio'
        verbose_name = 'Laboratorio'
        verbose_name_plural = 'Laboratorios'

