# Generated by Django 3.1.1 on 2021-02-18 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_thread_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Identificador'),
        ),
    ]
