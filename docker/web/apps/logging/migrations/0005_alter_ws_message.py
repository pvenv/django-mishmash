# Generated by Django 4.0.2 on 2022-03-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logging', '0004_alter_ws_app'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ws',
            name='message',
            field=models.CharField(max_length=500),
        ),
    ]
