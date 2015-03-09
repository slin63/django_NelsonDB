# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='Collecting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection_date', models.CharField(max_length=200)),
                ('collection_method', models.CharField(max_length=1000, blank=True)),
                ('comments', models.CharField(max_length=1000, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DiseaseInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('common_name', models.CharField(max_length=200)),
                ('abbrev', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('start_date', models.CharField(max_length=200)),
                ('purpose', models.CharField(max_length=1000)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=200)),
                ('field_num', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Isolate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isolate_id', models.CharField(max_length=200)),
                ('isolate_name', models.CharField(max_length=200)),
                ('plant_organ', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
                ('disease_info', models.ForeignKey(to='lab.DiseaseInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building_name', models.CharField(max_length=200)),
                ('location_name', models.CharField(max_length=200)),
                ('room', models.CharField(max_length=200)),
                ('shelf', models.CharField(max_length=200)),
                ('column', models.CharField(max_length=200)),
                ('box_name', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
                ('locality', models.ForeignKey(to='lab.Locality')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_of_measurement', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeasurementParameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parameter', models.CharField(max_length=200)),
                ('parameter_type', models.CharField(max_length=200)),
                ('unit_of_measure', models.CharField(default=b'No Units', max_length=200)),
                ('protocol', models.CharField(max_length=1000)),
                ('trait_id_buckler', models.CharField(max_length=200)),
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
            name='ObsCulture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('culture_id', models.CharField(max_length=200)),
                ('culture_name', models.CharField(max_length=200)),
                ('microbe_type', models.CharField(max_length=200)),
                ('plating_cycle', models.CharField(max_length=200)),
                ('dilution', models.CharField(max_length=200)),
                ('image_filename', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObsDNA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dna_id', models.CharField(max_length=200)),
                ('extraction_method', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=200)),
                ('tube_id', models.CharField(max_length=200)),
                ('tube_type', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObsEnv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('environment_id', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObsMicrobe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('microbe_id', models.CharField(max_length=200)),
                ('microbe_type', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObsPlant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plant_id', models.CharField(max_length=200)),
                ('plant_num', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObsPlate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plate_id', models.CharField(max_length=200)),
                ('plate_name', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('contents', models.CharField(max_length=200)),
                ('rep', models.CharField(max_length=200)),
                ('plate_type', models.CharField(max_length=200)),
                ('plate_status', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObsRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row_id', models.CharField(max_length=200)),
                ('row_name', models.CharField(max_length=200)),
                ('range_num', models.CharField(max_length=200)),
                ('plot', models.CharField(max_length=200)),
                ('block', models.CharField(max_length=200)),
                ('rep', models.CharField(max_length=200)),
                ('kernel_num', models.CharField(max_length=200)),
                ('planting_date', models.CharField(max_length=200)),
                ('harvest_date', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObsSample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sample_id', models.CharField(max_length=200)),
                ('sample_type', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('kernel_num', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObsTissue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tissue_id', models.CharField(max_length=200)),
                ('tissue_type', models.CharField(max_length=200)),
                ('tissue_name', models.CharField(max_length=200)),
                ('date_ground', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObsTracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entity_type', models.CharField(max_length=200)),
                ('collecting', models.ForeignKey(to='lab.Collecting')),
                ('experiment', models.ForeignKey(to='lab.Experiment')),
                ('field', models.ForeignKey(to='lab.Field')),
                ('isolate', models.ForeignKey(to='lab.Isolate')),
                ('location', models.ForeignKey(to='lab.Location')),
                ('medium', models.ForeignKey(to='lab.Medium')),
                ('obs_culture', models.OneToOneField(to='lab.ObsCulture')),
                ('obs_dna', models.OneToOneField(to='lab.ObsDNA')),
                ('obs_env', models.OneToOneField(to='lab.ObsEnv')),
                ('obs_microbe', models.OneToOneField(to='lab.ObsMicrobe')),
                ('obs_plant', models.OneToOneField(to='lab.ObsPlant')),
                ('obs_plate', models.OneToOneField(to='lab.ObsPlate')),
                ('obs_row', models.OneToOneField(to='lab.ObsRow')),
                ('obs_sample', models.OneToOneField(to='lab.ObsSample')),
                ('obs_tissue', models.OneToOneField(to='lab.ObsTissue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObsWell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('well_id', models.CharField(max_length=200)),
                ('well', models.CharField(max_length=200)),
                ('well_inventory', models.CharField(max_length=200)),
                ('tube_label', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collecting', models.ForeignKey(to='lab.Collecting')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publisher', models.CharField(max_length=200)),
                ('name_of_paper', models.CharField(max_length=200)),
                ('publish_date', models.DateField()),
                ('publication_info', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seed_id', models.CharField(max_length=200)),
                ('seed_name', models.CharField(max_length=200)),
                ('cross_type', models.CharField(max_length=200)),
                ('pedigree', models.CharField(max_length=200)),
                ('stock_status', models.CharField(max_length=200)),
                ('stock_date', models.CharField(max_length=200)),
                ('inoculated', models.BooleanField(default=False)),
                ('comments', models.CharField(max_length=1000)),
                ('passport', models.ForeignKey(to='lab.Passport')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StockPacket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.CharField(max_length=200)),
                ('num_seeds', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=1000)),
                ('location', models.ForeignKey(to='lab.Location')),
                ('stock', models.ForeignKey(to='lab.Stock')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genus', models.CharField(max_length=200)),
                ('species', models.CharField(max_length=200)),
                ('population', models.CharField(max_length=200)),
                ('common_name', models.CharField(max_length=200)),
                ('alias', models.CharField(max_length=200)),
                ('race', models.CharField(max_length=200)),
                ('subtaxa', models.CharField(max_length=200)),
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
                ('experiment', models.ForeignKey(to='lab.Experiment')),
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
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.CharField(max_length=250)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('phone', models.CharField(max_length=30)),
                ('organization', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=1000)),
                ('job_title', models.CharField(max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='passport',
            name='people',
            field=models.ForeignKey(to='lab.People'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='passport',
            name='taxonomy',
            field=models.ForeignKey(to='lab.Taxonomy'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='obs_well',
            field=models.OneToOneField(to='lab.ObsWell'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='source_obs_culture',
            field=models.ForeignKey(related_name=b'source_culture', to='lab.ObsTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='source_obs_dna',
            field=models.ForeignKey(related_name=b'source_dna', to='lab.ObsTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='source_obs_env',
            field=models.ForeignKey(related_name=b'source_env', to='lab.ObsTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='source_obs_microbe',
            field=models.ForeignKey(related_name=b'source_microbe', to='lab.ObsTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='source_obs_plant',
            field=models.ForeignKey(related_name=b'source_plant', to='lab.ObsTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='source_obs_plate',
            field=models.ForeignKey(related_name=b'source_plate', to='lab.ObsTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='source_obs_row',
            field=models.ForeignKey(related_name=b'source_row', to='lab.ObsTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='source_obs_sample',
            field=models.ForeignKey(related_name=b'source_sample', to='lab.ObsTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='source_obs_tissue',
            field=models.ForeignKey(related_name=b'source_tissue', to='lab.ObsTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='source_obs_well',
            field=models.ForeignKey(related_name=b'source_well', to='lab.ObsTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='stock',
            field=models.ForeignKey(to='lab.Stock'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='obstracker',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measurement',
            name='measurement_parameter',
            field=models.ForeignKey(to='lab.MeasurementParameter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measurement',
            name='obs_tracker',
            field=models.ForeignKey(to='lab.ObsTracker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measurement',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='isolate',
            name='location',
            field=models.ForeignKey(to='lab.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='isolate',
            name='passport',
            field=models.ForeignKey(to='lab.Passport'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='field',
            name='locality',
            field=models.ForeignKey(to='lab.Locality'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experiment',
            name='field',
            field=models.ForeignKey(to='lab.Field'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experiment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='collecting',
            name='field',
            field=models.ForeignKey(to='lab.Field'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='collecting',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
