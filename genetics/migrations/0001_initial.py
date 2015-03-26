# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GWASExperimentSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('experiment', models.ForeignKey(to='lab.Experiment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GWASResults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('p_value', models.CharField(max_length=200)),
                ('strand', models.CharField(max_length=200)),
                ('relationship_to_hit', models.CharField(max_length=200)),
                ('interpro_domain', models.CharField(max_length=200)),
                ('distance_from_gene', models.CharField(max_length=200)),
                ('f_value', models.CharField(max_length=200)),
                ('perm_p_value', models.CharField(max_length=200)),
                ('r2', models.CharField(max_length=200)),
                ('alleles', models.CharField(max_length=200)),
                ('bpp', models.CharField(max_length=200)),
                ('effect', models.CharField(max_length=200)),
                ('cM', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MapFeature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chromosome', models.CharField(max_length=200)),
                ('genetic_bin', models.CharField(max_length=200)),
                ('genetic_map', models.CharField(max_length=200)),
                ('genetic_position', models.CharField(max_length=200)),
                ('locus_type', models.CharField(max_length=200)),
                ('locus_name', models.CharField(max_length=200)),
                ('physical_position', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MapFeatureAnnotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annotation_type', models.CharField(max_length=200)),
                ('annotation_value', models.CharField(max_length=200)),
                ('map_feature', models.ForeignKey(to='genetics.MapFeature')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marker_name', models.CharField(max_length=200)),
                ('ref_seq', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('length', models.CharField(max_length=200)),
                ('map_feature', models.ForeignKey(to='genetics.MapFeature')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gwasresults',
            name='marker',
            field=models.ForeignKey(to='genetics.Marker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gwasresults',
            name='parameter',
            field=models.ForeignKey(to='lab.MeasurementParameter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gwasexperimentset',
            name='gwas_result',
            field=models.ForeignKey(to='genetics.GWASResults'),
            preserve_default=True,
        ),
    ]
