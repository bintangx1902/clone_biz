# Generated by Django 3.1.4 on 2020-12-19 10:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dotbiz', '0002_postpage_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postpage',
            old_name='slug',
            new_name='page_link',
        ),
        migrations.RemoveField(
            model_name='postpage',
            name='post_date',
        ),
        migrations.AddField(
            model_name='postpage',
            name='meta_description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postpage',
            name='meta_keyword',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
