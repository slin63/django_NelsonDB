# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('citation_type', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=300)),
                ('pubmed_id', models.CharField(max_length=300)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_type', models.CharField(max_length=200)),
                ('media_description', models.CharField(max_length=200)),
                ('media_preparation', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
                ('citation', models.ForeignKey(to='lab.Citation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObsOther',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entity_type', models.CharField(max_length=200)),
                ('dna_id', models.CharField(max_length=200)),
                ('dna_extraction_method', models.CharField(max_length=200)),
                ('dna_date', models.DateField()),
                ('dna_tube_id', models.CharField(max_length=200)),
                ('dna_tube_type', models.CharField(max_length=200)),
                ('dna_comments', models.CharField(max_length=1000)),
                ('tissue_id', models.CharField(max_length=200)),
                ('tissue_type', models.CharField(max_length=200)),
                ('tissue_name', models.CharField(max_length=200)),
                ('tissue_date_ground', models.DateField()),
                ('tissue_comments', models.CharField(max_length=1000)),
                ('plate_id', models.CharField(max_length=200)),
                ('plate_name', models.CharField(max_length=200)),
                ('plate_date_plated', models.DateField()),
                ('plate_contents', models.CharField(max_length=200)),
                ('plate_rep', models.CharField(max_length=200)),
                ('plate_type', models.CharField(max_length=200)),
                ('plate_status', models.CharField(max_length=200)),
                ('plate_comments', models.CharField(max_length=1000)),
                ('sample_id', models.CharField(max_length=200)),
                ('sample_type', models.CharField(max_length=200)),
                ('sample_weight', models.CharField(max_length=200)),
                ('sample_kernel_num', models.CharField(max_length=200)),
                ('sample_comments', models.CharField(max_length=1000)),
                ('well_id', models.CharField(max_length=200)),
                ('well', models.CharField(max_length=200)),
                ('well_inventory', models.CharField(max_length=200)),
                ('well_tube_label', models.CharField(max_length=200)),
                ('well_comments', models.CharField(max_length=1000)),
                ('culture_id', models.CharField(max_length=200)),
                ('culture_name', models.CharField(max_length=200)),
                ('culture_microbe_type', models.CharField(max_length=200)),
                ('culture_plating_cycle', models.CharField(max_length=200)),
                ('culture_dilution', models.CharField(max_length=200)),
                ('culture_image', models.CharField(max_length=200)),
                ('culture_comments', models.CharField(max_length=1000)),
                ('microbe_id', models.CharField(max_length=200)),
                ('microbe_type', models.CharField(max_length=200)),
                ('microbe_comments', models.CharField(max_length=1000)),
                ('location', models.ForeignKey(to='lab.Location')),
                ('medium', models.ForeignKey(to='lab.Medium')),
                ('source_culture', models.ForeignKey(related_name=b'culture_entity', to='lab.ObsOther')),
                ('source_dna', models.ForeignKey(related_name=b'dna_entity', to='lab.ObsOther')),
                ('source_isolate', models.ForeignKey(to='lab.Isolate')),
                ('source_microbe', models.ForeignKey(related_name=b'microbe_entity', to='lab.ObsOther')),
                ('source_plant', models.ForeignKey(to='lab.ObsPlant')),
                ('source_plate', models.ForeignKey(related_name=b'plate_entity', to='lab.ObsOther')),
                ('source_row', models.ForeignKey(to='lab.ObsRow')),
                ('source_sample', models.ForeignKey(related_name=b'sample_entity', to='lab.ObsOther')),
                ('source_stock', models.ForeignKey(to='lab.Stock')),
                ('source_tissue', models.ForeignKey(related_name=b'tissue_entity', to='lab.ObsOther')),
                ('source_well', models.ForeignKey(related_name=b'well_entity', to='lab.ObsOther')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UploadQueue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_name', models.FileField(upload_to=b'upload_queue')),
                ('upload_type', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('comments', models.CharField(max_length=1000)),
                ('experiment', models.ForeignKey(to='lab.Experiment')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
