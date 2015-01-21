import csv
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
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
	cultures = Culture.objects.all()
	context_dict['cultures'] = cultures
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('metamaize/fixed_queries.html', context_dict, context)

@login_required
def download_queries(request):
	response = HttpResponse(content_type='test/csv')
	response['Content-Disposition'] = 'attachment; filename="metamaize_queries.csv"'
	cultures = Culture.objects.all()
	writer = csv.writer(response)
	writer.writerow(['Tissue Type', 'Row ID', 'Pedigree', 'Seed Source', 'Microbe Type', 'Culture Name', 'Notes'])
	for row in cultures:
		try:
			writer.writerow([row.tissue.tissue_type, row.row.row_id, row.pedigree_label.pedigree_label, row.row.source, row.microbe_type_observed, row.culture_name, row.notes])
		except Tissue.DoesNotExist:
			writer.writerow(['', row.row.row_id, row.pedigree_label.pedigree_label, row.row.source, row.microbe_type_observed, row.culture_name, row.notes])
	return response
