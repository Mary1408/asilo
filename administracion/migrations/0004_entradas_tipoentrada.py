# Generated by Django 3.1 on 2022-06-28 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_auto_20220627_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEntrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipo', models.CharField(max_length=50, verbose_name='Tipo de Entrada')),
            ],
            options={
                'verbose_name': 'Tipo de entrada',
                'verbose_name_plural': 'Tipos de entradas',
                'db_table': 'tipo_entrada',
            },
        ),
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteAcreditador', models.CharField(max_length=50, verbose_name='Ente Acreditador')),
                ('descripcionEntrada', models.CharField(max_length=200, verbose_name='Motivo del ingreso monetario')),
                ('tipoEntrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.tipoentrada')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
                'db_table': 'entradas',
            },
        ),
    ]
