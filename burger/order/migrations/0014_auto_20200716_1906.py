# Generated by Django 2.2.6 on 2020-07-16 19:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20200716_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 19, 6, 41, 389863)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='hash_id',
            field=models.TextField(default='1387ef42-35c7-4637-92fb-db9e729268a7', unique=True),
        ),
    ]