# Generated by Django 4.0 on 2022-01-15 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_singer_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='image',
        ),
    ]
