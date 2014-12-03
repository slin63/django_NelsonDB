# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurementparameter',
            name='unit_of_measure',
            field=models.CharField(default=b'No Units', max_length=200),
            preserve_default=True,
        ),
    ]
