# Generated by Django 2.2.6 on 2020-07-29 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burguer', '0020_auto_20200729_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burguer',
            name='hash_id',
            field=models.TextField(default='48b6ef8c-7e02-4e27-9465-624ee4efc0c1', unique=True),
        ),
    ]
