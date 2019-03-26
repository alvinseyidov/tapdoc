# Generated by Django 2.1.2 on 2019-03-26 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0023_clinic_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='phone',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='diaqnostikalarprices',
            name='diaqnostika',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qiymetler', to='service.Diaqnostikalar'),
        ),
        migrations.AlterField(
            model_name='xidmetlerprices',
            name='xidmet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qiymetler', to='service.Xidmatlar'),
        ),
    ]
