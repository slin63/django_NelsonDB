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
    website = models.CharField(max_length=250, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    phone = models.CharField(max_length=30, blank=True)
    organization = models.CharField(max_length=200, blank=True)
    notes = models.CharField(max_length=1000, blank=True)
    job_title = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.user.username


class Locality(models.Model):
    city = models.CharField(max_length=200, blank=True)
    county = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.city


class Field(models.Model):
    locality = models.ForeignKey(Locality)
    field_name = models.CharField(max_length=200, unique=True)
    field_num = models.CharField(max_length=200, blank=True)
    dimensions = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)
    planting_year = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        return self.field_name + ' - ' + self.planting_year


class Experiment(models.Model):
    user = models.ForeignKey(User)
    field = models.ForeignKey(Field)
    name = models.CharField(max_length=200, unique=True)
    start_date = models.CharField(max_length=200, blank=True)
    purpose = models.CharField(max_length=1000, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.name


def subdirectory_upload(instance, filename):
    # file will be uploaded to subdirectory/filename
    # https://docs.djangoproject.com/en/1.9/ref/models/fields/#django.db.models.FileField.upload_to
    return 'files/{0}/{1}'.format(instance.file_subdirectory, filename)


class FileDump(models.Model):
    user = models.ForeignKey(User)
    experiment = models.ForeignKey(Experiment)
    file_name = models.CharField(max_length=250, blank=True)
    file = models.FileField(upload_to=subdirectory_upload, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    comments = models.CharField(max_length=1000, blank=True)
    file_subdirectory = models.CharField(
        max_length=1000, blank=True, default='files'
    )

    def __unicode__(self):
        return self.file_name


class Publication(models.Model):
    user = models.ForeignKey(User)
    publisher = models.CharField(max_length=200, blank=True)
    name_of_paper = models.CharField(max_length=200, unique=True)
    publish_date = models.DateField()
    publication_info = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.name_of_paper


class Taxonomy(models.Model):
    binomial = models.CharField(max_length=200, blank=True)
    population = models.CharField(max_length=200, blank=True)
    common_name = models.CharField(max_length=200, blank=True)
    alias = models.CharField(max_length=200, blank=True)
    race = models.CharField(max_length=200, blank=True)
    subtaxa = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.binomial


class People(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    organization = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.organization


class Citation(models.Model):
    citation_type = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, unique=True)
    url = models.CharField(max_length=300, blank=True)
    pubmed_id = models.CharField(max_length=300, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.title


class Medium(models.Model):
    citation = models.ForeignKey(Citation)
    media_name = models.CharField(max_length=200, unique=True)
    media_type = models.CharField(max_length=200, blank=True)
    media_description = models.CharField(max_length=200, blank=True)
    media_preparation = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.media_name


class ObsPlot(models.Model):
    plot_id = models.CharField(max_length=200, unique=True)
    plot_name = models.CharField(max_length=200, blank=True)
    row_num = models.CharField(max_length=200, blank=True)
    range_num = models.CharField(max_length=200, blank=True)
    plot = models.CharField(max_length=200, blank=True)
    block = models.CharField(max_length=200, blank=True)
    rep = models.CharField(max_length=200, blank=True)
    polli_type = models.CharField(max_length=30, blank=True)
    kernel_num = models.CharField(max_length=200, blank=True)
    shell_single = models.BooleanField(default=False)
    shell_multi = models.BooleanField(default=False)
    shell_bulk = models.BooleanField(default=False)
    planting_date = models.CharField(max_length=200, blank=True)
    harvest_date = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=3000, blank=True)
    gen = models.CharField(max_length=30, blank=True)

    def get_shell_type(self, pedigen=False):
        if pedigen:
            if self.shell_single: t = 'SINGLE-EAR'
            elif self.shell_multi: t = 'MULTI-ROW'
            elif self.shell_bulk: t = 'BULK'
        else:
            if self.shell_single: t = 'Single'
            elif self.shell_multi: t = 'Multi'
            elif self.shell_bulk: t = 'Bulk'
            else: t = 'None'
        return t

    def __unicode__(self):
        return self.plot_id


class ObsPlant(models.Model):
    plant_id = models.CharField(max_length=200, unique=True)
    plant_num = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=3000, blank=True)

    def __unicode__(self):
        return self.plant_id


class ObsSample(models.Model):
    sample_id = models.CharField(max_length=200, unique=True)
    sample_type = models.CharField(max_length=200, blank=True)
    sample_name = models.CharField(max_length=200, blank=True)
    weight = models.CharField(max_length=200, blank=True)
    volume = models.CharField(max_length=200, blank=True)
    density = models.CharField(max_length=200, blank=True)
    kernel_num = models.CharField(max_length=200, blank=True)
    photo = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=3000, blank=True)

    def __unicode__(self):
        return self.sample_id


class Separation(models.Model):
    obs_sample = models.ForeignKey(ObsSample)
    separation_type = models.CharField(max_length=200, blank=True)
    apparatus = models.CharField(max_length=200, blank=True)
    SG = models.CharField(max_length=200, blank=True)
    light_weight = models.CharField(max_length=200, blank=True)
    intermediate_weight = models.CharField(max_length=200, blank=True)
    heavy_weight = models.CharField(max_length=200, blank=True)
    light_percent = models.CharField(max_length=200, blank=True)
    intermediate_percent = models.CharField(max_length=200, blank=True)
    heavy_percent = models.CharField(max_length=200, blank=True)
    operating_factor = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.separation_type


class ObsExtract(models.Model):
    extract_id = models.CharField(max_length=200, unique=True)
    weight = models.CharField(max_length=200, blank=True)
    rep = models.CharField(max_length=200, blank=True)
    grind_method = models.CharField(max_length=200, blank=True)
    solvent = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=3000, blank=True)

    def __unicode__(self):
        return self.extract_id


class ObsEnv(models.Model):
    environment_id = models.CharField(max_length=200, unique=True)
    longitude = models.CharField(max_length=200, blank=True)
    latitude = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=3000, blank=True)

    def __unicode__(self):
        return self.environment_id


class ObsDNA(models.Model):
    dna_id = models.CharField(max_length=200, unique=True)
    extraction_method = models.CharField(max_length=500, blank=True)
    date = models.CharField(max_length=200, blank=True)
    tube_id = models.CharField(max_length=200, blank=True)
    tube_type = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=3000, blank=True)

    def __unicode__(self):
        return self.dna_id


class ObsTissue(models.Model):
    tissue_id = models.CharField(max_length=200, unique=True)
    tissue_type = models.CharField(max_length=200, blank=True)
    tissue_name = models.CharField(max_length=200, blank=True)
    date_ground = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=3000, blank=True)

    def __unicode__(self):
        return self.tissue_id


class ObsPlate(models.Model):
    plate_id = models.CharField(max_length=200, unique=True)
    plate_name = models.CharField(max_length=200, blank=True)
    date = models.CharField(max_length=200, blank=True)
    contents = models.CharField(max_length=200, blank=True)
    rep = models.CharField(max_length=200, blank=True)
    plate_type = models.CharField(max_length=200, blank=True)
    plate_status = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=3000, blank=True)

    def __unicode__(self):
        return self.plate_id


class ObsWell(models.Model):
    well_id = models.CharField(max_length=200, unique=True)
    well = models.CharField(max_length=200, blank=True)
    well_inventory = models.CharField(max_length=200, blank=True)
    tube_label = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=3000, blank=True)

    def __unicode__(self):
        return self.well_id


class ObsCulture(models.Model):
    medium = models.ForeignKey(Medium)
    culture_id = models.CharField(max_length=200, unique=True)
    culture_name = models.CharField(max_length=200, blank=True)
    microbe_type = models.CharField(max_length=200, blank=True)
    plating_cycle = models.CharField(max_length=200, blank=True)
    dilution = models.CharField(max_length=200, blank=True)
    image_filename = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=3000, blank=True)
    num_colonies = models.CharField(max_length=200, blank=True)
    num_microbes = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.culture_id


class ObsMicrobe(models.Model):
    microbe_id = models.CharField(max_length=200, unique=True)
    microbe_type = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=3000, blank=True)

    def __unicode__(self):
        return self.microbe_id


class Location(models.Model):
    locality = models.ForeignKey(Locality)
    building_name = models.CharField(max_length=200, blank=True)
    box_name = models.CharField(max_length=200, blank=False)
    room = models.CharField(max_length=200, blank=True)
    shelf = models.CharField(max_length=200, blank=True)
    column = models.CharField(max_length=200, blank=True)
    location_name = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.box_name


class Collecting(models.Model):
    user = models.ForeignKey(User)
    collection_date = models.CharField(max_length=200, blank=True)
    collection_method = models.CharField(max_length=1000, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.collection_date


class Passport(models.Model):
    collecting = models.ForeignKey(Collecting)
    people = models.ForeignKey(People)
    taxonomy = models.ForeignKey(Taxonomy)

    def __unicode__(self):
        return self.taxonomy.binomial


class Stock(models.Model):
    passport = models.ForeignKey(Passport)
    seed_id = models.CharField(max_length=200, unique=True)
    seed_name = models.CharField(max_length=200, blank=True)
    cross_type = models.CharField(max_length=200, blank=True)
    pedigree = models.CharField(max_length=200, blank=True)
    stock_status = models.CharField(max_length=200, blank=True)
    stock_date = models.CharField(max_length=200, blank=True)
    inoculated = models.BooleanField(default=False)
    comments = models.CharField(max_length=1000, blank=True)
    gen = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.seed_id


class MaizeSample(models.Model):
    maize_id = models.CharField(max_length=200, unique=True)
    county = models.CharField(max_length=200, blank=True)
    sub_location = models.CharField(max_length=200, blank=True)
    village = models.CharField(max_length=200, blank=True)
    weight = models.CharField(max_length=200, blank=True)
    harvest_date = models.CharField(max_length=200, blank=True)
    storage_months = models.CharField(max_length=200, blank=True)
    storage_conditions = models.CharField(max_length=200, blank=True)
    maize_variety = models.CharField(max_length=200, blank=True)
    seed_source = models.CharField(max_length=200, blank=True)
    moisture_content = models.CharField(max_length=200, blank=True)
    source_type = models.CharField(max_length=200, blank=True)
    appearance = models.CharField(max_length=200, blank=True)
    gps_latitude = models.CharField(max_length=200, blank=True)
    gps_longitude = models.CharField(max_length=200, blank=True)
    gps_altitude = models.CharField(max_length=200, blank=True)
    gps_accuracy = models.CharField(max_length=200, blank=True)
    photo = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.maize_id


class DiseaseInfo(models.Model):
    common_name = models.CharField(max_length=200, unique=True)
    abbrev = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.common_name


class IsolateStock(models.Model):
    passport = models.ForeignKey(Passport)
    locality = models.ForeignKey(Locality)
    disease_info = models.ForeignKey(DiseaseInfo)
    isolatestock_id = models.CharField(max_length=200, unique=True)
    isolatestock_name = models.CharField(max_length=200, blank=True)
    plant_organ = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.isolatestock_id


class Isolate(models.Model):
    isolate_id = models.CharField(max_length=200)
    isolatestock = models.ForeignKey(IsolateStock)
    location = models.ForeignKey(Location)
    locality = models.ForeignKey(Locality)
    stock_date = models.CharField(max_length=200, blank=True)
    extract_color = models.CharField(max_length=200, blank=True)
    organism = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.isolate_id


class StockPacket(models.Model):
    stock = models.ForeignKey(Stock)
    location = models.ForeignKey(Location)
    seed_id = models.CharField(max_length=200, blank=True)
    pedigree = models.CharField(max_length=200, blank=True)
    weight = models.CharField(max_length=200, blank=True)
    num_seeds = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)
    gen = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.stock.seed_id


class Treatment(models.Model):
    experiment = models.ForeignKey(Experiment)
    treatment_id = models.CharField(max_length=200, unique=True)
    treatment_type = models.CharField(max_length=200, blank=True)
    date = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.treatment_id


class UploadQueue(models.Model):
    experiment = models.ForeignKey(Experiment)
    user = models.ForeignKey(User)
    file_name = models.FileField(upload_to='upload_queue')
    upload_type = models.CharField(max_length=200, blank=True)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.file_name


class ObsTracker(models.Model):
    obs_entity_type = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location, blank=True, null=True)
    experiment = models.ForeignKey(Experiment, blank=True, null=True)
    field = models.ForeignKey(Field, blank=True, null=True)
    isolatestock = models.ForeignKey(IsolateStock, blank=True, null=True)
    stock = models.ForeignKey(Stock, blank=True, null=True)
    maize_sample = models.ForeignKey(MaizeSample, blank=True, null=True)
    isolate = models.ForeignKey(Isolate, blank=True, null=True)
    obs_culture = models.ForeignKey(ObsCulture, blank=True, null=True)
    obs_dna = models.ForeignKey(ObsDNA, blank=True, null=True)
    obs_microbe = models.ForeignKey(ObsMicrobe, blank=True, null=True)
    obs_plant = models.ForeignKey(ObsPlant, blank=True, null=True)
    obs_plate = models.ForeignKey(ObsPlate, blank=True, null=True)
    obs_plot = models.ForeignKey(ObsPlot, blank=True, null=True)
    obs_sample = models.ForeignKey(ObsSample, blank=True, null=True)
    obs_tissue = models.ForeignKey(ObsTissue, blank=True, null=True)
    obs_well = models.ForeignKey(ObsWell, blank=True, null=True)
    obs_env = models.ForeignKey(ObsEnv, blank=True, null=True)
    obs_extract = models.ForeignKey(ObsExtract, blank=True, null=True)

    def __unicode__(self):
        return self.obs_entity_type


class ObsTrackerSource(models.Model):
    target_obs = models.ForeignKey(ObsTracker, related_name='target_obs_tracker')
    source_obs = models.ForeignKey(ObsTracker, related_name='source_obs_tracker')
    relationship = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.target_obs


class Primer(models.Model):
    primer_id = models.CharField(max_length=200, unique=True)
    primer_name = models.CharField(max_length=200, blank=True)
    primer_tail = models.CharField(max_length=200, blank=True)
    size_range = models.CharField(max_length=200, blank=True)
    temp_min = models.CharField(max_length=200, blank=True)
    temp_max = models.CharField(max_length=200, blank=True)
    order_date = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    # Context sequence string
    # Sequence string

    def __unicode__(self):
        return self.primer_id


class MapFeature(models.Model):
    map_feature_id = models.CharField(max_length=200, unique=True)
    chromosome = models.CharField(max_length=200, blank=True)
    genetic_bin = models.CharField(max_length=200, blank=True)
    physical_map = models.CharField(max_length=200, blank=True)
    genetic_position = models.CharField(max_length=200, blank=True)
    physical_position = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.physical_position


class MapFeatureAnnotation(models.Model):
    map_feature = models.ForeignKey(MapFeature)
    annotation_type = models.CharField(max_length=200, blank=True)
    annotation_value = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.annotation_value


class MapFeatureInterval(models.Model):
    map_feature_start = models.ForeignKey(MapFeature, related_name='map_feature_interval_start')
    map_feature_end = models.ForeignKey(MapFeature, related_name='map_feature_interval_end')
    interval_type = models.CharField(max_length=200, blank=True)
    interval_name = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.interval_name


class Marker(models.Model):
    map_feature_interval = models.ForeignKey(MapFeatureInterval)
    marker_map_feature = models.ForeignKey(MapFeature)
    primer_f = models.ForeignKey(Primer, related_name='f_primer', blank=True, null=True)
    primer_r = models.ForeignKey(Primer, related_name='r_primer', blank=True, null=True)
    marker_id = models.CharField(max_length=200, unique=True)
    marker_name = models.CharField(max_length=200, blank=True)
    length = models.CharField(max_length=200, blank=True)
    bac = models.CharField(max_length=200, blank=True)
    nam_marker = models.CharField(max_length=200, blank=True)
    poly_type = models.CharField(max_length=200, blank=True)
    ref_seq = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)
    strand = models.CharField(max_length=200, blank=True)
    allele = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.marker_id


class MeasurementParameter(models.Model):
    parameter = models.CharField(max_length=200, unique=True)
    parameter_type = models.CharField(max_length=200, blank=True)
    unit_of_measure = models.CharField(max_length=200, blank=True)
    protocol = models.CharField(max_length=1000, blank=True)
    description = models.CharField(max_length=200, blank=True)
    trait_id_buckler = models.CharField(max_length=200, blank=True)
    marker = models.ForeignKey(Marker, blank=True, null=True)

    def __unicode__(self):
        return self.parameter


class QTL(models.Model):
    map_feature_interval = models.ForeignKey(MapFeatureInterval)
    parameter = models.ForeignKey(MeasurementParameter)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.map_feature_interval.interval_name


class MapFeatureExpression(models.Model):
    map_feature_interval = models.ForeignKey(MapFeatureInterval)
    parameter = models.ForeignKey(MeasurementParameter)
    value = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.map_feature_interval.interval_name


class GenotypeResults(models.Model):
    marker = models.ForeignKey(Marker)
    parameter = models.ForeignKey(MeasurementParameter)
    sequence = models.TextField(blank=True)
    comments = models.CharField(max_length=1000, blank=True)
    fasta_file = models.FileField(upload_to='fasta_files', blank=True)
    chromatogram_file = models.FileField(upload_to='chromatogram_files', blank=True)

    def __unicode__(self):
        return self.sequence


class GWASResults(models.Model):
    parameter = models.ForeignKey(MeasurementParameter)
    p_value = models.CharField(max_length=200)
    strand = models.CharField(max_length=200)
    relationship_to_hit = models.CharField(max_length=200)
    interpro_domain = models.CharField(max_length=200)
    distance_from_gene = models.CharField(max_length=200)
    f_value = models.CharField(max_length=200)
    perm_p_value = models.CharField(max_length=200)
    r2 = models.CharField(max_length=200)
    alleles = models.CharField(max_length=200)
    bpp = models.CharField(max_length=200)
    effect = models.CharField(max_length=200)
    cM = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.p_value


class GWASExperimentSet(models.Model):
    experiment = models.ForeignKey(Experiment)
    gwas_results = models.ForeignKey(GWASResults)

    def __unicode__(self):
        return self.gwas_results


class Measurement(models.Model):
    obs_tracker = models.ForeignKey(ObsTracker)
    user = models.ForeignKey(User)
    measurement_parameter = models.ForeignKey(MeasurementParameter)
    time_of_measurement = models.CharField(max_length=200, blank=True)
    value = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=1000, blank=True)
    experiment = models.ForeignKey(Experiment)

    class Meta:
        unique_together = ('value', 'time_of_measurement', 'measurement_parameter', 'obs_tracker')

    def __unicode__(self):
        return self.value
