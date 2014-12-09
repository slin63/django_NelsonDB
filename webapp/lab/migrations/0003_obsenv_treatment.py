# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_measurementparameter_unit_of_measure'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObsEnv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('environment_id', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
                ('field', models.ForeignKey(to='lab.Field')),
                ('obs_selector', models.ForeignKey(to='lab.ObsSelector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('treatment_id', models.CharField(max_length=200)),
                ('treatment_type', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
                ('obs_selector', models.ForeignKey(to='lab.ObsSelector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
