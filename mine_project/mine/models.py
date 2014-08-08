from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	phone = models.CharField(max_length=32)
	organization = models.CharField(max_length=128)
	notes = models.CharField(max_length=1024)
	job_title = models.CharField(max_length=128)

	def __unicode__(self):
		return self.user.username

class Experiment(models.Model):
	name = models.CharField(max_length=32, unique=True)
	experiment_date = models.CharField(max_length=32)
	user = models.ForeignKey(User)
	experiment_purpose = models.CharField(max_length=256)
	experiment_comments = models.CharField(max_length=256)

	def __unicode__(self):
		return self.name

class ExperimentFactor(models.Model):
	experiment_factor_name = models.CharField(max_length=32, unique=True)
	experiment_factor_type = models.CharField(max_length=32)
	experiment_factor_desc = models.CharField(max_length=256)
	experiment_factor_comments = models.CharField(max_length=256)

	def __unicode__(self):
		return self.experiment_factor_name

class Locality(models.Model):
	locality_name = models.CharField(max_length=32)
	city = models.CharField(max_length=32)
	state = models.CharField(max_length=32)
	country = models.CharField(max_length=32, blank=True)
	zipcode = models.CharField(max_length=32, blank=True)

	def __unicode__(self):
		return self.locality_name

class Location(models.Model):
  locality = models.ForeignKey(Locality)
  building_name = models.CharField(max_length=32)
  room = models.CharField(max_length=32)
  section = models.CharField(max_length=32)
  column = models.CharField(max_length=32)
  shelf = models.CharField(max_length=32)
  box_name = models.CharField(max_length=32)

  def __unicode__(self):
    return self.building_name

class Taxonomy(models.Model):
	genus = models.CharField(max_length=64)
	species = models.CharField(max_length=64)
	subspecies = models.CharField(max_length=64)
	population = models.CharField(max_length=32)
	common_name = models.CharField(max_length=64)

	def __unicode__(self):
		return self.common_name

class Source(models.Model):
	source_name = models.CharField(max_length=32)
	institute = models.CharField(max_length=32)
	contact_name = models.CharField(max_length=64)
	source_phone = models.CharField(max_length=32)
	source_email = models.CharField(max_length=64)
	source_comments = models.CharField(max_length=256)

	def __unicode__(self):
		return self.source_name

class Field(models.Model):
	locality = models.ForeignKey(Locality)
	field_name = models.CharField(max_length=32)
	field_number = models.CharField(max_length=32)
	latitude = models.CharField(max_length=32, blank=True)
	longitude = models.CharField(max_length=32, blank=True)
	altitude = models.CharField(max_length=32, blank=True)
	field_comments = models.CharField(max_length=256)

	def __unicode__(self):
		return self.field_name

class AccessionCollecting(models.Model):
	field = models.ForeignKey(Field)
	user = models.ForeignKey(User)
	collection_date = models.CharField(max_length=32, blank=True)
	collection_number = models.CharField(max_length=32, blank=True)
	collection_method = models.CharField(max_length=256, blank=True)
	collection_comments = models.CharField(max_length=256, blank=True)

	def __unicode__(self):
		return self.collection_date

class Passport(models.Model):
	accession_collecting = models.ForeignKey(AccessionCollecting)
	source = models.ForeignKey(Source)
	taxonomy = models.ForeignKey(Taxonomy)
	pedigree = models.CharField(max_length=32)
	passport_comments = models.CharField(max_length=256)

	def __unicode__(self):
		return self.pedigree

class Isolate(models.Model):
	isolate_name = models.CharField(max_length=32)
	scientific_name = models.CharField(max_length=64)
	isolate_comments = models.CharField(max_length=256)
	passport = models.ForeignKey(Passport)

	def __unicode__(self):
		return self.isolate_name

class DiseaseInfo(models.Model):
	disease_name = models.CharField(max_length=32)
	disease_abbrev = models.CharField(max_length=32)
	disease_comments = models.CharField(max_length=256)

	def __unicode__(self):
		return self.disease_name

class Media(models.Model):
	media_name = models.CharField(max_length=32)
	media_desc = models.CharField(max_length=256)
	media_URL = models.CharField(max_length=256)
	user = models.ForeignKey(User)
	media_date = models.DateField()

	def __unicode__(self):
		return self.media_name

class Inoculations(models.Model):
	disease_info = models.ForeignKey(DiseaseInfo)
	inoculations_date = models.DateField()
	inoculations_method = models.CharField(max_length=256)
	inoculations_comments = models.CharField(max_length=256)

	def __unicode__(self):
		return self.inoculations_date

class MatingPlan(models.Model):
	mating_type = models.CharField(max_length=32)
	role = models.CharField(max_length=32)
	mating_comments = models.CharField(max_length=256)

	def __unicode__(self):
		return self.mating_type

class Stock(models.Model):
  passport = models.ForeignKey(Passport)
  stock_name = models.CharField(max_length=32)
  cross_type = models.CharField(max_length=32)
  bulk_type = models.CharField(max_length=32)
  stock_status = models.CharField(max_length=32)
  stock_date = models.CharField(max_length=32)
  source_tagname = models.CharField(max_length=32)
  ear_num = models.CharField(max_length=32)

  def __unicode__(self):
      return self.source_tagname

class StockPacket(models.Model):
  timestamp = models.CharField(max_length=32, unique=True)
  stock = models.ForeignKey(Stock)
  location = models.ForeignKey(Location)
  weight = models.CharField(max_length=32)
  number_of_seeds = models.CharField(max_length=32)
  stock_packet_comments = models.CharField(max_length=256)

  def __unicode__(self):
    return self.weight

class ObsPlant(models.Model):
	field = models.ForeignKey(Field)
	stock = models.ForeignKey(Stock)
	inoculations = models.ForeignKey(Inoculations)
	mating_plan = models.ForeignKey(MatingPlan)
	row_num = models.CharField(max_length=32)
	range_num = models.CharField(max_length=32)
	plant_num = models.CharField(max_length=32)
	plot = models.CharField(max_length=32)
	row = models.CharField(max_length=32)
	tagname = models.CharField(max_length=32)
	planting_date = models.DateField()
	harvest_date = models.DateField()
	plant_comments = models.CharField(max_length=256)

	def __unicode__(self):
		return self.tagname

class ObsTissue(models.Model):
	obs_plant = models.ForeignKey(ObsPlant)
	tissue_name = models.CharField(max_length=32)
	tissue_type = models.CharField(max_length=32)
	tissue_comments = models.CharField(max_length=256)

	def __unicode__(self):
		return self.tissue_name

class ObsCulture(models.Model):
	obs_tissue = models.ForeignKey(ObsTissue)
	petri_parent = models.ForeignKey('self')
	user = models.ForeignKey(User)
	media = models.ForeignKey(Media)
	location = models.ForeignKey(Location)
	isolate = models.ForeignKey(Isolate)
	petri_name = models.CharField(max_length=32)
	petri_type = models.CharField(max_length=32)
	dilution = models.CharField(max_length=32)
	plating_cycle = models.CharField(max_length=32)
	date_ground = models.DateField()
	date_plated = models.DateField()
	petri_comments = models.CharField(max_length=256)

	def __unicode__(self):
		return self.petri_name

class ExperimentUnit(models.Model):
	experiment_factor = models.ForeignKey(ExperimentFactor)
	obs_culture = models.ForeignKey(ObsCulture)
	experiment = models.ForeignKey(Experiment)

	def __unicode__(self):
		return self.experiment_id

class MicrobeMeasurements(models.Model):
	experiment_unit = models.ForeignKey(ExperimentUnit)
	measurement_type = models.CharField(max_length=32)
	time_of_measurement = models.DateTimeField()
	value = models.CharField(max_length=32)
	description = models.CharField(max_length=256)
	picture = models.ImageField(upload_to='microbe_images', blank=True)
	microbe_comments = models.CharField(max_length=256)

	def __unicode__(self):
		return self.description
