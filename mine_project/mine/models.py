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

class ExperimentFactor(models.Model):
  factor_name = models.CharField(max_length=200, unique=True)
  factor_type = models.CharField(max_length=200)
  description = models.CharField(max_length=1000)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.factor_name

class Experiment(models.Model):
  factor = models.ForeignKey(ExperimentFactor)
  user = models.ForeignKey(User)
  name = models.CharField(max_length=200, unique=True)
  start_date = models.DateField(blank=True)
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

class Locality(models.Model):
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=30)

	def __unicode__(self):
		return self.city

class Location(models.Model):
  locality = models.ForeignKey(Locality)
  building_name = models.CharField(max_length=200)
  room = models.CharField(max_length=200)
  section = models.CharField(max_length=200)
  column = models.CharField(max_length=200)
  shelf = models.CharField(max_length=200)
  box_name = models.CharField(max_length=200)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.building_name

class Citation(models.Model):
  citation_name = models.CharField(max_length=200)
  citation_type = models.CharField(max_length=200)
  citation_date = models.DateField()
  info = models.CharField(max_length=200)
  notes = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.citation_name

class Taxonomy(models.Model):
	genus = models.CharField(max_length=200)
	species = models.CharField(max_length=200)
	subspecies = models.CharField(max_length=200)
	population = models.CharField(max_length=200)
	common_name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.common_name

class Source(models.Model):
	source_name = models.CharField(max_length=200)
	institute = models.CharField(max_length=200)
	contact_name = models.CharField(max_length=200)
	source_phone = models.CharField(max_length=30)
	source_email = models.CharField(max_length=200)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.source_name

class Field(models.Model):
	locality = models.ForeignKey(Locality)
	field_name = models.CharField(max_length=200)
	field_number = models.CharField(max_length=200)
	latitude = models.CharField(max_length=200, blank=True)
	longitude = models.CharField(max_length=200, blank=True)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.field_name

class AccessionCollecting(models.Model):
	field = models.ForeignKey(Field)
	user = models.ForeignKey(User)
	collection_date = models.DateField()
	collection_number = models.CharField(max_length=200, blank=True)
	collection_method = models.CharField(max_length=1000, blank=True)
	comments = models.CharField(max_length=1000, blank=True)

	def __unicode__(self):
		return self.collection_date

class Passport(models.Model):
	accession_collecting = models.ForeignKey(AccessionCollecting)
	source = models.ForeignKey(Source)
	taxonomy = models.ForeignKey(Taxonomy)
	pedigree = models.CharField(max_length=200)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.pedigree

class OrderingInfo(models.Model):
  user = models.ForeignKey(User)
  source = models.ForeignKey(Source)
  what_ordered = models.CharField(max_length=200)
  date_ordered = models.DateField()
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.what_ordered

class DiseaseInfo(models.Model):
	disease_name = models.CharField(max_length=200)
	disease_abbrev = models.CharField(max_length=200)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.disease_name

class Media(models.Model):
  citation = models.ForeignKey(Citation)
  media_name = models.CharField(max_length=200)
  media_purpose = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.media_name

class Inoculations(models.Model):
	disease_info = models.ForeignKey(DiseaseInfo)
	inoculations_date = models.DateField()
	method = models.CharField(max_length=1000)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.inoculations_date

class MatingPlan(models.Model):
	mating_type = models.CharField(max_length=200)
	role = models.CharField(max_length=200)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.mating_type

class Stock(models.Model):
  passport = models.ForeignKey(Passport)
  stock_name = models.CharField(max_length=200)
  cross_type = models.CharField(max_length=200)
  bulk_type = models.CharField(max_length=200)
  stock_status = models.CharField(max_length=200)
  stock_date = models.DateField()
  source_tagname = models.CharField(max_length=200)

  def __unicode__(self):
      return self.source_tagname

class StockPacket(models.Model):
  barcode = models.CharField(max_length=200, unique=True)
  stock = models.ForeignKey(Stock)
  location = models.ForeignKey(Location)
  weight = models.CharField(max_length=30)
  num_seeds = models.CharField(max_length=30)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.weight

class ObsPlant(models.Model):
	field = models.ForeignKey(Field)
	stock = models.ForeignKey(Stock)
	inoculations = models.ForeignKey(Inoculations)
	mating_plan = models.ForeignKey(MatingPlan)
	row_num = models.CharField(max_length=200)
	range_num = models.CharField(max_length=200)
	plant_num = models.CharField(max_length=200)
	plot = models.CharField(max_length=200)
	row = models.CharField(max_length=200)
	tagname = models.CharField(max_length=200)
	planting_date = models.DateField()
	harvest_date = models.DateField()
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.tagname

class ObsTissue(models.Model):
  obs_plant = models.ForeignKey(ObsPlant)
  tissue_name = models.CharField(max_length=200)
  tissue_type = models.CharField(max_length=200)
  date_collected = models.DateField()
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.tissue_name

class ObsCulture(models.Model):
	obs_tissue = models.ForeignKey(ObsTissue)
	media = models.ForeignKey(Media)
	date_plated = models.DateField()

	def __unicode__(self):
		return self.date_plated

class Microbe(models.Model):
  obs_culture = models.ForeignKey(ObsCulture)
  microbe_type = models.CharField(max_length=200)
  glycerol_stock_id = models.CharField(max_length=200)
  dna_isolate_id = models.CharField(max_length=200)
  picture = models.ImageField(upload_to='microbe_images', blank=True)

  def __unicode__(self):
    return self.glycerol_stock_id

class Primers(models.Model):
  citation = models.ForeignKey(Citation)
  ordering_info = models.ForeignKey(OrderingInfo)
  primer_code = models.CharField(max_length=200)
  primer_seq = models.CharField(max_length=1000)
  direction = models.CharField(max_length=200)
  gene_target = models.CharField(max_length=1000)
  purpose = models.CharField(max_length=1000)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.primer_seq

class Sequence(models.Model):
  obs_culture = models.ForeignKey(ObsCulture)
  primer_id1 = models.ForeignKey(Primers, related_name='sequence_primer_id1')
  primer_id2 = models.ForeignKey(Primers, related_name='sequence_primer_id2')
  sequence = models.CharField(max_length=1000)
  genus_species = models.CharField(max_length=1000)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.genus_species

class ObsSelector(models.Model):
  obs_plant = models.ForeignKey(ObsPlant)
  obs_tissue = models.ForeignKey(ObsTissue)
  obs_culture = models.ForeignKey(ObsCulture)
  experiment = models.ForeignKey(Experiment)

  def __unicode__(self):
    return self.experiment.name

class MeasurementParameter(models.Model):
  measurement_type = models.CharField(max_length=200)
  parameter = models.CharField(max_length=200)
  protocol = models.CharField(max_length=1000)
  unit_of_measure = models.CharField(max_length=30)

  def __unicode__(self):
    return self.parameter

class StatisticType(models.Model):
  statistic_type = models.CharField(max_length=200)
  comments = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.statistic_type

class Measurement(models.Model):
  obs_selector = models.ForeignKey(ObsSelector)
  parameter = models.ForeignKey(MeasurementParameter)
  statistic_type = models.ForeignKey(StatisticType)
  time_of_measurement = models.DateTimeField(auto_now_add=True)
  value = models.CharField(max_length=200)

  def __unicode__(self):
    return self.value

class Analysis(models.Model):
  disease_info = models.ForeignKey(DiseaseInfo)
  publication = models.ForeignKey(Publication)
  date = models.DateField()

  def __unicode__(self):
    return self.publication.name_of_paper

class PhenoSet(models.Model):
  measurement = models.ForeignKey(Measurement)
  analysis = models.ForeignKey(Analysis)

  def __unicode__(self):
    return self.analysis.publication.name_of_paper

class ObsSet(models.Model):
  obs_selector = models.ForeignKey(ObsSelector)
  analysis = models.ForeignKey(Analysis)

  def __unicode__(self):
    return self.analysis.publication.name_of_paper
