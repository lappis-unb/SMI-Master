# Generated by Django 2.1.5 on 2019-09-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transductors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energytransductor',
            name='model',
            field=models.CharField(max_length=256),
        ),
    ]
