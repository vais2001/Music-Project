# Generated by Django 4.2.3 on 2023-08-09 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_watch_later'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch_later',
            name='video_id',
            field=models.CharField(default='', max_length=10000),
        ),
    ]