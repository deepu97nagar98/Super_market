# Generated by Django 3.1.2 on 2020-10-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue_length', '0003_queuehistory_length_diff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queuehistory',
            name='length_diff',
            field=models.IntegerField(),
        ),
    ]
