# Generated by Django 5.1.7 on 2025-03-23 19:48

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comments_post_alter_comments_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(default=datetime.time(22, 48, 23, 287510), verbose_name='Время публикации комментария'),
        ),
    ]
