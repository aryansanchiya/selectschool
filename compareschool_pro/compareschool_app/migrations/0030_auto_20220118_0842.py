# Generated by Django 2.2.20 on 2022-01-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compareschool_app', '0029_auto_20220118_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooldetail',
            name='Auditorium',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='schooldetail',
            name='Cafeteria',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='schooldetail',
            name='Computer_lab',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='schooldetail',
            name='Infirmary',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='schooldetail',
            name='Library',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='schooldetail',
            name='Science_lab',
            field=models.CharField(max_length=200),
        ),
    ]