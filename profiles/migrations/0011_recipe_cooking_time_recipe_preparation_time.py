# Generated by Django 4.2.6 on 2023-11-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_remove_recipe_preparation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='preparation_time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]