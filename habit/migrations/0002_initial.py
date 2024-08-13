# Generated by Django 4.2 on 2024-08-13 18:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='author',
            field=models.ForeignKey(blank=True, help_text='Укажите автора привычки', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор привычки'),
        ),
    ]
