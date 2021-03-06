# Generated by Django 3.1.4 on 2020-12-28 10:39

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dotbiz', '0024_auto_20201228_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=255)),
                ('sub_title_tag', models.CharField(max_length=255)),
                ('sub_page_link', models.SlugField(max_length=255, unique=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('meta_description', models.TextField()),
                ('meta_keyword', models.TextField()),
                ('parent_page', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='dotbiz.post')),
            ],
        ),
    ]
