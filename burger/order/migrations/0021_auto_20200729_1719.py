# Generated by Django 2.2.6 on 2020-07-29 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_auto_20200729_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 29, 17, 19, 7, 951031)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='hash_id',
            field=models.TextField(default='f9c3cbc4-ccb1-4ee1-9922-19622fa10cfb', unique=True),
        ),
    ]
