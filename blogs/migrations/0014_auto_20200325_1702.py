# Generated by Django 3.0.3 on 2020-03-25 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0013_airline_ligne'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plane',
            name='clé_airline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Airline'),
        ),
    ]