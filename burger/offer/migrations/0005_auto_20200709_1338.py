# Generated by Django 2.2.6 on 2020-07-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0004_auto_20200709_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='hash_id',
            field=models.TextField(default='35c26967-8eca-44b0-9d73-fda1f4dcf3de', unique=True),
        ),
        migrations.AlterField(
            model_name='ticketraffle',
            name='code',
            field=models.TextField(default='3HSVCF', unique=True),
        ),
    ]
