# Generated by Django 5.1.7 on 2025-03-23 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='time',
            field=models.TimeField(default=datetime.time(22, 12, 9, 749040), verbose_name='Время публикации комментария'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.date(2025, 3, 23), verbose_name='Дата публикации комментария'),
        ),
    ]
