# Generated by Django 2.2.6 on 2020-07-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0014_auto_20200716_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='hash_id',
            field=models.TextField(default='c4037d3a-ceeb-4a35-b301-94dca9e3f50d', unique=True),
        ),
        migrations.AlterField(
            model_name='ticketraffle',
            name='code',
            field=models.TextField(default='3CFUPQ', unique=True),
        ),
    ]