from __future__ import unicode_literals

from django.db import models


# Keeping `managed = False` to disallow Django from creating, modifying or deleting tables
class Citation(models.Model):
    #type is enum field in DB
    citation_type_choices = (
        ('literature','literature'),
        ('website','website'),
        ('personal','personal'),
        ('other','other'),
    )
    citation_id = models.IntegerField(db_column='Citation_ID', primary_key=True)  # Field name made lowercase.
    citation_type = models.CharField(db_column='Type', max_length=10, choices=citation_type_choices)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=50, blank=True)  # Field name made lowercase.
    pubmed_id = models.CharField(db_column='Pubmed_ID', max_length=10, blank=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=2000, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Citation'


class Culture(models.Model):
    #type is enum field in DB
    microbe_type_observed_choices = (
        ('Fungi','Fungi'),
        ('Bacteria','Bacteria'),
        ('Both','Fungi and Bacteria'),
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('Na','NA'),
    )
    culture_id = models.IntegerField(db_column='Culture_ID', primary_key=True)  # Field name made lowercase.
    row = models.ForeignKey('Temprow', db_column='Row_ID')  # Field name made lowercase.
    pedigree_label = models.ForeignKey('Temppedigree', db_column='Pedigree_Label')  # Field name made lowercase.
    person = models.ForeignKey('Person', db_column='Person_ID')  # Field name made lowercase.
    medium = models.ForeignKey('Medium', db_column='Medium_ID')  # Field name made lowercase.
    tissue = models.ForeignKey('Tissue', db_column='Tissue_ID')  # Field name made lowercase.
    culture_name = models.CharField(db_column='Culture_Name', max_length=30)  # Field name made lowercase.
    microbe_type_observed = models.CharField(db_column='Microbe_Type_Observed', max_length=8, blank=True, choice=microbe_type_observed_choices)  # Field name made lowercase.
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
    #type is enum field in DB
    microbe_type_choices = (
        ('Fungi','Fungi'),
        ('Bacteria','Bacteria'),
        ('Archaea','Archaea'),
        ('Unknown','Unknown'),
    )
    microbe_id = models.IntegerField(db_column='Microbe_ID', primary_key=True)  # Field name made lowercase.
    source_culture = models.ForeignKey(Culture, db_column='Source_Culture', blank=True, null=True)  # Field name made lowercase.
    source_tissue = models.ForeignKey('Tissue', db_column='Source_Tissue', blank=True, null=True)  # Field name made lowercase.
    microbe_type = models.CharField(db_column='Type', max_length=8, blank=True, choices=microbe_type_choices)  # Field name made lowercase.
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
    #direction and barcode are enum fields in DB
    direction_choices = (
        ('F','Forward'),
        ('R','Reverse'),
    )
    barcode_choices = (
        ('Y','Yes'),
        ('N','No'),
    )
    primer_id = models.IntegerField(db_column='Primer_ID', primary_key=True)  # Field name made lowercase.
    primer_number = models.CharField(db_column='Primer_Number', max_length=10)  # Field name made lowercase.
    sequence = models.CharField(db_column='Sequence', max_length=255)  # Field name made lowercase.
    direction = models.CharField(db_column='Direction', max_length=1, choices=direction_choices)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=1, choices=barcode_choices)  # Field name made lowercase.
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
    #type is enum field in DB
    tissue_type_choices = (
        ('planted_kernel','Planted Kernel'),
        ('leaf','Leaf'),
        ('root','Root'),
        ('stem','Stem'),
        ('prop_root','Adventitious or prop roots'),
        ('immature_ear','Immature ears'),
        ('harvested_kernel','Harvested Kernel'),
        ('other','Other'),
    )

    tissue_id = models.IntegerField(db_column='Tissue_ID', primary_key=True)  # Field name made lowercase.
    tissue_type = models.CharField(db_column='Type', max_length=16, choices=tissue_type_choices)  # Field name made lowercase.
    sample_name = models.CharField(db_column='Sample_Name', max_length=40)  # Field name made lowercase.
    date_ground = models.DateField(db_column='Date_Ground', blank=True, null=True)  # Field name made lowercase.
    date_plated = models.DateField(db_column='Date_Plated', blank=True, null=True)  # Field name made lowercase.
    date_harvested = models.DateField(db_column='Date_Harvested', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=2000, blank=True)  # Field name made lowercase.
    row = models.ForeignKey('Temprow', db_column='Row_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tissue'

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

