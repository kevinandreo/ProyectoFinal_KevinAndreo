# Generated by Django 4.2.1 on 2023-05-29 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0004_remove_perfil_descripcion_remove_perfil_link_pagina'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='website',
            field=models.URLField(default=''),
        ),
    ]
