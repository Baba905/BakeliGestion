# Generated by Django 4.0.5 on 2022-06-09 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0002_eleve_etablissement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='etablissement',
        ),
    ]
