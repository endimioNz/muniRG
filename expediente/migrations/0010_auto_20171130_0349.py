# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-30 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0009_auto_20171129_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capacitacion1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30, unique=True, verbose_name='Capacitacion: ')),
            ],
        ),
        migrations.CreateModel(
            name='Capacitacion2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30, unique=True, verbose_name='Capacitacion: ')),
            ],
        ),
        migrations.CreateModel(
            name='Capacitacion3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30, unique=True, verbose_name='Capacitacion: ')),
            ],
        ),
        migrations.CreateModel(
            name='Capacitacion4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30, unique=True, verbose_name='Capacitacion: ')),
            ],
        ),
        migrations.CreateModel(
            name='Capacitacion5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30, unique=True, verbose_name='Capacitacion: ')),
            ],
        ),
        migrations.CreateModel(
            name='Capacitacion6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30, unique=True, verbose_name='Capacitacion: ')),
            ],
        ),
        migrations.CreateModel(
            name='Capacitacion7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30, unique=True, verbose_name='Capacitacion: ')),
            ],
        ),
        migrations.RemoveField(
            model_name='emprendedor',
            name='capacitacion',
        ),
        migrations.RemoveField(
            model_name='expediente',
            name='updated',
        ),
        migrations.AlterField(
            model_name='expediente',
            name='asiento',
            field=models.CharField(choices=[('ASESORAMIENTO', 'ASESORAMIENTO'), ('SEGUIMIENTO: CREDITO', 'SEGUIMIENTO: CREDITO'), ('SEGUIMIENTO: SUBSIDIO', 'SEGUIMIENTO: SUBSIDIO'), ('FINANCIAMIENTO: PROPIO', 'FINANCIAMIENTO: PROPIO'), ('FINANCIAMIENTO: TERCERO', 'FINANCIAMIENTO: TERCERO'), ('FERIA: DESAFIO PRODUCIR', 'FERIA: DESAFIO PRODUCIR'), ('FERIA: PASEO ARTESANO', 'FERIA: PASEO ARTESANO'), ('FERIA: OTROS', 'FERIA: OTROS'), ('CAPACITACION', 'CAPACITACION'), ('NO APROBADO', 'NO APROBADO')], max_length=25, verbose_name='Asiento'),
        ),
        migrations.DeleteModel(
            name='Capacitacion',
        ),
        migrations.AddField(
            model_name='emprendedor',
            name='capacitacion1',
            field=models.ManyToManyField(to='expediente.Capacitacion1'),
        ),
        migrations.AddField(
            model_name='emprendedor',
            name='capacitacion2',
            field=models.ManyToManyField(to='expediente.Capacitacion2'),
        ),
        migrations.AddField(
            model_name='emprendedor',
            name='capacitacion3',
            field=models.ManyToManyField(to='expediente.Capacitacion3'),
        ),
        migrations.AddField(
            model_name='emprendedor',
            name='capacitacion4',
            field=models.ManyToManyField(to='expediente.Capacitacion4'),
        ),
        migrations.AddField(
            model_name='emprendedor',
            name='capacitacion5',
            field=models.ManyToManyField(to='expediente.Capacitacion5'),
        ),
        migrations.AddField(
            model_name='emprendedor',
            name='capacitacion6',
            field=models.ManyToManyField(to='expediente.Capacitacion6'),
        ),
        migrations.AddField(
            model_name='emprendedor',
            name='capacitacion7',
            field=models.ManyToManyField(to='expediente.Capacitacion7'),
        ),
    ]