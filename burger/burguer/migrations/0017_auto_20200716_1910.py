# Generated by Django 2.2.6 on 2020-07-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burguer', '0016_auto_20200716_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burguer',
            name='hash_id',
            field=models.TextField(default='4babf03d-ce2c-48e0-a78f-652edb602384', unique=True),
        ),
    ]