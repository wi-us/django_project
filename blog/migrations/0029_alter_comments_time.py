# Generated by Django 5.1.7 on 2025-03-29 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_alter_comments_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default=datetime.time(14, 12, 10, 56684), verbose_name='Время публикации комментария'),
        ),
    ]
