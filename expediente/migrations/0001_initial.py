# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-15 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emprendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('identificacion', models.CharField(choices=[('DNI', 'DNI (Documento Nacional de Identidad)'), ('CI', 'CI (Cedula de identidad)'), ('LC', 'LC (Libreta de enrolamiento)')], default='DNI', max_length=3, verbose_name='Tipo de Identificacion')),
                ('numero', models.CharField(max_length=8, unique=True)),
                ('direccion', models.CharField(max_length=30, verbose_name='Direccion')),
                ('telefono', models.CharField(max_length=20, verbose_name='Telefono')),
                ('estadocivil', models.CharField(choices=[('SOLTERO/A', 'SOLTERO/A'), ('COMPROMETIDO/A', 'COMPROMETIDO/A'), ('CASADO/A', 'CASADO/A'), ('DIVORCIADO/A', 'DIVORCIADO/A'), ('VIUDO/A', 'VIUDO/A'), ('CONCUBINATO', 'CONCUBINATO')], max_length=14, verbose_name='Estado Civil')),
                ('profesion', models.CharField(max_length=30, verbose_name='Profesion')),
                ('cuil', models.CharField(max_length=13, verbose_name='CUIL o CUIT')),
                ('fecha', models.DateField(verbose_name='Fecha de carga: ')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('usuario', models.CharField(max_length=30, verbose_name='Responsable')),
                ('modeladodenegocios', models.BooleanField(default=False)),
                ('ventas', models.BooleanField(default=False)),
                ('marketing', models.BooleanField(default=False)),
                ('disenodemarca', models.BooleanField(default=False)),
                ('marcacolectiva', models.BooleanField(default=False)),
                ('rentabilidad', models.BooleanField(default=False)),
                ('costos', models.BooleanField(default=False)),
                ('entrenamientointensivo', models.BooleanField(default=False)),
                ('culturaemprendedora', models.BooleanField(default=False)),
                ('desarrollodeproducto', models.BooleanField(default=False)),
                ('plandenegocios', models.BooleanField(default=False)),
                ('innovacionycreatividad', models.BooleanField(default=False)),
                ('liderazgo', models.BooleanField(default=False)),
                ('trabajoenequipo', models.BooleanField(default=False)),
                ('comunicacionefectiva', models.BooleanField(default=False)),
                ('concursosyconvocatorias', models.BooleanField(default=False)),
                ('tradicionalynotradicional', models.BooleanField(default=False)),
                ('marketingdigital', models.BooleanField(default=False)),
                ('redessociales', models.BooleanField(default=False)),
                ('tiendaonline', models.BooleanField(default=False)),
                ('cooperativismo', models.BooleanField(default=False)),
                ('asociativismo', models.BooleanField(default=False)),
                ('personajuridica', models.BooleanField(default=False)),
                ('mujeremprendedora', models.BooleanField(default=False)),
                ('trabajoydiscapacidad', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asiento', models.CharField(choices=[('ASESORAMIENTO', 'ASESORAMIENTO'), ('OTORGAMIENTO: CREDITO', 'OTORGAMIENTO: CREDITO'), ('OTORGAMIENTO: SUBSIDIO', 'OTORGAMIENTO: SUBSIDIO'), ('SEGUIMIENTO: CREDITO', 'SEGUIMIENTO: CREDITO'), ('SEGUIMIENTO: SUBSIDIO', 'SEGUIMIENTO: SUBSIDIO'), ('FINANCIAMIENTO: PROPIO', 'FINANCIAMIENTO: PROPIO'), ('FINANCIAMIENTO: TERCERO', 'FINANCIAMIENTO: TERCERO'), ('FERIA: DESAFIO PRODUCIR', 'FERIA: DESAFIO PRODUCIR'), ('FERIA: PASEO ARTESANO', 'FERIA: PASEO ARTESANO'), ('FERIA: OTROS', 'FERIA: OTROS'), ('CAPACITACION', 'CAPACITACION'), ('NO APROBADO', 'NO APROBADO'), ('CREDITO: CANCELADO', 'CREDITO: CANCELADO'), ('SUBSIDIO: CANCELADO', 'SUBSIDIO: CANCELADO'), ('OBSERVACIONES', 'OBSERVACIONES')], max_length=25, verbose_name='Asiento')),
                ('monto', models.IntegerField(default=0)),
                ('rubro', models.CharField(choices=[('ARTESANO', 'ARTESANO'), ('DISEÑO', 'DISEÑO'), ('GASTRONOMICO', 'GASTRONOMICO'), ('HORTICOLA', 'HORTICOLA'), ('SERVICIOS', 'SERVICIOS'), ('SUSTENTABILIDAD', 'SUSTENTABILIDAD'), ('TAXI/REMIS', 'TAXI/REMIS'), ('TECNOLOGIA APROPIADA', 'TECNOLOGIA APROPIADA'), ('TECNOLOGICO', 'TECNOLOGICO')], max_length=20, verbose_name='Rubro')),
                ('texto', models.TextField(verbose_name='Informacion del expediente: ')),
                ('fecha', models.DateField(verbose_name='Fecha de carga: ')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.CharField(max_length=30, verbose_name='Responsable')),
                ('activo', models.BooleanField(default=True)),
                ('emprendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Emprendedor')),
            ],
        ),
    ]
