# Generated by Django 3.1.5 on 2021-01-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotbiz', '0047_auto_20210122_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropdownURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DropdownTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.ManyToManyField(to='dotbiz.DropdownURL')),
            ],
        ),
    ]
