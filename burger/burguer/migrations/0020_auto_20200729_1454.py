# Generated by Django 2.2.6 on 2020-07-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burguer', '0019_auto_20200716_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='burguer',
            name='burger_type',
            field=models.IntegerField(choices=[(1, 'Burger Unico'), (2, 'Combo Simples'), (3, 'Combo Duplo')], default=1, help_text='Tipo do produto vendido', verbose_name='Tipo do produto vendido'),
        ),
        migrations.AlterField(
            model_name='burguer',
            name='hash_id',
            field=models.TextField(default='b74bd872-9900-4f84-8cb9-a4d8ca943187', unique=True),
        ),
    ]
