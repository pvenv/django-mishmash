# Generated by Django 4.0.2 on 2022-03-05 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0011_alter_page_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='date_edit',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Последнее редактирование'),
        ),
        migrations.AlterField(
            model_name='page',
            name='date_publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 5, 16, 11, 11, 953731), null=True, verbose_name='Дата публикации'),
        ),
    ]
