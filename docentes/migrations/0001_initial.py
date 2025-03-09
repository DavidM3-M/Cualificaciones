# Generated by Django 5.1.7 on 2025-03-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_de_cedula', models.CharField(max_length=20)),
                ('primer_nombre', models.CharField(max_length=50)),
                ('segundo_nombre', models.CharField(max_length=50)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(max_length=20)),
                ('pais_de_residencia', models.CharField(max_length=20)),
                ('departamento_de_residencia', models.CharField(max_length=20)),
                ('ciudad_de_residencia', models.CharField(max_length=50)),
                ('barrio_de_residencia', models.CharField(max_length=20)),
                ('direccion_de_residencia', models.CharField(max_length=100)),
            ],
        ),
    ]
