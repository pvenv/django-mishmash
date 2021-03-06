# Generated by Django 4.0.2 on 2022-02-09 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('priority', models.IntegerField()),
            ],
            options={
                'verbose_name': 'категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(default=1, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('content', models.TextField(blank=True)),
                ('date_publish', models.DateTimeField(null=True, verbose_name='Дата публикации')),
                ('date_edit', models.DateTimeField(null=True, verbose_name='Последнее редактирование')),
            ],
            options={
                'verbose_name': 'страницы',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]
