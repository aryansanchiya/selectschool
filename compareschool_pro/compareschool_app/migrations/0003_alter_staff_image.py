# Generated by Django 3.2.5 on 2021-12-17 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compareschool_app', '0002_auto_20211217_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Image',
            field=models.ImageField(upload_to='media/pics'),
        ),
    ]
