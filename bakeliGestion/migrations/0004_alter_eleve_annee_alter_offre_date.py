# Generated by Django 4.0.5 on 2022-06-11 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakeliGestion', '0003_postuler_remove_offre_eleve_eleve_offre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='annee',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='offre',
            name='date',
            field=models.DateTimeField(),
        ),
    ]