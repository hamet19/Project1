# Generated by Django 3.0.3 on 2020-03-20 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200320_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plane',
            name='code_IATA',
        ),
        migrations.RemoveField(
            model_name='plane',
            name='code_OACI',
        ),
    ]