from django.db import models
from django.contrib.auth.models import User
from lab.models import ObsRow
from legacy.models import Legacy_Tissue


class Plate(models.Model):
	plate_contents_choices = (
        ('Tissue','Tissue'),
        ('DNA','DNA'),
        ('RNA','RNA'),
        ('PCR Products','PCR Products'),
    )
	plate_type_choices = (
        ('96 Well Costar Rack','96 Well Costar Rack'),
    )
	plate_status_choices = (
        ('Success','Success'),
        ('Empty','Empty'),
        ('Lost','Lost'),
    )
	plate_id = models.CharField(max_length=200)
	plate_name = models.CharField(max_length=200)
	plate_contents = models.CharField(max_length=20, choices=plate_contents_choices)
	plate_rep = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	container = models.CharField(max_length=200)
	plate_type = models.CharField(max_length=40, choices=plate_type_choices)
	status = models.CharField(max_length=20, choices=plate_status_choices)
	date_made = models.DateField(blank=True, null=True)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.location_id

class Well(models.Model):
	well_plant_choices = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
    )
	well_inventory_choices = (
        ('+','+'),
        ('-','-'),
        ('E','E'),
        ('X','X'),
        ('No Tube','No Tube'),
    )
	plate = models.ForeignKey(Plate)
	tissue = models.ForeignKey(Legacy_Tissue, related_name="tissue_well")
	obs_row = models.ForeignKey(ObsRow)
	well_id = models.CharField(max_length=200)
	well = models.CharField(max_length=200)
	plant = models.CharField(max_length=1, choices=well_plant_choices)
	inventory = models.CharField(max_length=20, choices=well_inventory_choices)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.well_id

class Donor(models.Model):
	target_well = models.ForeignKey(Well, related_name="target_well")
	donor_well = models.ForeignKey(Well, related_name="donor_well")

	def __unicode__(self):
		return self.donor_well

class DNA(models.Model):
	dna_well = models.ForeignKey(Well)
	dna_tube_id = models.CharField(max_length=200)
	jbc_dna_id = models.CharField(max_length=200)
	dna_tube_type = models.CharField(max_length=200)
	extraction_method = models.CharField(max_length=200)
	date_made = models.DateField(blank=True, null=True)
	comments = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.dna_tube_id
