# Generated by Django 5.0.7 on 2024-07-18 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('death_app', '0002_alter_obituary_slug_alter_obituary_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obituary',
            name='submission_date',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
