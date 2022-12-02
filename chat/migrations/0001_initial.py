# Generated by Django 4.1.3 on 2022-11-30 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=1000)),
                ('reply', models.BooleanField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
