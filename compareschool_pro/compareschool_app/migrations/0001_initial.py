# Generated by Django 3.2.5 on 2021-12-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mobile_No', models.IntegerField()),
                ('Phone_No', models.IntegerField()),
                ('Website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Standard', models.IntegerField()),
                ('Medium', models.CharField(max_length=40)),
                ('Batch', models.CharField(max_length=100)),
                ('Fees', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Address', models.TextField()),
                ('Established', models.DateField()),
                ('Achievements', models.TextField()),
                ('Hostel', models.IntegerField(default=1)),
                ('Sports', models.CharField(max_length=255)),
                ('Image1', models.ImageField(upload_to='media/pics')),
                ('Image2', models.ImageField(upload_to='media/pics')),
                ('Image3', models.ImageField(upload_to='media/pics')),
                ('Image4', models.ImageField(upload_to='media/pics')),
                ('Image5', models.ImageField(upload_to='media/pics')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Study_Carrier', models.CharField(max_length=255)),
                ('Designation', models.CharField(max_length=255)),
                ('Standard', models.IntegerField()),
            ],
        ),
    ]
