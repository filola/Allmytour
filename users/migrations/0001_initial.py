# Generated by Django 3.2.8 on 2021-10-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200)),
                ('is_maker', models.BooleanField(default=False)),
                ('agree_service', models.BooleanField(default=False)),
                ('agree_maketing', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
