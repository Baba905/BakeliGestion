# Generated by Django 4.0.5 on 2022-06-09 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0003_remove_eleve_etablissement'),
        ('etablissement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='etablissement',
            name='eleves',
            field=models.ManyToManyField(to='eleve.eleve'),
        ),
    ]
