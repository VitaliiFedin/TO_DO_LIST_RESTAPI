# Generated by Django 4.0.4 on 2022-05-01 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0009_remove_task_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
    ]
