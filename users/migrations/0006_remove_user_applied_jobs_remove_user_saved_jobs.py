# Generated by Django 4.0.3 on 2022-05-10 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_applied_jobs_alter_user_saved_jobs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='applied_jobs',
        ),
        migrations.RemoveField(
            model_name='user',
            name='saved_jobs',
        ),
    ]