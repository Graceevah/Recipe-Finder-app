# Generated by Django 4.2.6 on 2023-11-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_recipe_cooking_time_recipe_preparation_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='cooking_time',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='preparation_time',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='servings',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=''),
        ),
    ]
