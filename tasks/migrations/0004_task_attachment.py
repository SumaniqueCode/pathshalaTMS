# Generated by Django 5.2.1 on 2025-06-19 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='tasks/{instance.id}/attachments'),
        ),
    ]
