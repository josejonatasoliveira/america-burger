# Generated by Django 2.2.6 on 2020-07-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0023_auto_20200729_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='hash_id',
            field=models.TextField(default='d0313b6a-8d07-454c-8cad-75ad848044e1', unique=True),
        ),
        migrations.AlterField(
            model_name='ticketraffle',
            name='code',
            field=models.TextField(default='4KY6JY', unique=True),
        ),
    ]
