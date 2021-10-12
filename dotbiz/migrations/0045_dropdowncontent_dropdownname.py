# Generated by Django 3.1.4 on 2021-01-10 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotbiz', '0044_auto_20210109_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropdownContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DropdownName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(max_length=150)),
            ],
        ),
    ]