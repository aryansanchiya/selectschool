# Generated by Django 2.2.20 on 2022-01-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compareschool_app', '0047_broucher_broucherschoolname'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooldetail',
            name='broucher',
            field=models.FileField(null=True, upload_to='files/', verbose_name=''),
        ),
        migrations.DeleteModel(
            name='Broucher',
        ),
    ]
