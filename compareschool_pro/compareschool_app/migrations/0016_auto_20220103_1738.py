# Generated by Django 2.2.20 on 2022-01-03 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compareschool_app', '0015_auto_20220101_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='School_Name_id',
            new_name='SchoolName',
        ),
    ]