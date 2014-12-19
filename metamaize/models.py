# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Citation(models.Model):
    citation_id = models.IntegerField(db_column='Citation_ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=50, blank=True)  # Field name made lowercase.
    pubmed_id = models.CharField(db_column='Pubmed_ID', max_length=10, blank=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=2000, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Citation'


class Culture(models.Model):
    culture_id = models.IntegerField(db_column='Culture_ID', primary_key=True)  # Field name made lowercase.
    row = models.ForeignKey('Temprow', db_column='Row_ID')  # Field name made lowercase.
    pedigree_label = models.ForeignKey('Temppedigree', db_column='Pedigree_Label')  # Field name made lowercase.
    person = models.ForeignKey('Person', db_column='Person_ID')  # Field name made lowercase.
    medium = models.ForeignKey('Medium', db_column='Medium_ID')  # Field name made lowercase.
    tissue = models.ForeignKey('Tissue', db_column='Tissue_ID')  # Field name made lowercase.
    culture_name = models.CharField(db_column='Culture_Name', max_length=30)  # Field name made lowercase.
    microbe_type_observed = models.CharField(db_column='Microbe_Type_Observed', max_length=8, blank=True)  # Field name made lowercase.
    plating_cycle = models.IntegerField(db_column='Plating_Cycle')  # Field name made lowercase.
    dilution = models.CharField(db_column='Dilution', max_length=10)  # Field name made lowercase.
    image_location = models.CharField(db_column='Image_Location', max_length=100, blank=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=2000, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Culture'


class Medium(models.Model):
    medium_id = models.CharField(db_column='Medium_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=2000)  # Field name made lowercase.
    citation = models.ForeignKey(Citation, db_column='Citation_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medium'


class Microbe(models.Model):
    microbe_id = models.IntegerField(db_column='Microbe_ID', primary_key=True)  # Field name made lowercase.
    source_culture = models.ForeignKey(Culture, db_column='Source_Culture', blank=True, null=True)  # Field name made lowercase.
    source_tissue = models.ForeignKey('Tissue', db_column='Source_Tissue', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=8, blank=True)  # Field name made lowercase.
    sequence = models.ForeignKey('MicrobeSequence', db_column='Sequence_ID', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=2000, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Microbe'


class MicrobeSequence(models.Model):
    microbe_sequence_id = models.IntegerField(db_column='Microbe_Sequence_ID', primary_key=True)  # Field name made lowercase.
    sequence = models.CharField(db_column='Sequence', max_length=1500)  # Field name made lowercase.
    f_primer_id = models.IntegerField(db_column='F_Primer_ID')  # Field name made lowercase.
    r_primer_id = models.IntegerField(db_column='R_Primer_ID')  # Field name made lowercase.
    taxonomy = models.CharField(db_column='Taxonomy', max_length=100, blank=True)  # Field name made lowercase.
    source_tissue = models.ForeignKey('Tissue', db_column='Source_Tissue', blank=True, null=True)  # Field name made lowercase.
    source_culture = models.ForeignKey(Culture, db_column='Source_Culture', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=2000, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Microbe_Sequence'


class Person(models.Model):
    person_id = models.IntegerField(db_column='Person_ID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=255)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=10, blank=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=40)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=2000, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person'


class Primer(models.Model):
    primer_id = models.IntegerField(db_column='Primer_ID', primary_key=True)  # Field name made lowercase.
    primer_number = models.CharField(db_column='Primer_Number', max_length=10)  # Field name made lowercase.
    sequence = models.CharField(db_column='Sequence', max_length=255)  # Field name made lowercase.
    direction = models.CharField(db_column='Direction', max_length=1)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=1)  # Field name made lowercase.
    target = models.CharField(db_column='Target', max_length=255, blank=True)  # Field name made lowercase.
    purpose = models.CharField(db_column='Purpose', max_length=255, blank=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=2000, blank=True)  # Field name made lowercase.
    citation = models.ForeignKey(Citation, db_column='Citation_ID')  # Field name made lowercase.
    source = models.ForeignKey('Source', db_column='Source_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Primer'


class Source(models.Model):
    source_id = models.IntegerField(db_column='Source_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    order_person = models.ForeignKey(Person, db_column='Order_Person')  # Field name made lowercase.
    date_ordered = models.DateField(db_column='Date_ordered', blank=True, null=True)  # Field name made lowercase.
    date_received = models.DateField(db_column='Date_received', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Source'


class Tissue(models.Model):
    tissue_id = models.IntegerField(db_column='Tissue_ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=16)  # Field name made lowercase.
    sample_name = models.CharField(db_column='Sample_Name', max_length=40)  # Field name made lowercase.
    date_ground = models.DateField(db_column='Date_Ground', blank=True, null=True)  # Field name made lowercase.
    date_plated = models.DateField(db_column='Date_Plated', blank=True, null=True)  # Field name made lowercase.
    date_harvested = models.DateField(db_column='Date_Harvested', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=2000, blank=True)  # Field name made lowercase.
    row = models.ForeignKey('Temprow', db_column='Row_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tissue'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LabCollecting(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    collection_date = models.CharField(max_length=200)
    collection_method = models.CharField(max_length=1000)
    comments = models.CharField(max_length=1000)
    field = models.ForeignKey('LabField')
    obs_selector = models.ForeignKey('LabObsselector')
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'lab_collecting'


class LabDiseaseinfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    common_name = models.CharField(max_length=200)
    abbrev = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'lab_diseaseinfo'


class LabExperiment(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=200)
    start_date = models.CharField(max_length=200)
    purpose = models.CharField(max_length=1000)
    comments = models.CharField(max_length=1000)
    field = models.ForeignKey('LabField')
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'lab_experiment'


class LabField(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    field_name = models.CharField(max_length=200)
    field_num = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    locality = models.ForeignKey('LabLocality')

    class Meta:
        managed = False
        db_table = 'lab_field'


class LabIsolate(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    isolate_id = models.CharField(max_length=200)
    isolate_name = models.CharField(max_length=200)
    plant_organ = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    disease_info = models.ForeignKey(LabDiseaseinfo)
    location = models.ForeignKey('LabLocation')
    passport = models.ForeignKey('LabPassport')

    class Meta:
        managed = False
        db_table = 'lab_isolate'


class LabLocality(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'lab_locality'


class LabLocation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    building_name = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    room = models.CharField(max_length=200)
    shelf = models.CharField(max_length=200)
    column = models.CharField(max_length=200)
    box_name = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    locality = models.ForeignKey(LabLocality)

    class Meta:
        managed = False
        db_table = 'lab_location'


class LabMeasurement(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    time_of_measurement = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    measurement_parameter = models.ForeignKey('LabMeasurementparameter')
    obs_selector = models.ForeignKey('LabObsselector')
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'lab_measurement'


class LabMeasurementparameter(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    parameter = models.CharField(max_length=200)
    parameter_type = models.CharField(max_length=200)
    unit_of_measure = models.CharField(max_length=200)
    protocol = models.CharField(max_length=1000)
    trait_id_buckler = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'lab_measurementparameter'


class LabObsenv(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    environment_id = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    field = models.ForeignKey(LabField)
    obs_selector = models.ForeignKey('LabObsselector')

    class Meta:
        managed = False
        db_table = 'lab_obsenv'


class LabObsplant(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    plant_id = models.CharField(max_length=200)
    plant_num = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    obs_row = models.ForeignKey('LabObsrow')
    obs_selector = models.ForeignKey('LabObsselector')

    class Meta:
        managed = False
        db_table = 'lab_obsplant'


class LabObsrow(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    row_id = models.CharField(max_length=200)
    row_name = models.CharField(max_length=200)
    range_num = models.CharField(max_length=200)
    plot = models.CharField(max_length=200)
    block = models.CharField(max_length=200)
    rep = models.CharField(max_length=200)
    kernel_num = models.CharField(max_length=200)
    planting_date = models.CharField(max_length=200)
    harvest_date = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    field = models.ForeignKey(LabField)
    obs_selector = models.ForeignKey('LabObsselector')
    stock = models.ForeignKey('LabStock')

    class Meta:
        managed = False
        db_table = 'lab_obsrow'


class LabObssample(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sample_id = models.CharField(max_length=200)
    sample_type = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    kernel_num = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    obs_plant = models.ForeignKey(LabObsplant)
    obs_row = models.ForeignKey(LabObsrow)
    obs_selector = models.ForeignKey('LabObsselector')
    source_sample = models.ForeignKey('self')
    stock = models.ForeignKey('LabStock')

    class Meta:
        managed = False
        db_table = 'lab_obssample'


class LabObsselector(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    experiment = models.ForeignKey(LabExperiment)

    class Meta:
        managed = False
        db_table = 'lab_obsselector'


class LabPassport(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    collecting = models.ForeignKey(LabCollecting)
    people = models.ForeignKey('LabPeople')
    taxonomy = models.ForeignKey('LabTaxonomy')

    class Meta:
        managed = False
        db_table = 'lab_passport'


class LabPeople(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'lab_people'


class LabPublication(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    publisher = models.CharField(max_length=200)
    name_of_paper = models.CharField(max_length=200)
    publish_date = models.DateField()
    publication_info = models.CharField(max_length=200)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'lab_publication'


class LabStock(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seed_id = models.CharField(max_length=200)
    seed_name = models.CharField(max_length=200)
    cross_type = models.CharField(max_length=200)
    pedigree = models.CharField(max_length=200)
    stock_status = models.CharField(max_length=200)
    stock_date = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    passport = models.ForeignKey(LabPassport)
    inoculated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lab_stock'


class LabStockpacket(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    weight = models.CharField(max_length=200)
    num_seeds = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    location = models.ForeignKey(LabLocation)
    stock = models.ForeignKey(LabStock)

    class Meta:
        managed = False
        db_table = 'lab_stockpacket'


class LabTaxonomy(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    genus = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    population = models.CharField(max_length=200)
    common_name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    race = models.CharField(max_length=200)
    subtaxa = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'lab_taxonomy'


class LabTreatment(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    treatment_id = models.CharField(max_length=200)
    treatment_type = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    experiment = models.ForeignKey(LabExperiment)

    class Meta:
        managed = False
        db_table = 'lab_treatment'


class LabUserprofile(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    website = models.CharField(max_length=250)
    picture = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    organization = models.CharField(max_length=200)
    notes = models.CharField(max_length=1000)
    job_title = models.CharField(max_length=200)
    user = models.ForeignKey(AuthUser, unique=True)

    class Meta:
        managed = False
        db_table = 'lab_userprofile'


class LegacyLegacyDiseaseinfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    trait = models.CharField(max_length=100)
    disease_name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    disease_info = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'legacy_legacy_diseaseinfo'


class LegacyLegacyExperiment(models.Model):
    experiment_id = models.CharField(primary_key=True, max_length=100)
    location = models.CharField(max_length=100)
    planting_date = models.CharField(max_length=100)
    tissue_collection = models.CharField(max_length=100)
    inoculations = models.CharField(max_length=100)
    inoculation_date1 = models.CharField(max_length=100)
    inoculation_date2 = models.CharField(max_length=100)
    inoculation_date3 = models.CharField(max_length=100)
    pathogen_isolate = models.CharField(max_length=100)
    harvest_date = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    notes = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'legacy_legacy_experiment'


class LegacyLegacyGenotype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    genotype_plate_id = models.CharField(max_length=100)
    genotype_well_id = models.CharField(max_length=100)
    genotype_plate_name = models.CharField(max_length=100)
    well_a01 = models.CharField(db_column='well_A01', max_length=100)  # Field name made lowercase.
    well_01a = models.CharField(db_column='well_01A', max_length=100)  # Field name made lowercase.
    plate_size = models.CharField(max_length=100)
    dna_id = models.CharField(max_length=100)
    sample_id = models.CharField(max_length=100)
    locus_name = models.CharField(max_length=100)
    marker_id = models.CharField(max_length=100)
    marker_name = models.CharField(max_length=100)
    marker_type = models.CharField(max_length=100)
    f_primer_id = models.CharField(max_length=100)
    r_primer_id = models.CharField(max_length=100)
    f2_primer_id = models.CharField(max_length=100)
    r2_primer_id = models.CharField(max_length=100)
    label_color = models.CharField(max_length=100)
    value1 = models.CharField(max_length=100)
    value2 = models.CharField(max_length=100)
    value3 = models.CharField(max_length=100)
    value4 = models.CharField(max_length=100)
    passive_ref = models.CharField(max_length=100)
    quality_value = models.CharField(max_length=100)
    call_type = models.CharField(max_length=100)
    call_name = models.CharField(max_length=100)
    genotype = models.CharField(max_length=100)
    brc_plate_num = models.CharField(max_length=100)
    brc_sample_num = models.CharField(max_length=100)
    genotype_file = models.CharField(max_length=100)
    run_date = models.CharField(max_length=100)
    genotype_person_id = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'legacy_legacy_genotype'


class LegacyLegacyIsolate(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.
    isolate_id = models.CharField(max_length=100)
    isolate_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    other_sname = models.CharField(max_length=100)
    pathotype_race = models.CharField(max_length=100)
    mating_type = models.CharField(max_length=100)
    disease_common_name = models.CharField(max_length=100)
    collection_site = models.CharField(max_length=100)
    collection_date = models.CharField(max_length=100)
    plant_organ = models.CharField(max_length=100)
    collector = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    glycerol_stock_n80c = models.CharField(max_length=100)
    mycelium_4c = models.CharField(max_length=100)
    cite = models.CharField(max_length=100)
    notes = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'legacy_legacy_isolate'


class LegacyLegacyMarkers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_placeholder = models.CharField(max_length=100)
    marker_id = models.CharField(max_length=100)
    locus_name = models.CharField(max_length=100)
    chromosome = models.CharField(max_length=100)
    maize_bin = models.CharField(max_length=100)
    map_physical = models.CharField(max_length=100)
    map_physical_refgen_v1 = models.CharField(max_length=100)
    map_physical_refgen_v2 = models.CharField(max_length=100)
    map_physical_refgen_v3 = models.CharField(max_length=100)
    bac = models.CharField(max_length=100)
    nam_marker = models.CharField(max_length=100)
    map_ibm2n_cm = models.CharField(db_column='map_IBM2n_cM', max_length=100)  # Field name made lowercase.
    polymorphism_type = models.CharField(max_length=100)
    snp_type = models.CharField(max_length=100)
    sequence_f1 = models.CharField(max_length=100)
    sequence_f2 = models.CharField(max_length=100)
    sequence_r1 = models.CharField(max_length=100)
    sequence_r2 = models.CharField(max_length=100)
    primer_name_f1 = models.CharField(max_length=100)
    primer_name_f2 = models.CharField(max_length=100)
    primer_name_r1 = models.CharField(max_length=100)
    primer_name_r2 = models.CharField(max_length=100)
    primer_tail = models.CharField(max_length=100)
    size_range = models.CharField(max_length=100)
    tm_min = models.CharField(db_column='Tm_min', max_length=100)  # Field name made lowercase.
    tm_max = models.CharField(db_column='Tm_max', max_length=100)  # Field name made lowercase.
    chemestry = models.CharField(max_length=100)
    primer_person = models.CharField(max_length=100)
    order_date = models.CharField(max_length=100)
    consense_sequence = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    reference_b73 = models.CharField(db_column='reference_B73', max_length=100)  # Field name made lowercase.
    reference_mo17 = models.CharField(db_column='reference_Mo17', max_length=100)  # Field name made lowercase.
    reference_cml52 = models.CharField(db_column='reference_CML52', max_length=100)  # Field name made lowercase.
    reference_dk888 = models.CharField(db_column='reference_DK888', max_length=100)  # Field name made lowercase.
    reference_s11 = models.CharField(db_column='reference_S11', max_length=100)  # Field name made lowercase.
    reference_xl380 = models.CharField(db_column='reference_XL380', max_length=100)  # Field name made lowercase.
    reference_tx303 = models.CharField(db_column='reference_Tx303', max_length=100)  # Field name made lowercase.
    maizegdblink = models.CharField(db_column='MaizeGDBLink', max_length=100)  # Field name made lowercase.
    maizeseqlink = models.CharField(db_column='MaizeSeqLink', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'legacy_legacy_markers'


class LegacyLegacyPeople(models.Model):
    person_id = models.CharField(primary_key=True, max_length=100)
    person_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    url = models.CharField(db_column='URL', max_length=100)  # Field name made lowercase.
    notes = models.CharField(max_length=100)
    peopleorg_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'legacy_legacy_people'


class LegacyLegacyPhenotype(models.Model):
    phenotype_id = models.CharField(primary_key=True, max_length=100)
    entity_id = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=100)
    experiment_id = models.CharField(max_length=100)
    trait_id = models.CharField(max_length=100)
    phenotype_value = models.CharField(max_length=100)
    phenotype_date = models.CharField(max_length=100)
    plate_id = models.CharField(max_length=100)
    phenotype_person_id = models.CharField(max_length=100)
    scoring_order = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    changed = models.CharField(max_length=100)
    technical_rep = models.CharField(max_length=100)
    biological_rep = models.CharField(max_length=100)
    trait_id_buckler = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'legacy_legacy_phenotype'


class LegacyLegacyPlant(models.Model):
    plant_id = models.CharField(primary_key=True, max_length=100)
    row_id = models.CharField(max_length=100)
    plant_name = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'legacy_legacy_plant'


class LegacyLegacyRow(models.Model):
    row_id = models.CharField(primary_key=True, max_length=100)
    row_name = models.CharField(max_length=100)
    pedigree = models.CharField(max_length=100)
    line_num = models.CharField(max_length=100)
    source_seed_id = models.CharField(max_length=100)
    source_seed_name = models.CharField(max_length=100)
    range_num = models.CharField(max_length=100)
    plot = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    rep_num = models.CharField(max_length=100)
    kernel_num = models.CharField(max_length=100)
    pop = models.CharField(max_length=100)
    delay = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    row_person = models.CharField(max_length=100)
    experiment_id = models.ForeignKey(LegacyLegacyExperiment)

    class Meta:
        managed = False
        db_table = 'legacy_legacy_row'


class LegacyLegacySeed(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seed_id = models.CharField(unique=True, max_length=100)
    plant_id_origin = models.CharField(max_length=100)
    row_id_origin = models.CharField(max_length=100)
    plant_name = models.CharField(max_length=100)
    row_name = models.CharField(max_length=100)
    seed_name = models.CharField(max_length=100)
    cross_type = models.CharField(max_length=100)
    male_parent_id = models.CharField(max_length=100)
    male_parent_name = models.CharField(max_length=100)
    program_origin = models.CharField(max_length=100)
    seed_pedigree = models.CharField(max_length=100)
    line_num = models.CharField(max_length=100)
    seed_person_id = models.CharField(max_length=100)
    disease_info = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    accession = models.CharField(max_length=100)
    lot = models.CharField(max_length=100)
    experiment_id_origin = models.ForeignKey(LegacyLegacyExperiment)

    class Meta:
        managed = False
        db_table = 'legacy_legacy_seed'


class LegacyLegacySeedInventory(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.
    seed_id = models.CharField(max_length=100)
    seed_name = models.CharField(max_length=100)
    inventory_date = models.CharField(max_length=100)
    inventory_person = models.CharField(max_length=100)
    seed_person_id = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    weight_g = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'legacy_legacy_seed_inventory'


class LegacyLegacyTissue(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.
    experiment_id = models.CharField(max_length=100)
    entity_id = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=100)
    pedigree = models.CharField(max_length=100)
    row_name = models.CharField(max_length=100)
    plant = models.CharField(max_length=100)
    tissue_type = models.CharField(max_length=100)
    well = models.CharField(max_length=100)
    tissue_plate_id = models.CharField(max_length=100)
    comments = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'legacy_legacy_tissue'


class LegacyLegacyTraitInfo(models.Model):
    trait_id = models.CharField(primary_key=True, max_length=100)
    trait_grp = models.CharField(max_length=100)
    trait_grp_id = models.CharField(max_length=100)
    trait_name = models.CharField(max_length=100)
    trait_name_id = models.CharField(max_length=100)
    trait_basis = models.CharField(max_length=100)
    trait_id_buckler = models.CharField(max_length=100)
    trait_min = models.CharField(max_length=100)
    trait_max = models.CharField(max_length=100)
    data_type = models.CharField(max_length=100)
    trait_howto = models.CharField(max_length=100)
    trait_when = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'legacy_legacy_trait_info'


class Temppedigree(models.Model):
    pedigree_label = models.CharField(db_column='Pedigree_Label', primary_key=True, max_length=8)  # Field name made lowercase.
    environment = models.CharField(db_column='Environment', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempPedigree'


class Temprow(models.Model):
    row_id = models.CharField(db_column='Row_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    pedigree_label = models.ForeignKey(Temppedigree, db_column='Pedigree_Label')  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=5)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempRow'
