# Generated by Django 2.1.5 on 2019-04-29 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190429_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manageruser',
            options={'verbose_name': 'Researcher'},
        ),
        migrations.AlterModelOptions(
            name='researcheruser',
            options={'verbose_name': 'Researcher'},
        ),
    ]