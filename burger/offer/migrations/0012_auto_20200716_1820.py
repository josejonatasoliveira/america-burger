# Generated by Django 2.2.6 on 2020-07-16 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0011_auto_20200716_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='hash_id',
            field=models.TextField(default='574c5c48-2b2f-4e87-85f1-335a1c3865b2', unique=True),
        ),
        migrations.AlterField(
            model_name='ticketraffle',
            name='code',
            field=models.TextField(default='3QTFMC', unique=True),
        ),
    ]