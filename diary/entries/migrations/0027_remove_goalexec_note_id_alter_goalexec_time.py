# Generated by Django 4.2.1 on 2023-05-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0026_remove_goal_notification_time_goal_continuing_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goalexec',
            name='note_id',
        ),
        migrations.AlterField(
            model_name='goalexec',
            name='time',
            field=models.CharField(default='2023-05-10', max_length=25),
        ),
    ]
