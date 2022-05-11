# Generated by Django 4.0.3 on 2022-05-07 07:55

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_jobs_saved_by'),
        ('users', '0003_user_saved_jobs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='saved_jobs',
        ),
        migrations.AddField(
            model_name='user',
            name='saved_jobs',
            field=djongo.models.fields.ArrayReferenceField(blank=True, null=True, on_delete=djongo.models.fields.ArrayReferenceField._on_delete, to='jobs.jobs'),
        ),
    ]
