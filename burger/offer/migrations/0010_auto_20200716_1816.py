# Generated by Django 2.2.6 on 2020-07-16 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0009_auto_20200716_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='hash_id',
            field=models.TextField(default='b4731f77-1b6e-480a-ab61-83e948b20aa7', unique=True),
        ),
        migrations.AlterField(
            model_name='ticketraffle',
            name='code',
            field=models.TextField(default='6TXFHG', unique=True),
        ),
    ]
