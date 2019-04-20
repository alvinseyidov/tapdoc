# Generated by Django 2.1.2 on 2019-04-20 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0018_auto_20190419_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaqnostikalar',
            name='diaqnostika_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diaqnostikalar', to='service.DiaqnostikalarGroup', verbose_name='Diaqnostik Xidmətin Adı'),
        ),
        migrations.AlterField(
            model_name='diaqnostikalargroup',
            name='group_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Diaqnostik Xidmət Qrupun Adı'),
        ),
        migrations.AlterField(
            model_name='diaqnostikalargroup',
            name='group_name_az',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Diaqnostik Xidmət Qrupun Adı'),
        ),
        migrations.AlterField(
            model_name='diaqnostikalargroup',
            name='group_name_ru',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Diaqnostik Xidmət Qrupun Adı'),
        ),
        migrations.AlterField(
            model_name='xidmatlar',
            name='service_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='xidmetler', to='service.XidmatlarGroup', verbose_name='Xidmətin Adı'),
        ),
        migrations.AlterField(
            model_name='xidmatlargroup',
            name='group_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Xidmət Qrup Adı'),
        ),
        migrations.AlterField(
            model_name='xidmatlargroup',
            name='group_name_az',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Xidmət Qrup Adı'),
        ),
        migrations.AlterField(
            model_name='xidmatlargroup',
            name='group_name_ru',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Xidmət Qrup Adı'),
        ),
    ]
