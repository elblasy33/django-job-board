# Generated by Django 4.2.4 on 2023-08-06 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_jop_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='descraption',
            field=models.TextField(default=' ', max_length=30),
        ),
    ]
