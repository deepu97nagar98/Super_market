# Generated by Django 3.1.2 on 2020-10-03 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queue_length', '0004_auto_20201003_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queuehistory',
            name='length_diff',
        ),
    ]
