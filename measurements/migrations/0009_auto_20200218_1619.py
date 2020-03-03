# Generated by Django 3.0.2 on 2020-02-18 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0008_auto_20200218_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='active_max_power_list_off_peak1',
            new_name='active_max_power_list_off_peak',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='active_max_power_list_off_peak_time1',
            new_name='active_max_power_list_off_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='active_max_power_list_peak1',
            new_name='active_max_power_list_peak',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='active_max_power_list_peak_time1',
            new_name='active_max_power_list_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='active_max_power_off_peak_time1',
            new_name='active_max_power_off_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='active_max_power_peak_time1',
            new_name='active_max_power_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='capacitive_power_off_peak_time1',
            new_name='capacitive_power_off_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='capacitive_power_peak_time1',
            new_name='capacitive_power_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='consumption_off_peak_time1',
            new_name='consumption_off_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='consumption_peak_time1',
            new_name='consumption_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='generated_energy_off_peak_time1',
            new_name='generated_energy_off_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='generated_energy_peak_time1',
            new_name='generated_energy_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='inductive_power_off_peak_time1',
            new_name='inductive_power_off_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='inductive_power_peak_time1',
            new_name='inductive_power_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='reactive_max_power_list_off_peak1',
            new_name='reactive_max_power_list_off_peak',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='reactive_max_power_list_off_peak_time1',
            new_name='reactive_max_power_list_off_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='reactive_max_power_list_peak1',
            new_name='reactive_max_power_list_peak',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='reactive_max_power_list_peak_time1',
            new_name='reactive_max_power_list_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='reactive_max_power_off_peak_time1',
            new_name='reactive_max_power_off_peak_time',
        ),
        migrations.RenameField(
            model_name='monthlymeasurement',
            old_name='reactive_max_power_peak_time1',
            new_name='reactive_max_power_peak_time',
        ),
    ]
