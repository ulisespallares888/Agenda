# Generated by Django 3.2.8 on 2021-11-22 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notitas', '0003_remove_notitas_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notitas',
            name='fecha',
        ),
    ]
