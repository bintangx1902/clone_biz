# Generated by Django 3.1.4 on 2020-12-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotbiz', '0030_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='file_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
