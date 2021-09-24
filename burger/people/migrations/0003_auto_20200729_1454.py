# Generated by Django 2.2.6 on 2020-07-29 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20200716_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 29, 14, 54, 10, 604329), verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hash_id',
            field=models.TextField(default='1cb89530-0421-461f-b8e8-1d8d473a3527', unique=True, verbose_name='ID Unico do Usuário'),
        ),
    ]
