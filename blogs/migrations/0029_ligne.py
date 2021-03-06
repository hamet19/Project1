# Generated by Django 3.0.3 on 2020-03-26 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0028_delete_ligne'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ligne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrete', models.CharField(max_length=20)),
                ('type_avion', models.CharField(max_length=200)),
                ('clé_aeroport_arr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aeroportarr', to='blogs.Aeroport')),
                ('clé_aeroport_dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Aeroport')),
                ('clé_airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Airline')),
            ],
        ),
    ]
