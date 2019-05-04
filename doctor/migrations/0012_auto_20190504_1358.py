# Generated by Django 2.1.2 on 2019-05-04 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_auto_20190428_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='usaq_hekimi',
            field=models.BooleanField(blank=True, null=True, verbose_name='Uşaq həkimi?'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='usaq_hekimi_qiymet',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Uşaq Həkimi Müayinə Qiyməti'),
        ),
    ]
