# Generated by Django 4.1.3 on 2022-12-01 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_messages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='messages',
            new_name='msg',
        ),
    ]