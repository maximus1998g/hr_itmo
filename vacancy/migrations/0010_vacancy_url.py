# Generated by Django 3.1.2 on 2021-03-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0009_auto_20210310_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='url',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
