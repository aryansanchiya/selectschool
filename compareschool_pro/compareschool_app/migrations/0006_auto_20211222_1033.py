# Generated by Django 3.2.5 on 2021-12-22 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('compareschool_app', '0005_remove_schooldetail_image4'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooldetail',
            name='Email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schooldetail',
            name='Hostel',
            field=models.CharField(max_length=100),
        ),
    ]