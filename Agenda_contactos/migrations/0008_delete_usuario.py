# Generated by Django 3.2.8 on 2021-11-12 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda_contactos', '0007_alter_contacto_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
