# Generated by Django 4.1.7 on 2023-04-28 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestPlace', '0002_dish_place_place_category'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='localisation',
            unique_together={('longitude', 'latitude')},
        ),
    ]
