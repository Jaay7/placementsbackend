# Generated by Django 4.0.3 on 2022-04-21 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='job_start_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
