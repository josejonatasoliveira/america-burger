# Generated by Django 2.2.6 on 2020-07-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burguer', '0006_auto_20200709_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burguer',
            name='hash_id',
            field=models.TextField(default='526461b4-b593-48e9-a536-4988c7e359a8', unique=True),
        ),
    ]
