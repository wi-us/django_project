# Generated by Django 5.1.7 on 2025-03-23 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_comments_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default=datetime.time(22, 57, 36, 410075), verbose_name='Время публикации комментария'),
        ),
    ]
