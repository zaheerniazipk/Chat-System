# Generated by Django 4.1.3 on 2022-12-01 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_friend_list_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('sender', models.TextField(max_length=200)),
                ('reciver', models.TextField(max_length=200)),
            ],
        ),
    ]
