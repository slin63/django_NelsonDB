# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
        ('legacy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dna_tube_id', models.CharField(max_length=200)),
                ('jbc_dna_id', models.CharField(max_length=200)),
                ('dna_tube_type', models.CharField(max_length=200)),
                ('extraction_method', models.CharField(max_length=200)),
                ('date_made', models.DateField(null=True, blank=True)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plate_id', models.CharField(max_length=200)),
                ('plate_name', models.CharField(max_length=200)),
                ('plate_contents', models.CharField(max_length=20, choices=[(b'Tissue', b'Tissue'), (b'DNA', b'DNA'), (b'RNA', b'RNA'), (b'PCR Products', b'PCR Products')])),
                ('plate_rep', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('container', models.CharField(max_length=200)),
                ('plate_type', models.CharField(max_length=40, choices=[(b'96 Well Costar Rack', b'96 Well Costar Rack')])),
                ('status', models.CharField(max_length=20, choices=[(b'Success', b'Success'), (b'Empty', b'Empty'), (b'Lost', b'Lost')])),
                ('date_made', models.DateField(null=True, blank=True)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('well_id', models.CharField(max_length=200)),
                ('well', models.CharField(max_length=200)),
                ('plant', models.CharField(max_length=1, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C')])),
                ('inventory', models.CharField(max_length=20, choices=[(b'+', b'+'), (b'-', b'-'), (b'E', b'E'), (b'X', b'X'), (b'No Tube', b'No Tube')])),
                ('comments', models.CharField(max_length=1000)),
                ('obs_row', models.ForeignKey(to='lab.ObsRow')),
                ('plate', models.ForeignKey(to='jmaize.Plate')),
                ('tissue', models.ForeignKey(related_name=b'tissue_well', to='legacy.Legacy_Tissue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='donor',
            name='donor_well',
            field=models.ForeignKey(related_name=b'donor_well', to='jmaize.Well'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donor',
            name='target_well',
            field=models.ForeignKey(related_name=b'target_well', to='jmaize.Well'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dna',
            name='dna_well',
            field=models.ForeignKey(to='jmaize.Well'),
            preserve_default=True,
        ),
    ]
