# Generated by Django 2.2.6 on 2020-07-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0006_auto_20200709_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='hash_id',
            field=models.TextField(default='da3a9c49-d075-4d1d-9f7f-f3d23d137bb3', unique=True),
        ),
        migrations.AlterField(
            model_name='ticketraffle',
            name='code',
            field=models.TextField(default='MWQ98R', unique=True),
        ),
    ]
