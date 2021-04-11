# Generated by Django 3.1.2 on 2021-04-10 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0018_auto_20210320_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='CompanyCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'db_table': 'company_categories',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='categories',
            field=models.ManyToManyField(through='company.CompanyCategories', to='company.Category'),
        ),
    ]