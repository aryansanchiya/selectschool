# Generated by Django 2.2.20 on 2022-01-07 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('compareschool_app', '0018_schooldetail_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooldetail',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
