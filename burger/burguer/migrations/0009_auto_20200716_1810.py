# Generated by Django 2.2.6 on 2020-07-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burguer', '0008_auto_20200716_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burguer',
            name='hash_id',
            field=models.TextField(default='a6c2b372-5e81-4b7e-9b50-2fb48c9d2cf8', unique=True),
        ),
    ]
