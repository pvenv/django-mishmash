# Generated by Django 4.0.2 on 2022-02-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logging', '0003_ws_app'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ws',
            name='app',
            field=models.CharField(max_length=20),
        ),
    ]
