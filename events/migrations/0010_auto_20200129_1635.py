# Generated by Django 3.0.2 on 2020-01-29 16:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slaves', '0005_auto_20200129_1635'),
        ('transductors', '0011_auto_20200129_1635'),
        ('events', '0009_auto_20200129_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, help_text='This field is required', verbose_name='details'),
        ),
        migrations.AlterField(
            model_name='failedconnectionslaveevent',
            name='slave',
            field=models.ForeignKey(help_text='This field is required', on_delete=django.db.models.deletion.CASCADE, related_name='events_failedconnectionslaveevent', to='slaves.Slave', verbose_name='slave'),
        ),
        migrations.AlterField(
            model_name='failedconnectiontransductorevent',
            name='transductor',
            field=models.ForeignKey(help_text='This field is required', on_delete=django.db.models.deletion.CASCADE, related_name='events_failedconnectiontransductorevent', to='transductors.EnergyTransductor', verbose_name='meter'),
        ),
        migrations.AlterField(
            model_name='voltagerelatedevent',
            name='transductor',
            field=models.ForeignKey(help_text='This field is required', on_delete=django.db.models.deletion.CASCADE, related_name='events_voltagerelatedevent', to='transductors.EnergyTransductor', verbose_name='meter'),
        ),
    ]
