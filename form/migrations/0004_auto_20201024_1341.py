# Generated by Django 3.1.2 on 2020-10-24 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20201024_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='extra_skills',
            field=models.ManyToManyField(through='form.FormExtraSkills', to='form.ExtraSkill'),
        ),
        migrations.AlterField(
            model_name='formextraskills',
            name='extra_skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.extraskill'),
        ),
    ]
