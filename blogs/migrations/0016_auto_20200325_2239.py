# Generated by Django 3.0.3 on 2020-03-25 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_remove_plane_clé_airline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plane',
            old_name='code_IATA',
            new_name='code_iata',
        ),
        migrations.RenameField(
            model_name='plane',
            old_name='code_OACI',
            new_name='code_oaci',
        ),
    ]
