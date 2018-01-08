# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-06 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0014_auto_20171203_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='monto',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='asiento',
            field=models.CharField(choices=[('ASESORAMIENTO', 'ASESORAMIENTO'), ('OTORGAMIENTO: CREDITO', 'OTORGAMIENTO: CREDITO'), ('OTORGAMIENTO: SUBSIDIO', 'OTORGAMIENTO: SUBSIDIO'), ('SEGUIMIENTO: CREDITO', 'SEGUIMIENTO: CREDITO'), ('SEGUIMIENTO: SUBSIDIO', 'SEGUIMIENTO: SUBSIDIO'), ('FINANCIAMIENTO: PROPIO', 'FINANCIAMIENTO: PROPIO'), ('FINANCIAMIENTO: TERCERO', 'FINANCIAMIENTO: TERCERO'), ('FERIA: DESAFIO PRODUCIR', 'FERIA: DESAFIO PRODUCIR'), ('FERIA: PASEO ARTESANO', 'FERIA: PASEO ARTESANO'), ('FERIA: OTROS', 'FERIA: OTROS'), ('CAPACITACION', 'CAPACITACION'), ('NO APROBADO', 'NO APROBADO'), ('CREDITO: CANCELADO', 'CREDITO: CANCELADO'), ('SUBSIDIO: CANCELADO', 'SUBSIDIO: CANCELADO'), ('OBSERVACIONES', 'OBSERVACIONES')], max_length=25, verbose_name='Asiento'),
        ),
    ]