# Generated by Django 4.0.4 on 2022-04-29 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_task_task_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_priority',
        ),
    ]
