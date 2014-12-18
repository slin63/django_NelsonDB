# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obssample',
            name='source_sample',
            field=models.ForeignKey(default=1, to='lab.ObsSample'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obssample',
            name='stock',
            field=models.ForeignKey(default=1, to='lab.Stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='inoculated',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
