# Generated by Django 2.1.2 on 2019-03-03 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0009_auto_20190303_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prices',
            name='klinika',
        ),
        migrations.RemoveField(
            model_name='prices',
            name='service',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='services',
        ),
        migrations.DeleteModel(
            name='Prices',
        ),
    ]