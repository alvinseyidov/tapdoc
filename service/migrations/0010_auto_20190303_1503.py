# Generated by Django 2.1.2 on 2019-03-03 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_xidmatlar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xidmatlar',
            name='service_group',
        ),
        migrations.DeleteModel(
            name='Xidmatlar',
        ),
    ]