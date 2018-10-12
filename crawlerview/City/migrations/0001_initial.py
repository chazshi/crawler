# Generated by Django 2.1.1 on 2018-10-12 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anqing',
            fields=[
                ('title', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('time', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'anqing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hefei',
            fields=[
                ('title', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('time', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'hefei',
                'managed': False,
            },
        ),
    ]