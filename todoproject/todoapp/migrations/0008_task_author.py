# Generated by Django 4.0.4 on 2022-04-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_alter_task_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.CharField(default='User', max_length=255),
        ),
    ]
