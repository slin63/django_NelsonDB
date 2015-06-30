# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20150618_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maizesample',
            old_name='description',
            new_name='appearance',
        ),
        migrations.RenameField(
            model_name='maizesample',
            old_name='sample_source',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='maizesample',
            old_name='type_of_source',
            new_name='gps_altitude',
        ),
        migrations.RemoveField(
            model_name='maizesample',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='maizesample',
            name='locality',
        ),
        migrations.AddField(
            model_name='maizesample',
            name='gps_accuracy',
            field=models.CharField(default='No Maize Sample', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maizesample',
            name='gps_latitude',
            field=models.CharField(default='No Maize Sample', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maizesample',
            name='gps_longitude',
            field=models.CharField(default='No Maize Sample', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maizesample',
            name='harvest_date',
            field=models.CharField(default='No Maize Sample', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maizesample',
            name='maize_variety',
            field=models.CharField(default='No Maize Sample', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maizesample',
            name='moisture_content',
            field=models.CharField(default='No Maize Sample', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maizesample',
            name='seed_source',
            field=models.CharField(default='No Maize Sample', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maizesample',
            name='source_type',
            field=models.CharField(default='No Maize Sample', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maizesample',
            name='storage_conditions',
            field=models.CharField(default='No Maize Sample', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maizesample',
            name='storage_months',
            field=models.CharField(default='No Maize Sample', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maizesample',
            name='sub_location',
            field=models.CharField(default='No Maize Sample', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maizesample',
            name='village',
            field=models.CharField(default='No Maize Sample', max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
