# Generated by Django 3.2.13 on 2022-05-04 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0022_auto_20220504_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='highlighted',
        ),
    ]
