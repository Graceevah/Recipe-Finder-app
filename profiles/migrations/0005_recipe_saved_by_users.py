# Generated by Django 4.2.6 on 2023-12-10 06:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_favoriterecipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='saved_by_users',
            field=models.ManyToManyField(blank=True, related_name='saved_recipes', to=settings.AUTH_USER_MODEL),
        ),
    ]
