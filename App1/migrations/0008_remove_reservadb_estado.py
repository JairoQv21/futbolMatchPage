# Generated by Django 5.0.6 on 2024-05-21 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0007_alter_reservadb_estado_alter_usuariodb_dni_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservadb',
            name='estado',
        ),
    ]
