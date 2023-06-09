# Generated by Django 4.1.1 on 2023-05-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0025_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='notification_time',
        ),
        migrations.AddField(
            model_name='goal',
            name='continuing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='goal',
            name='notification_hour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='notification_minutes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='notifications',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='goalexec',
            name='note_id',
            field=models.IntegerField(default=0),
        ),
    ]
