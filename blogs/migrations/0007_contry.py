# Generated by Django 3.0.3 on 2020-03-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0006_auto_20200323_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_contry', models.CharField(max_length=50)),
            ],
        ),
    ]