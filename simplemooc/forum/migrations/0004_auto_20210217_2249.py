# Generated by Django 3.1.1 on 2021-02-18 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20210217_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Identificador'),
        ),
    ]
