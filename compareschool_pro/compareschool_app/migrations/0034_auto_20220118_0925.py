# Generated by Django 2.2.20 on 2022-01-18 09:25

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('compareschool_app', '0033_auto_20220118_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooldetail',
            name='Image3',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[640, 480], upload_to='media/pics'),
        ),
    ]
