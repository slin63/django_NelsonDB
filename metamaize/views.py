from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from metamaize.models import Citation, Culture, Medium, Microbe, MicrobeSequence, Person, Primer, Source, Tissue, Temppedigree, Temprow
#UserForm, UserProfileForm, ChangePasswordForm, EditUserForm, EditUserProfileForm, NewExperimentForm

def index(request):
	return HttpResponse("Metamaize is alive!!")

@login_required	
def pedigree(request):
	context = RequestContext(request)
	context_dict = {}
	pedigree_model_data = Temppedigree.objects.all()
	context_dict['pedigrees'] = pedigree_model_data

	return render_to_response('metamaize/pedigree.html', context_dict, context)

def row(request):
	context = RequestContext(request)
	context_dict = {}
	row_model_data = Temprow.objects.all()
	context_dict['rows'] = row_model_data

	return render_to_response('metamaize/row.html', context_dict, context)

def person(request):
	context = RequestContext(request)
	context_dict = {}
	person_model_data = Person.objects.all()
	context_dict['persons'] = person_model_data
	
	return render_to_response('metamaize/person.html', context_dict, context)

def culture(request):
	context = RequestContext(request)
	context_dict = {}
	culture_model_data = Culture.objects.all()
	context_dict['cultures'] = culture_model_data
	
	return render_to_response('metamaize/culture.html', context_dict, context)

def tissue(request):
	context = RequestContext(request)
	context_dict = {}
	tissue_model_data = Tissue.objects.all()
	context_dict['tissues'] = tissue_model_data
	
	return render_to_response('metamaize/tissue.html', context_dict, context)

def medium(request):
	context = RequestContext(request)
	context_dict = {}
	medium_model_data = Medium.objects.all()
	context_dict['mediums'] = medium_model_data
	
	return render_to_response('metamaize/medium.html', context_dict, context)

