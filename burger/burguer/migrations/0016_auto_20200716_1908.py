# Generated by Django 2.2.6 on 2020-07-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burguer', '0015_auto_20200716_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burguer',
            name='hash_id',
            field=models.TextField(default='0b6e2e11-6c53-4dd6-b84b-07633d7ea626', unique=True),
        ),
    ]