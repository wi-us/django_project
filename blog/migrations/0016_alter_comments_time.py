# Generated by Django 5.1.7 on 2025-03-23 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_comments_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default=datetime.time(23, 46, 0, 740712), verbose_name='Время публикации комментария'),
        ),
    ]
