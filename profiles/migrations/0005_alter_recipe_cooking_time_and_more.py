# Generated by Django 4.2.6 on 2023-11-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_recipe_cooking_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.DurationField(default='00:30:00'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time',
            field=models.DurationField(default='00:30:00'),
        ),
    ]