# Generated by Django 5.1.3 on 2024-11-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
