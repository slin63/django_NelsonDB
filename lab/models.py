from django.db import models
from django.contrib.auth.models import User

"""User Model

class User:
	username
	first_name
	last_name
	email
	password
	is_staff
	is_active
	is_superuser
	last_login
	date_joined
"""

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.CharField(max_length=250)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	phone = models.CharField(max_length=30)
	organization = models.CharField(max_length=200)
	notes = models.CharField(max_length=1000)
	job_title = models.CharField(max_length=200)

	def __unicode__(self):
		return self.user.username

class Locality(models.Model):
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  country = models.CharField(max_length=200)
  zipcode = models.CharField(max_length=30)

  def __unicode__(self):
    return self.city

class Field(models.Model):
  locality = models.ForeignKey(Locality)
  field_name = models.CharField(max_length=200)
  field_num = models.CharField(max_length=200)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.field_name

class Experiment(models.Model):
  user = models.ForeignKey(User)
  field = models.ForeignKey(Field)
  name = models.CharField(max_length=200, unique=True)
  start_date = models.CharField(max_length=200)
  purpose = models.CharField(max_length=1000)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.name

class Publication(models.Model):
  user = models.ForeignKey(User)
  publisher = models.CharField(max_length=200)
  name_of_paper = models.CharField(max_length=200)
  publish_date = models.DateField()
  publication_info = models.CharField(max_length=200)

  def __unicode__(self):
    return self.name_of_paper

class Taxonomy(models.Model):
	genus = models.CharField(max_length=200)
	species = models.CharField(max_length=200)
	population = models.CharField(max_length=200)
	common_name = models.CharField(max_length=200)
	alias = models.CharField(max_length=200)
	race = models.CharField(max_length=200)
	subtaxa = models.CharField(max_length=200)

	def __unicode__(self):
		return self.genus

class People(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	organization = models.CharField(max_length=200)
	phone = models.CharField(max_length=30)
	email = models.CharField(max_length=200)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.organization

class ObsSelector(models.Model):
  experiment = models.ForeignKey(Experiment)

  def __unicode__(self):
    return self.experiment.name

class Collecting(models.Model):
  obs_selector = models.ForeignKey(ObsSelector)
  user = models.ForeignKey(User)
  field = models.ForeignKey(Field)
  collection_date = models.CharField(max_length=200)
  collection_method = models.CharField(max_length=1000, blank=True)
  comments = models.CharField(max_length=1000, blank=True)

  def __unicode__(self):
    return self.collection_date

class Passport(models.Model):
	collecting = models.ForeignKey(Collecting)
	people = models.ForeignKey(People)
	taxonomy = models.ForeignKey(Taxonomy)

	def __unicode__(self):
		return self.taxonomy.genus

class Stock(models.Model):
  passport = models.ForeignKey(Passport)
  seed_id = models.CharField(max_length=200)
  seed_name = models.CharField(max_length=200)
  cross_type = models.CharField(max_length=200)
  pedigree = models.CharField(max_length=200)
  stock_status = models.CharField(max_length=200)
  stock_date = models.CharField(max_length=200)
  inoculated = models.BooleanField(default=False)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
      return self.seed_id

class DiseaseInfo(models.Model):
  common_name = models.CharField(max_length=200)
  abbrev = models.CharField(max_length=200)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
      return self.common_name

class ObsRow(models.Model):
  obs_selector = models.ForeignKey(ObsSelector)
  field = models.ForeignKey(Field)
  stock = models.ForeignKey(Stock)
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

  def __unicode__(self):
    return self.row_id

class ObsPlant(models.Model):
  obs_selector = models.ForeignKey(ObsSelector)
  obs_row = models.ForeignKey(ObsRow)
  stock = models.ForeignKey(Stock, default=1)
  plant_id = models.CharField(max_length=200)
  plant_num = models.CharField(max_length=200)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.plant_id

class ObsSample(models.Model):
	obs_selector = models.ForeignKey(ObsSelector)
	obs_row = models.ForeignKey(ObsRow)
	obs_plant = models.ForeignKey(ObsPlant)
	stock = models.ForeignKey(Stock)
	source_sample = models.ForeignKey("self")
	sample_id = models.CharField(max_length=200)
	sample_type = models.CharField(max_length=200)
	weight = models.CharField(max_length=200)
	kernel_num = models.CharField(max_length=200)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.sample_id

class ObsEnv(models.Model):
	obs_selector = models.ForeignKey(ObsSelector)
	field = models.ForeignKey(Field)
	environment_id = models.CharField(max_length=200)
	longitude = models.CharField(max_length=200)
	latitude = models.CharField(max_length=200)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.environment_id

class Location(models.Model):
  locality = models.ForeignKey(Locality)
  building_name = models.CharField(max_length=200)
  location_name = models.CharField(max_length=200)
  room = models.CharField(max_length=200)
  shelf = models.CharField(max_length=200)
  column = models.CharField(max_length=200)
  box_name = models.CharField(max_length=200)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.building_name

class Isolate(models.Model):
  passport = models.ForeignKey(Passport)
  location = models.ForeignKey(Location)
  disease_info = models.ForeignKey(DiseaseInfo)
  isolate_id = models.CharField(max_length=200)
  isolate_name = models.CharField(max_length=200)
  plant_organ = models.CharField(max_length=200)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
      return self.isolate_id

class StockPacket(models.Model):
  stock = models.ForeignKey(Stock)
  location = models.ForeignKey(Location)
  weight = models.CharField(max_length=200)
  num_seeds = models.CharField(max_length=200)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.stock.seed_id

class MeasurementParameter(models.Model):
	parameter = models.CharField(max_length=200)
	parameter_type = models.CharField(max_length=200)
	unit_of_measure = models.CharField(max_length=200, default='No Units')
	protocol = models.CharField(max_length=1000)
	trait_id_buckler = models.CharField(max_length=200)

	def __unicode__(self):
		return self.parameter

class Measurement(models.Model):
	obs_selector = models.ForeignKey(ObsSelector)
	user = models.ForeignKey(User)
	measurement_parameter = models.ForeignKey(MeasurementParameter)
	time_of_measurement = models.CharField(max_length=200)
	value = models.CharField(max_length=200)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.value

class Treatment(models.Model):
	experiment = models.ForeignKey(Experiment)
	treatment_id = models.CharField(max_length=200)
	treatment_type = models.CharField(max_length=200)
	date = models.CharField(max_length=200)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.treatment_id

class UploadQueue(models.Model):
	experiment = models.ForeignKey(Experiment)
	user = models.ForeignKey(User)
	file_name = models.FileField(upload_to='upload_queue')
	upload_type = models.CharField(max_length=200)
	date = models.DateField(auto_now_add=True)
	completed = models.BooleanField(default=False)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.file_name

class Citation(models.Model):
	citation_type = models.CharField(max_length=200)
	url = models.CharField(max_length=300)
	pubmed_id = models.CharField(max_length=300)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.url

class Medium(models.Model):
	citation = models.ForeignKey(Citation)
	media_type = models.CharField(max_length=200)
	media_description = models.CharField(max_length=200)
	media_preparation = models.CharField(max_length=200)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.media_description

class ObsOther(models.Model):
	user = models.ForeignKey(User)
	medium = models.ForeignKey(Medium)
	location = models.ForeignKey(Location)
	source_stock = models.ForeignKey(Stock)
	source_isolate = models.ForeignKey(Isolate)
	source_row = models.ForeignKey(ObsRow)
	source_plant = models.ForeignKey(ObsPlant)
	source_well = models.ForeignKey("self", related_name='well_entity')
	source_microbe = models.ForeignKey("self", related_name='microbe_entity')
	source_culture = models.ForeignKey("self", related_name='culture_entity')
	source_tissue = models.ForeignKey("self", related_name='tissue_entity')
	source_sample = models.ForeignKey("self", related_name='sample_entity')
	source_dna = models.ForeignKey("self", related_name='dna_entity')
	source_plate = models.ForeignKey("self", related_name='plate_entity')
	entity_type = models.CharField(max_length=200)
	dna_id = models.CharField(max_length=200)
	dna_extraction_method = models.CharField(max_length=200)
	dna_date = models.DateField()
	dna_tube_id = models.CharField(max_length=200)
	dna_tube_type = models.CharField(max_length=200)
	dna_comments = models.CharField(max_length=1000)
	tissue_id = models.CharField(max_length=200)
	tissue_type = models.CharField(max_length=200)
	tissue_name = models.CharField(max_length=200)
	tissue_date_ground = models.DateField()
	tissue_comments = models.CharField(max_length=1000)
	plate_id = models.CharField(max_length=200)
	plate_name = models.CharField(max_length=200)
	plate_date_plated = models.DateField()
	plate_contents = models.CharField(max_length=200)
	plate_rep = models.CharField(max_length=200)
	plate_type = models.CharField(max_length=200)
	plate_status = models.CharField(max_length=200)
	plate_comments = models.CharField(max_length=1000)
	sample_id = models.CharField(max_length=200)
	sample_type = models.CharField(max_length=200)
	sample_weight = models.CharField(max_length=200)
	sample_kernel_num = models.CharField(max_length=200)
	sample_comments = models.CharField(max_length=1000)
	well_id = models.CharField(max_length=200)
	well = models.CharField(max_length=200)
	well_inventory = models.CharField(max_length=200)
	well_tube_label = models.CharField(max_length=200)
	well_comments = models.CharField(max_length=1000)
	culture_id = models.CharField(max_length=200)
	culture_name = models.CharField(max_length=200)
	culture_microbe_type = models.CharField(max_length=200)
	culture_plating_cycle = models.CharField(max_length=200)
	culture_dilution = models.CharField(max_length=200)
	culture_image = models.CharField(max_length=200)
	culture_comments = models.CharField(max_length=1000)
	microbe_id = models.CharField(max_length=200)
	microbe_type = models.CharField(max_length=200)
	microbe_comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.entity_type
