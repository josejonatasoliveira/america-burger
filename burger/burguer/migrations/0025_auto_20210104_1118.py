# Generated by Django 2.2.6 on 2021-01-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burguer', '0024_auto_20200729_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burguer',
            name='hash_id',
            field=models.TextField(default='ace6a6d1-138d-46bf-808f-e46c5ae55408', unique=True),
        ),
    ]
