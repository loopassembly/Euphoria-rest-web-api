# Generated by Django 4.0 on 2022-02-13 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0009_cov_name_name_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cov_data',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='cov_data',
            name='time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='cov_name',
            name='number',
            field=models.IntegerField(unique=True),
        ),
    ]
