# Generated by Django 2.1.3 on 2018-12-03 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0015_auto_20181202_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recette',
            name='nbCalories',
        ),
    ]
