# Generated by Django 2.1.2 on 2019-03-19 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0021_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinicreviews', to='clinic.Clinic'),
        ),
    ]