# Generated by Django 3.1.4 on 2020-12-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotbiz', '0026_post_parent_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='stats',
            field=models.CharField(default='ACTIVE', max_length=255),
        ),
        migrations.AddField(
            model_name='subpage',
            name='stats',
            field=models.CharField(default='ACTIVE', max_length=255),
        ),
    ]