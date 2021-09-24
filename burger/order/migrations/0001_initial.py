# Generated by Django 2.2.6 on 2020-05-24 10:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('burguer', '0002_auto_20200524_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2020, 5, 24, 10, 19, 49, 642668))),
                ('value', models.DecimalField(decimal_places=2, default=0.0, help_text='Preço de cada ticket', max_digits=20, verbose_name='Valor')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, help_text='Desconto sobre o ticket se houver', max_digits=20, verbose_name='Desconto Final')),
                ('final_value', models.DecimalField(decimal_places=2, default=0.0, help_text='Valor final da compra', max_digits=20, verbose_name='Valor Final')),
                ('is_paid', models.BooleanField(default=True, help_text='Se a compra foi paga', verbose_name='Foi pago')),
            ],
            options={
                'verbose_name': 'Ordem',
                'verbose_name_plural': 'Ordens',
                'db_table': 'ord_order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_id', models.TextField(default='821cabd0-fa5a-4082-a124-9e1e82def11c', unique=True)),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantidade do Item')),
                ('final_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Preço Final')),
                ('burger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='burguer.Burguer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
            options={
                'verbose_name': 'Item da Ordem',
                'verbose_name_plural': 'Itens da Ordem',
                'db_table': 'order_item',
            },
        ),
    ]