# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-28 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0002_auto_20171128_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='capacitacion',
            field=models.CharField(choices=[('Crear y Emprender', 'Crear y Emprender'), ('Gestionado de Empresa', 'Gestionado de Empresa'), ('Habilidades blandas', 'Habilidades blandas'), ('Alternativas de Financimiento', 'Alternativas de Financimiento'), ("Tic's en Gestion Empresarial", "Tic's en Gestion Empresarial"), ('Asociatividad Empresarial', 'Asociatividad Empresarial'), ('Inclusion Productiva', 'Inclusion Productiva')], max_length=30, verbose_name='Lista de Capacitacion: '),
        ),
    ]