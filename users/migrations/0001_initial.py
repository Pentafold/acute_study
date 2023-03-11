# Generated by Django 4.1.7 on 2023-03-11 15:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=254, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('mobile_number', models.CharField(blank=True, max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('designation', models.CharField(blank=True, max_length=50, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('whitelabel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.whitelabel')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]