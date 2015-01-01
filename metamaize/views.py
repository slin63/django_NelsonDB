from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from metamaize.models import Citation, Culture, Medium, Microbe, MicrobeSequence, Person, Primer, Source, Tissue, Temppedigree, Temprow
#UserForm, UserProfileForm, ChangePasswordForm, EditUserForm, EditUserProfileForm, NewExperimentForm

def index(request):
	return HttpResponse("Metamaize is alive!!")
	
def pedigree(request):
	context = RequestContext(request)
	context_dict = {}
	pedigree_model_data = Temppedigree.objects.all()
	context_dict['pedigrees'] = pedigree_model_data
	
	return render_to_response('metamaize/pedigree.html', context_dict, context)


