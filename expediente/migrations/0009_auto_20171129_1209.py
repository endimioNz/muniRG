# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-29 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0008_expediente_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='fecha',
            field=models.DateField(verbose_name='Fecha de carga: '),
        ),
    ]