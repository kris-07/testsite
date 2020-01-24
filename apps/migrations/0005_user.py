# Generated by Django 3.0.2 on 2020-01-24 07:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_auto_20200124_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(default=datetime.datetime(1990, 1, 1, 0, 0))),
                ('sex', models.CharField(max_length=10)),
                ('bio', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('pincode', models.IntegerField(default=0)),
            ],
        ),
    ]
