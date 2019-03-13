# Generated by Django 2.1.2 on 2019-03-03 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_service_name'),
        ('clinic', '0002_auto_20190303_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qiymet', models.CharField(max_length=64)),
                ('klinika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Service')),
            ],
        ),
        migrations.AddField(
            model_name='clinic',
            name='services',
            field=models.ManyToManyField(related_name='relate_name_services', through='clinic.Prices', to='service.Service'),
        ),
    ]
