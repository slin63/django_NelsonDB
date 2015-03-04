import csv
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from itertools import chain
from collections import OrderedDict
from metamaize.models import Citation, Culture, Medium, Microbe, MicrobeSequence, Person, Primer, Source, Tissue, Temppedigree, Temprow
from jmaize.models import Plate, Well, DNA, Donor
#UserForm, UserProfileForm, ChangePasswordForm, EditUserForm, EditUserProfileForm, NewExperimentForm

def index(request):
	return HttpResponse("Metamaize is alive!!")

@login_required
def pedigree(request):
	context = RequestContext(request)
	context_dict = {}
	pedigree_model_data = Temppedigree.objects.all()
	context_dict['pedigrees'] = pedigree_model_data
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('metamaize/pedigree.html', context_dict, context)

@login_required
def row(request):
	context = RequestContext(request)
	context_dict = {}
	row_model_data = Temprow.objects.all()
	context_dict['rows'] = row_model_data
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('metamaize/row.html', context_dict, context)

@login_required
def person(request):
	context = RequestContext(request)
	context_dict = {}
	person_model_data = Person.objects.all()
	context_dict['persons'] = person_model_data
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('metamaize/person.html', context_dict, context)

@login_required
def culture(request):
	context = RequestContext(request)
	context_dict = {}
	culture_model_data = Culture.objects.all()
	context_dict['cultures'] = culture_model_data
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('metamaize/culture.html', context_dict, context)

@login_required
def tissue(request):
	context = RequestContext(request)
	context_dict = {}
	tissue_model_data = Tissue.objects.all()
	context_dict['tissues'] = tissue_model_data
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('metamaize/tissue.html', context_dict, context)

@login_required
def medium(request):
	context = RequestContext(request)
	context_dict = {}
	medium_model_data = Medium.objects.all()
	context_dict['mediums'] = medium_model_data
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('metamaize/medium.html', context_dict, context)

@login_required
def fixed_queries(request):
	context = RequestContext(request)
	context_dict = {}

	context_dict['logged_in_user'] = request.user.username
	return render_to_response('metamaize/fixed_queries.html', context_dict, context)

@login_required
def download(request, content):
	response = HttpResponse(content_type='text/csv')

	if content == 'query_01':
		response['Content-Disposition'] = 'attachment; filename="metamaize_query_01.csv"'
		cultures = Culture.objects.all().exclude(microbe_type_observed='NA').exclude(microbe_type_observed='0').exclude(microbe_type_observed='')
		writer = csv.writer(response)
		writer.writerow(['Tissue Type', 'Media', 'Row ID', 'Pedigree', 'Seed Source', 'Microbe Type', 'Culture Name', 'Notes'])
		for row in cultures:
			try:
				writer.writerow([row.tissue.tissue_type, row.medium.medium_id, row.row.row_id, row.pedigree_label.pedigree_label, row.row.source, row.microbe_type_observed, row.culture_name, row.notes])
			except Tissue.DoesNotExist:
				writer.writerow(['', row.medium.medium_id, row.row.row_id, row.pedigree_label.pedigree_label, row.row.source, row.microbe_type_observed, row.culture_name, row.notes])
			except UnicodeError:
				pass
	if content == 'query_02':
		response['Content-Disposition'] = 'attachment; filename="metamaize_query_02.csv"'
		well_check_table = OrderedDict({})
		wells = Well.objects.all()
		for well in wells:
			if well.obs_row_id != 1:
				wells_list = '%s' % (well.well_id)
				wells_inv_list = '%s' % (well.inventory)
				wells_comments_list = '%s' % (well.comments)
				donors = Donor.objects.filter(target_well=well)
				for donor1 in donors:
					wells_list = '%s || %s' % (wells_list, donor1.donor_well.well_id)
					wells_inv_list = '%s || %s' % (wells_inv_list, donor1.donor_well.inventory)
					wells_comments_list = '%s || %s' % (wells_comments_list, donor1.donor_well.comments)
					donor_donor = Donor.objects.filter(target_well=donor1.donor_well)
					for donor2 in donor_donor:
						wells_list = '%s || %s' % (wells_list, donor2.donor_well.well_id)
						wells_inv_list = '%s || %s' % (wells_inv_list, donor2.donor_well.inventory)
						wells_comments_list = '%s || %s' % (wells_comments_list, donor2.donor_well.comments)
						donor_donor_donor = Donor.objects.filter(target_well=donor2.donor_well)
						for donor3 in donor_donor_donor:
							wells_list = '%s || %s' % (wells_list, donor3.donor_well.well_id)
							wells_inv_list = '%s || %s' % (wells_inv_list, donor3.donor_well.inventory)
							wells_comments_list = '%s || %s' % (wells_comments_list, donor3.donor_well.comments)
							donor_donor_donor_donor = Donor.objects.filter(target_well=donor3.donor_well)
							for donor4 in donor_donor_donor_donor:
								wells_list = '%s || %s' % (wells_list, donor4.donor_well.well_id)
								wells_inv_list = '%s || %s' % (wells_inv_list, donor4.donor_well.inventory)
								wells_comments_list = '%s || %s' % (wells_comments_list, donor4.donor_well.comments)
								donor_donor_donor_donor_donor = Donor.objects.filter(target_well=donor4.donor_well)
								for donor5 in donor_donor_donor_donor_donor:
									wells_list = '%s || %s' % (wells_list, donor5.donor_well.well_id)
									wells_inv_list = '%s || %s' % (wells_inv_list, donor5.donor_well.inventory)
									wells_comments_list = '%s || %s' % (wells_comments_list, donor5.donor_well.comments)
				if (well.obs_row, well.tissue_type, well.plant) in well_check_table:
					wells_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][4], wells_list)
					wells_inv_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][5], wells_inv_list)
					wells_comments_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][6], wells_comments_list)
					well_check_table[(well.obs_row, well.tissue_type, well.plant)] = (well.obs_row.stock.pedigree, well.obs_row, well.tissue_type, well.plant, wells_list, wells_inv_list, wells_comments_list)
				else:
					well_check_table[(well.obs_row, well.tissue_type, well.plant)] = (well.obs_row.stock.pedigree, well.obs_row, well.tissue_type, well.plant, wells_list, wells_inv_list, wells_comments_list)
		writer = csv.writer(response)
		writer.writerow(['Pedigree', 'Row ID', 'Tissue Type', 'Plant', 'Well IDs', 'Inventories', 'Comments'])
		for value in well_check_table.itervalues():
			writer.writerow(value)
	if content == 'query_03':
		response['Content-Disposition'] = 'attachment; filename="metamaize_query_03.csv"'
		well_check_table = OrderedDict({})
		wells = Well.objects.filter(obs_row__obs_selector__experiment__name__contains='12')
		for well in wells:
			if well.obs_row_id != 1:
				if well.obs_row.stock.pedigree == 'B73' or well.obs_row.stock.pedigree == 'B97' or well.obs_row.stock.pedigree == 'CML103' or well.obs_row.stock.pedigree == 'CML322' or well.obs_row.stock.pedigree == 'Mo17':
					wells_list = '%s' % (well.well_id)
					wells_inv_list = '%s' % (well.inventory)
					wells_comments_list = '%s' % (well.comments)
					donors = Donor.objects.filter(target_well=well)
					for donor1 in donors:
						wells_list = '%s || %s' % (wells_list, donor1.donor_well.well_id)
						wells_inv_list = '%s || %s' % (wells_inv_list, donor1.donor_well.inventory)
						wells_comments_list = '%s || %s' % (wells_comments_list, donor1.donor_well.comments)
						donor_donor = Donor.objects.filter(target_well=donor1.donor_well)
						for donor2 in donor_donor:
							wells_list = '%s || %s' % (wells_list, donor2.donor_well.well_id)
							wells_inv_list = '%s || %s' % (wells_inv_list, donor2.donor_well.inventory)
							wells_comments_list = '%s || %s' % (wells_comments_list, donor2.donor_well.comments)
							donor_donor_donor = Donor.objects.filter(target_well=donor2.donor_well)
							for donor3 in donor_donor_donor:
								wells_list = '%s || %s' % (wells_list, donor3.donor_well.well_id)
								wells_inv_list = '%s || %s' % (wells_inv_list, donor3.donor_well.inventory)
								wells_comments_list = '%s || %s' % (wells_comments_list, donor3.donor_well.comments)
								donor_donor_donor_donor = Donor.objects.filter(target_well=donor3.donor_well)
								for donor4 in donor_donor_donor_donor:
									wells_list = '%s || %s' % (wells_list, donor4.donor_well.well_id)
									wells_inv_list = '%s || %s' % (wells_inv_list, donor4.donor_well.inventory)
									wells_comments_list = '%s || %s' % (wells_comments_list, donor4.donor_well.comments)
									donor_donor_donor_donor_donor = Donor.objects.filter(target_well=donor4.donor_well)
									for donor5 in donor_donor_donor_donor_donor:
										wells_list = '%s || %s' % (wells_list, donor5.donor_well.well_id)
										wells_inv_list = '%s || %s' % (wells_inv_list, donor5.donor_well.inventory)
										wells_comments_list = '%s || %s' % (wells_comments_list, donor5.donor_well.comments)
					if (well.obs_row, well.tissue_type, well.plant) in well_check_table:
						wells_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][4], wells_list)
						wells_inv_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][5], wells_inv_list)
						wells_comments_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][6], wells_comments_list)
						well_check_table[(well.obs_row, well.tissue_type, well.plant)] = (well.obs_row.stock.pedigree, well.obs_row, well.tissue_type, well.plant, wells_list, wells_inv_list, wells_comments_list)
					else:
						well_check_table[(well.obs_row, well.tissue_type, well.plant)] = (well.obs_row.stock.pedigree, well.obs_row, well.tissue_type, well.plant, wells_list, wells_inv_list, wells_comments_list)
		writer = csv.writer(response)
		writer.writerow(['Pedigree', 'Row ID', 'Tissue Type', 'Plant', 'Well IDs', 'Inventories', 'Comments'])
		for value in well_check_table.itervalues():
			writer.writerow(value)
	if content == 'query_04':
		response['Content-Disposition'] = 'attachment; filename="metamaize_query_04.csv"'
		well_check_table = OrderedDict({})
		wells = Well.objects.filter(obs_row__obs_selector__experiment__name__contains='13')
		for well in wells:
			if well.obs_row_id != 1:
				if well.obs_row.stock.pedigree == 'B73' or well.obs_row.stock.pedigree == 'B97' or well.obs_row.stock.pedigree == 'CML103' or well.obs_row.stock.pedigree == 'CML322' or well.obs_row.stock.pedigree == 'Mo17':
					wells_list = '%s' % (well.well_id)
					wells_inv_list = '%s' % (well.inventory)
					wells_comments_list = '%s' % (well.comments)
					donors = Donor.objects.filter(target_well=well)
					for donor1 in donors:
						wells_list = '%s || %s' % (wells_list, donor1.donor_well.well_id)
						wells_inv_list = '%s || %s' % (wells_inv_list, donor1.donor_well.inventory)
						wells_comments_list = '%s || %s' % (wells_comments_list, donor1.donor_well.comments)
						donor_donor = Donor.objects.filter(target_well=donor1.donor_well)
						for donor2 in donor_donor:
							wells_list = '%s || %s' % (wells_list, donor2.donor_well.well_id)
							wells_inv_list = '%s || %s' % (wells_inv_list, donor2.donor_well.inventory)
							wells_comments_list = '%s || %s' % (wells_comments_list, donor2.donor_well.comments)
							donor_donor_donor = Donor.objects.filter(target_well=donor2.donor_well)
							for donor3 in donor_donor_donor:
								wells_list = '%s || %s' % (wells_list, donor3.donor_well.well_id)
								wells_inv_list = '%s || %s' % (wells_inv_list, donor3.donor_well.inventory)
								wells_comments_list = '%s || %s' % (wells_comments_list, donor3.donor_well.comments)
								donor_donor_donor_donor = Donor.objects.filter(target_well=donor3.donor_well)
								for donor4 in donor_donor_donor_donor:
									wells_list = '%s || %s' % (wells_list, donor4.donor_well.well_id)
									wells_inv_list = '%s || %s' % (wells_inv_list, donor4.donor_well.inventory)
									wells_comments_list = '%s || %s' % (wells_comments_list, donor4.donor_well.comments)
									donor_donor_donor_donor_donor = Donor.objects.filter(target_well=donor4.donor_well)
									for donor5 in donor_donor_donor_donor_donor:
										wells_list = '%s || %s' % (wells_list, donor5.donor_well.well_id)
										wells_inv_list = '%s || %s' % (wells_inv_list, donor5.donor_well.inventory)
										wells_comments_list = '%s || %s' % (wells_comments_list, donor5.donor_well.comments)
					if (well.obs_row, well.tissue_type, well.plant) in well_check_table:
						wells_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][4], wells_list)
						wells_inv_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][5], wells_inv_list)
						wells_comments_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][6], wells_comments_list)
						well_check_table[(well.obs_row, well.tissue_type, well.plant)] = (well.obs_row.stock.pedigree, well.obs_row, well.tissue_type, well.plant, wells_list, wells_inv_list, wells_comments_list)
					else:
						well_check_table[(well.obs_row, well.tissue_type, well.plant)] = (well.obs_row.stock.pedigree, well.obs_row, well.tissue_type, well.plant, wells_list, wells_inv_list, wells_comments_list)
		writer = csv.writer(response)
		writer.writerow(['Pedigree', 'Row ID', 'Tissue Type', 'Plant', 'Well IDs', 'Inventories', 'Comments'])
		for value in well_check_table.itervalues():
			writer.writerow(value)
	if content == 'query_05':
		response['Content-Disposition'] = 'attachment; filename="metamaize_query_05.csv"'
		well_check_table = OrderedDict({})
		wells = Well.objects.filter(obs_row__obs_selector__experiment__name__contains='12')
		for well in wells:
			if well.obs_row_id != 1:
				if well.obs_row.stock.pedigree == 'CML52' or well.obs_row.stock.pedigree == 'M162W' or well.obs_row.stock.pedigree == 'NC358' or well.obs_row.stock.pedigree == 'Oh7b' or well.obs_row.stock.pedigree == 'Tzi8':
					wells_list = '%s' % (well.well_id)
					wells_inv_list = '%s' % (well.inventory)
					wells_comments_list = '%s' % (well.comments)
					donors = Donor.objects.filter(target_well=well)
					for donor1 in donors:
						wells_list = '%s || %s' % (wells_list, donor1.donor_well.well_id)
						wells_inv_list = '%s || %s' % (wells_inv_list, donor1.donor_well.inventory)
						wells_comments_list = '%s || %s' % (wells_comments_list, donor1.donor_well.comments)
						donor_donor = Donor.objects.filter(target_well=donor1.donor_well)
						for donor2 in donor_donor:
							wells_list = '%s || %s' % (wells_list, donor2.donor_well.well_id)
							wells_inv_list = '%s || %s' % (wells_inv_list, donor2.donor_well.inventory)
							wells_comments_list = '%s || %s' % (wells_comments_list, donor2.donor_well.comments)
							donor_donor_donor = Donor.objects.filter(target_well=donor2.donor_well)
							for donor3 in donor_donor_donor:
								wells_list = '%s || %s' % (wells_list, donor3.donor_well.well_id)
								wells_inv_list = '%s || %s' % (wells_inv_list, donor3.donor_well.inventory)
								wells_comments_list = '%s || %s' % (wells_comments_list, donor3.donor_well.comments)
								donor_donor_donor_donor = Donor.objects.filter(target_well=donor3.donor_well)
								for donor4 in donor_donor_donor_donor:
									wells_list = '%s || %s' % (wells_list, donor4.donor_well.well_id)
									wells_inv_list = '%s || %s' % (wells_inv_list, donor4.donor_well.inventory)
									wells_comments_list = '%s || %s' % (wells_comments_list, donor4.donor_well.comments)
									donor_donor_donor_donor_donor = Donor.objects.filter(target_well=donor4.donor_well)
									for donor5 in donor_donor_donor_donor_donor:
										wells_list = '%s || %s' % (wells_list, donor5.donor_well.well_id)
										wells_inv_list = '%s || %s' % (wells_inv_list, donor5.donor_well.inventory)
										wells_comments_list = '%s || %s' % (wells_comments_list, donor5.donor_well.comments)
					if (well.obs_row, well.tissue_type, well.plant) in well_check_table:
						wells_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][4], wells_list)
						wells_inv_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][5], wells_inv_list)
						wells_comments_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][6], wells_comments_list)
						well_check_table[(well.obs_row, well.tissue_type, well.plant)] = (well.obs_row.stock.pedigree, well.obs_row, well.tissue_type, well.plant, wells_list, wells_inv_list, wells_comments_list)
					else:
						well_check_table[(well.obs_row, well.tissue_type, well.plant)] = (well.obs_row.stock.pedigree, well.obs_row, well.tissue_type, well.plant, wells_list, wells_inv_list, wells_comments_list)
		writer = csv.writer(response)
		writer.writerow(['Pedigree', 'Row ID', 'Tissue Type', 'Plant', 'Well IDs', 'Inventories', 'Comments'])
		for value in well_check_table.itervalues():
			writer.writerow(value)
	if content == 'query_06':
		response['Content-Disposition'] = 'attachment; filename="metamaize_query_06.csv"'
		well_check_table = OrderedDict({})
		wells = Well.objects.filter(obs_row__obs_selector__experiment__name__contains='13')
		for well in wells:
			if well.obs_row_id != 1:
				if well.obs_row.stock.pedigree == 'CML52' or well.obs_row.stock.pedigree == 'M162W' or well.obs_row.stock.pedigree == 'NC358' or well.obs_row.stock.pedigree == 'Oh7b' or well.obs_row.stock.pedigree == 'Tzi8':
					wells_list = '%s' % (well.well_id)
					wells_inv_list = '%s' % (well.inventory)
					wells_comments_list = '%s' % (well.comments)
					donors = Donor.objects.filter(target_well=well)
					for donor1 in donors:
						wells_list = '%s || %s' % (wells_list, donor1.donor_well.well_id)
						wells_inv_list = '%s || %s' % (wells_inv_list, donor1.donor_well.inventory)
						wells_comments_list = '%s || %s' % (wells_comments_list, donor1.donor_well.comments)
						donor_donor = Donor.objects.filter(target_well=donor1.donor_well)
						for donor2 in donor_donor:
							wells_list = '%s || %s' % (wells_list, donor2.donor_well.well_id)
							wells_inv_list = '%s || %s' % (wells_inv_list, donor2.donor_well.inventory)
							wells_comments_list = '%s || %s' % (wells_comments_list, donor2.donor_well.comments)
							donor_donor_donor = Donor.objects.filter(target_well=donor2.donor_well)
							for donor3 in donor_donor_donor:
								wells_list = '%s || %s' % (wells_list, donor3.donor_well.well_id)
								wells_inv_list = '%s || %s' % (wells_inv_list, donor3.donor_well.inventory)
								wells_comments_list = '%s || %s' % (wells_comments_list, donor3.donor_well.comments)
								donor_donor_donor_donor = Donor.objects.filter(target_well=donor3.donor_well)
								for donor4 in donor_donor_donor_donor:
									wells_list = '%s || %s' % (wells_list, donor4.donor_well.well_id)
									wells_inv_list = '%s || %s' % (wells_inv_list, donor4.donor_well.inventory)
									wells_comments_list = '%s || %s' % (wells_comments_list, donor4.donor_well.comments)
									donor_donor_donor_donor_donor = Donor.objects.filter(target_well=donor4.donor_well)
									for donor5 in donor_donor_donor_donor_donor:
										wells_list = '%s || %s' % (wells_list, donor5.donor_well.well_id)
										wells_inv_list = '%s || %s' % (wells_inv_list, donor5.donor_well.inventory)
										wells_comments_list = '%s || %s' % (wells_comments_list, donor5.donor_well.comments)
					if (well.obs_row, well.tissue_type, well.plant) in well_check_table:
						wells_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][4], wells_list)
						wells_inv_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][5], wells_inv_list)
						wells_comments_list = '%s || %s' % (well_check_table[(well.obs_row, well.tissue_type, well.plant)][6], wells_comments_list)
						well_check_table[(well.obs_row, well.tissue_type, well.plant)] = (well.obs_row.stock.pedigree, well.obs_row, well.tissue_type, well.plant, wells_list, wells_inv_list, wells_comments_list)
					else:
						well_check_table[(well.obs_row, well.tissue_type, well.plant)] = (well.obs_row.stock.pedigree, well.obs_row, well.tissue_type, well.plant, wells_list, wells_inv_list, wells_comments_list)
		writer = csv.writer(response)
		writer.writerow(['Pedigree', 'Row ID', 'Tissue Type', 'Plant', 'Well IDs', 'Inventories', 'Comments'])
		for value in well_check_table.itervalues():
			writer.writerow(value)
	if content == 'pedigree_all':
		response['Content-Disposition'] = 'attachment; filename="metamaize_pedigrees.csv"'
		pedigree_model_data = Temppedigree.objects.all()
		writer = csv.writer(response)
		writer.writerow(['Pedigree Label', 'Environment'])
		for row in pedigree_model_data:
			writer.writerow([row.pedigree_label, row.environment])
	if content == 'row_all':
		response['Content-Disposition'] = 'attachment; filename="metamaize_rows.csv"'
		row_model_data = Temprow.objects.all()
		writer = csv.writer(response)
		writer.writerow(['Row ID', 'Pedigree Label', 'Source', 'Location'])
		for row in row_model_data:
			writer.writerow([row.row_id, row.pedigree_label.pedigree_label, row.source, row.location])
	if content == 'culture_all':
		response['Content-Disposition'] = 'attachment; filename="metamaize_cultures.csv"'
		culture_model_data = Culture.objects.all()
		writer = csv.writer(response)
		writer.writerow(['Culture ID', 'Row ID', 'Pedigree Label', 'Person ID', 'Medium ID', 'Tissue ID', 'Culture Name', 'Microbe Type Observed', 'Plating Cycle', 'Dilution', 'Image Location', 'Notes'])
		for row in culture_model_data:
			writer.writerow([row.culture_id, row.row.row_id, row.pedigree_label.pedigree_label, row.person.person_id, row.medium.medium_id, row.tissue.tissue_id, row.culture_name, row.microbe_type_observed, row.plating_cycle, row.dilution, row.image_location, row.notes])
	if content == 'tissue_all':
		response['Content-Disposition'] = 'attachment; filename="metamaize_tissues.csv"'
		tissue_model_data = Tissue.objects.all()
		writer = csv.writer(response)
		writer.writerow(['Tissue ID', 'Type', 'Sample Name', 'Date Ground', 'Date Plated', 'Date Harvested', 'Notes', 'Row ID'])
		for row in tissue_model_data:
			writer.writerow([row.tissue_id, row.tissue_type, row.sample_name, row.date_ground, row.date_plated, row.date_harvested, row.notes, row.row.row_id])
	if content == 'medium_all':
		response['Content-Disposition'] = 'attachment; filename="metamaize_medium.csv"'
		medium_model_data = Medium.objects.all()
		writer = csv.writer(response)
		writer.writerow(['Medium ID', 'Notes', 'Citation URL'])
		for row in medium_model_data:
			writer.writerow([row.medium_id, row.notes, row.citation.url])

	return response
