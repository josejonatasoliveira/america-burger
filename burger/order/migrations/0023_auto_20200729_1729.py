# Generated by Django 2.2.6 on 2020-07-29 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0022_auto_20200729_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 29, 17, 29, 42, 246003)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='hash_id',
            field=models.TextField(default='c1779df4-d798-4195-bd2c-073f3666bda9', unique=True),
        ),
    ]
