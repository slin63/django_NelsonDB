from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from metamaize.models import Citation, Culture, Medium, Microbe, MicrobeSequence, Person, Primer, Source, Tissue, Temppedigree, Temprow
from metamaize.forms import TODO
#UserForm, UserProfileForm, ChangePasswordForm, EditUserForm, EditUserProfileForm, NewExperimentForm

def index(request):
	return HttpResponse("Metamaize is alive!!")
