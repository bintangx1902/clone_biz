# Generated by Django 3.1.4 on 2020-12-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotbiz', '0029_auto_20201229_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='img/')),
            ],
        ),
    ]
