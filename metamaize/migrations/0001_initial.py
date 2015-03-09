# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citation',
            fields=[
            ],
            options={
                'db_table': 'Citation',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
            ],
            options={
                'db_table': 'Culture',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
            ],
            options={
                'db_table': 'Medium',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Microbe',
            fields=[
            ],
            options={
                'db_table': 'Microbe',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MicrobeSequence',
            fields=[
            ],
            options={
                'db_table': 'Microbe_Sequence',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
            ],
            options={
                'db_table': 'Person',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Primer',
            fields=[
            ],
            options={
                'db_table': 'Primer',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
            ],
            options={
                'db_table': 'Source',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Temppedigree',
            fields=[
            ],
            options={
                'db_table': 'tempPedigree',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Temprow',
            fields=[
            ],
            options={
                'db_table': 'tempRow',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tissue',
            fields=[
            ],
            options={
                'db_table': 'Tissue',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
