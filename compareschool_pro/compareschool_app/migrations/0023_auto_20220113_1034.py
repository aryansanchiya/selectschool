# Generated by Django 2.2.20 on 2022-01-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compareschool_app', '0022_auto_20220112_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facalities',
            name='Auditorium',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=11),
        ),
    ]
