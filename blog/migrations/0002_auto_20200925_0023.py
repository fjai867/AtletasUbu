# Generated by Django 3.0.6 on 2020-09-24 22:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
