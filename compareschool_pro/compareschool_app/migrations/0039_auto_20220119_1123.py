# Generated by Django 2.2.20 on 2022-01-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compareschool_app', '0038_auto_20220119_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooldetail',
            name='Social_Developement',
            field=models.CharField(max_length=255),
        ),
    ]