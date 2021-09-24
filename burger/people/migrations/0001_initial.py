# Generated by Django 2.2.6 on 2020-05-24 10:19

import burger.security.models
import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from burger.people.models import Company
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    def save_first_company(apps, schema_editor):
        company = Company(id="722ecc2c-9ccb-4439-b9d2-42e8ee5a7844", code = "1", name = 'América Burger')

        company.save()

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.IntegerField(default=2, help_text='Código da Empresa', verbose_name='Código da Empresa')),
                ('name', models.CharField(default='', help_text='Nome da Empresa', max_length=40, verbose_name='Nome da Empresa')),
            ],
            bases=(models.Model, burger.security.models.PermissionLevelMixin),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('hash_id', models.TextField(default='38a7cc3c-6e4d-443b-ad90-b3cd8ef3d711', unique=True, verbose_name='ID Unico do Usuário')),
                ('profile', models.TextField(blank=True, null=True, verbose_name='Profile')),
                ('first_name', models.CharField(blank=True, help_text='O primeiro nome do usuário', max_length=255, null=True, verbose_name='Primeiro nome')),
                ('last_name', models.CharField(blank=True, help_text='Sobrenome do usuário', max_length=255, null=True, verbose_name='Sobrenome do usuário')),
                ('phone_number', models.CharField(blank=True, help_text='Número do telefone pessoal', max_length=255, null=True, verbose_name='Número do Telefone')),
                ('birthday', models.DateTimeField(default=datetime.datetime(2020, 5, 24, 10, 19, 30, 859670), verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(blank=True, help_text='Cpf do usuário', max_length=11, null=True, verbose_name='Cpf do usuário')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.Address')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Company')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RunPython(save_first_company),
    ]