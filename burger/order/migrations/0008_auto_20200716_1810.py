# Generated by Django 2.2.6 on 2020-07-16 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20200716_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 18, 10, 28, 919034)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='hash_id',
            field=models.TextField(default='d190041a-dfe7-4578-a7a6-ba6133a07d10', unique=True),
        ),
    ]
