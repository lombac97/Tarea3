# Generated by Django 3.0.3 on 2020-02-05 21:27

import django.core.validators
from django.db import migrations, models
import login.validators


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguridad',
            name='clave',
            field=models.CharField(max_length=20, validators=[login.validators.validar_clave]),
        ),
        migrations.AlterField(
            model_name='seguridad',
            name='correo',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(regex='^\\w+([\\.-]?\\w+)@\\w+([\\.-]?\\w+)(\\.\\w{2,3})+$')]),
        ),
    ]
