# Generated by Django 5.0.6 on 2024-05-20 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CanchaDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoReservaDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PromocionDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReservaDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('cancha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.canchadb')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.estadoreservadb')),
                ('promociones', models.ManyToManyField(to='App1.promociondb')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.usuariodb')),
            ],
        ),
        migrations.CreateModel(
            name='ReservaPromocionDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promocion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.promociondb')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.reservadb')),
            ],
        ),
    ]