# Generated by Django 3.1.2 on 2020-10-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('queue_id', models.IntegerField(primary_key=True, serialize=False)),
                ('queue_size', models.IntegerField()),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
