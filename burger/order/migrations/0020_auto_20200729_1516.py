# Generated by Django 2.2.6 on 2020-07-29 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_auto_20200729_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 29, 15, 16, 20, 103211)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='hash_id',
            field=models.TextField(default='9c847b76-bc06-41b4-9fb7-8410946e7639', unique=True),
        ),
    ]
