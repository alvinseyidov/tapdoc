# Generated by Django 2.1.2 on 2019-05-05 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_clinic_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='fulltime',
            field=models.BooleanField(blank=True, null=True, verbose_name='24 saat işləyir'),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='city',
            field=models.CharField(blank=True, choices=[('Bakı', 'Bakı'), ('Sumqayıt', 'Sumqayıt'), ('Gəncə', 'Gəncə'), ('Qəbələ', 'Qəbələ')], max_length=25, null=True, verbose_name='Şəhər'),
        ),
    ]
