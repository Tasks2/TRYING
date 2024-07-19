# Generated by Django 5.0.7 on 2024-07-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('death_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obituary',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterModelTable(
            name='obituary',
            table='obituaries',
        ),
    ]
