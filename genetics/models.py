from django.db import models
from lab.models import Experiment, MeasurementParameter

class MapFeature(models.Model):
    chromosome = models.CharField(max_length=200)
    genetic_bin = models.CharField(max_length=200)
    genetic_map = models.CharField(max_length=200)
    genetic_position = models.CharField(max_length=200)
    locus_type = models.CharField(max_length=200)
    locus_name = models.CharField(max_length=200)
    physical_position = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)

    def __unicode__(self):
		return self.physical_position

class MapFeatureAnnotation(models.Model):
    map_feature = models.ForeignKey(MapFeature)
    annotation_type = models.CharField(max_length=200)
    annotation_value = models.CharField(max_length=200)

    def __unicode__(self):
		return self.annotation_value

class Marker(models.Model):
    map_feature = models.ForeignKey(MapFeature)
    marker_name = models.CharField(max_length=200)
    ref_seq = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    length = models.CharField(max_length=200)

    def __unicode__(self):
		return self.marker_name

class GWASResults(models.Model):
    parameter = models.ForeignKey(MeasurementParameter)
    marker = models.ForeignKey(Marker)
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
	gwas_result = models.ForeignKey(GWASResults)

	def __unicode__(self):
		return self.gwas_result
