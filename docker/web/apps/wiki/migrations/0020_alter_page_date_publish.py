# Generated by Django 4.0.2 on 2022-03-21 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0019_alter_page_date_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='date_publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 21, 10, 20, 0, 516470), null=True, verbose_name='Дата публикации'),
        ),
    ]
