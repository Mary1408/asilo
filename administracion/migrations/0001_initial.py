# Generated by Django 3.1 on 2022-06-28 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dpi', models.PositiveIntegerField(max_length=13, null=True, verbose_name='DPI del Paciente')),
                ('nombreCompleto', models.CharField(max_length=50, verbose_name='Nombre completo del Paciente')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1, verbose_name='Genero')),
                ('fechaNacimiento', models.DateField(verbose_name='fecha nacimiento')),
                ('telefonoFamiliar', models.PositiveIntegerField(max_length=8, verbose_name='Telefono del familiar')),
                ('correoFamiliar', models.CharField(max_length=50, null=True, verbose_name='Direccion de correo del Familiar')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'db_table': 'paciente',
            },
        ),
    ]
