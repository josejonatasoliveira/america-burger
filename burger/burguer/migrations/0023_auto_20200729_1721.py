# Generated by Django 2.2.6 on 2020-07-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burguer', '0022_auto_20200729_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burguer',
            name='hash_id',
            field=models.TextField(default='aa015a01-6dcc-4796-b63e-7367e439af26', unique=True),
        ),
    ]