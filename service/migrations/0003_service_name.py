# Generated by Django 2.1.2 on 2019-03-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20190303_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
