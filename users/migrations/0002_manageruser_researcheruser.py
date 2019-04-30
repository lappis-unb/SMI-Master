# Generated by Django 2.1.5 on 2019-04-29 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerUser',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.CustomUser')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.customuser',),
        ),
        migrations.CreateModel(
            name='ResearcherUser',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.CustomUser')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.customuser',),
        ),
    ]
