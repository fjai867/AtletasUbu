# Generated by Django 3.0.6 on 2020-07-03 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_atletas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atleta',
            name='Id_Atleta',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='Id_Cat',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='Id_Ins',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='Id_Prueba',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
