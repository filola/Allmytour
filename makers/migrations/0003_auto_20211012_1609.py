# Generated by Django 3.2.8 on 2021-10-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makers', '0002_auto_20211012_1431'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avaliable_service',
            new_name='Available_schedule',
        ),
        migrations.RenameModel(
            old_name='Avaliable_schedule',
            new_name='Available_service',
        ),
        migrations.RenameField(
            model_name='available_schedule',
            old_name='service',
            new_name='schedule',
        ),
        migrations.RenameField(
            model_name='available_service',
            old_name='schedule',
            new_name='service',
        ),
        migrations.RemoveField(
            model_name='maker',
            name='avaliable_schedule',
        ),
        migrations.RemoveField(
            model_name='maker',
            name='avaliable_service',
        ),
        migrations.AddField(
            model_name='maker',
            name='available_schedule',
            field=models.ManyToManyField(blank=True, to='makers.Available_schedule'),
        ),
        migrations.AddField(
            model_name='maker',
            name='available_service',
            field=models.ManyToManyField(blank=True, to='makers.Available_service'),
        ),
        migrations.AlterModelTable(
            name='available_schedule',
            table='available_schdules',
        ),
        migrations.AlterModelTable(
            name='available_service',
            table='available_services',
        ),
    ]
