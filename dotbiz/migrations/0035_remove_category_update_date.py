# Generated by Django 3.1.4 on 2021-01-06 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dotbiz', '0034_category_update_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='update_date',
        ),
    ]
