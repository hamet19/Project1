# Generated by Django 3.0.3 on 2020-03-25 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_auto_20200325_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_airline', models.CharField(max_length=200)),
                ('clé_contry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Contry')),
            ],
        ),
        migrations.CreateModel(
            name='Ligne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ligne_direct', models.BooleanField(default=True)),
                ('clé_aeroport_arr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aeroportarr', to='blogs.Aeroport')),
                ('clé_aeroport_dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Aeroport')),
                ('clé_airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Airline')),
            ],
        ),
    ]
