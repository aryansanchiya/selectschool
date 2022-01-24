# Generated by Django 2.2.20 on 2022-01-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compareschool_app', '0039_auto_20220119_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campus1', models.ImageField(blank=True, upload_to='media/pics')),
                ('Campus2', models.ImageField(upload_to='media/pics')),
                ('Campus3', models.ImageField(upload_to='media/pics')),
                ('Class1', models.ImageField(upload_to='media/pics')),
                ('Class2', models.ImageField(upload_to='media/pics')),
                ('Class3', models.ImageField(upload_to='media/pics')),
                ('Lab1', models.ImageField(upload_to='media/pics')),
                ('Lab2', models.ImageField(upload_to='media/pics')),
                ('Area1', models.ImageField(upload_to='media/pics')),
                ('Area2', models.ImageField(upload_to='media/pics')),
                ('Area3', models.ImageField(upload_to='media/pics')),
                ('Sports1', models.ImageField(upload_to='media/pics')),
                ('Sports2', models.ImageField(upload_to='media/pics')),
                ('Sports3', models.ImageField(upload_to='media/pics')),
                ('Sports4', models.ImageField(upload_to='media/pics')),
                ('Sports5', models.ImageField(upload_to='media/pics')),
            ],
        ),
    ]
