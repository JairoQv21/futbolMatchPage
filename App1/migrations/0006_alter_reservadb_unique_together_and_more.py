# Generated by Django 5.0.6 on 2024-05-20 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0005_alter_usuariodb_apellido_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservadb',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='reservadb',
            name='estado',
            field=models.CharField(default='disponible', max_length=13),
        ),
    ]
