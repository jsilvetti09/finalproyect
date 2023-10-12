# Generated by Django 4.2.5 on 2023-10-06 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Computadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('computadora', models.CharField(choices=[('pcs', 'Pcs'), ('notebook', 'Notebook'), ('netbook', 'Netbook'), ('otro', 'Otro')], default='pcs', max_length=15)),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('anio', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fechaPublicacion', models.DateTimeField(auto_now_add=True)),
                ('telefonoContacto', models.IntegerField()),
                ('emailContacto', models.EmailField(max_length=254)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['usuario', '-fechaPublicacion'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='FinalApp.computadora')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
    ]
