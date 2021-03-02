# Generated by Django 3.0.2 on 2021-03-02 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campi', '0002_auto_20200409_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('finish_date', models.DateField(blank=True, null=True)),
                ('tariff', models.FloatField(blank=True, max_length=10, null=True)),
                ('campus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='campi.Campus')),
            ],
            options={
                'unique_together': {('start_date', 'finish_date', 'campus')},
            },
        ),
    ]
