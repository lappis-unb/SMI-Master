# Generated by Django 2.1.5 on 2020-01-21 11:12

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20200121_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
