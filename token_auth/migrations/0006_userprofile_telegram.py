# Generated by Django 3.1.2 on 2020-10-24 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_auth', '0005_auto_20201024_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='telegram',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
