# Generated by Django 3.1.2 on 2020-12-21 14:28

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(blank=True, upload_to=core.models.get_path_for_file),
        ),
    ]
