# Generated by Django 2.2.6 on 2020-07-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0007_auto_20200716_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='hash_id',
            field=models.TextField(default='b26b1c83-86c4-4a34-a6c7-eb8048906f95', unique=True),
        ),
        migrations.AlterField(
            model_name='ticketraffle',
            name='code',
            field=models.TextField(default='3LOZXQ', unique=True),
        ),
    ]
