# Generated by Django 3.2.9 on 2021-11-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NbaFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('link', models.URLField()),
                ('image', models.URLField()),
                ('sourcefeed', models.CharField(max_length=100)),
                ('guid', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PythonFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('link', models.URLField()),
                ('image', models.URLField()),
                ('sourcefeed', models.CharField(max_length=100)),
                ('guid', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RemoteJobsFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('link', models.URLField()),
                ('image', models.URLField()),
                ('sourcefeed', models.CharField(max_length=100)),
                ('guid', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TechFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('link', models.URLField()),
                ('image', models.URLField()),
                ('sourcefeed', models.CharField(max_length=100)),
                ('guid', models.CharField(max_length=50)),
            ],
        ),
    ]
