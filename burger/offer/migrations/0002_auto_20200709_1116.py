# Generated by Django 2.2.6 on 2020-07-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='hash_id',
            field=models.TextField(default='bc8cc0a8-ff16-4d77-bfa5-abdf8072c76c', unique=True),
        ),
    ]