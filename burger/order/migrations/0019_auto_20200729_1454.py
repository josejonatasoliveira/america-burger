# Generated by Django 2.2.6 on 2020-07-29 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_auto_20200716_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 29, 14, 54, 10, 722694)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='hash_id',
            field=models.TextField(default='99db96d8-d152-43d5-8866-814e397725cc', unique=True),
        ),
    ]
