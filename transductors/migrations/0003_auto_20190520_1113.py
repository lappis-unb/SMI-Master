# Generated by Django 2.1.5 on 2019-05-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transductors', '0002_energytransductor_polymorphic_ctype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energytransductor',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='calibration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='creation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='last_data_collection',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='energytransductor',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
