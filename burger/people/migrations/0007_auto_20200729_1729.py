# Generated by Django 2.2.6 on 2020-07-29 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20200729_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 29, 17, 29, 42, 129153), verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hash_id',
            field=models.TextField(default='38c596f9-22ef-4967-8412-53abbdbf2dec', unique=True, verbose_name='ID Unico do Usuário'),
        ),
    ]