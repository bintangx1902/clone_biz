# Generated by Django 3.1.4 on 2021-01-09 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotbiz', '0043_auto_20210109_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='header_img',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='quote',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='subpage',
            name='header_img',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='subpage',
            name='quote',
            field=models.CharField(default='', max_length=150),
        ),
    ]
