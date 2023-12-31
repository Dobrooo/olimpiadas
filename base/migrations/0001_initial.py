# Generated by Django 4.2.5 on 2023-09-27 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='alarma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaentrada', models.DateTimeField(default=django.utils.timezone.now)),
                ('horasalida', models.DateTimeField(blank=True, null=True)),
                ('activa', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('ocupada', models.BooleanField()),
                ('paciente', models.CharField(blank=True, max_length=50, null=True)),
                ('habitacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('motivoingreso', models.TextField(max_length=400)),
                ('horaentrada', models.DateTimeField()),
                ('horasalida', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camas', models.IntegerField()),
                ('piso', models.IntegerField()),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
        ),
    ]
