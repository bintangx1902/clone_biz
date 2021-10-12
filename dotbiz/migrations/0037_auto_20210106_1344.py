# Generated by Django 3.1.4 on 2021-01-06 13:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dotbiz', '0036_category_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subpage',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subpage',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]