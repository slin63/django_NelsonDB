from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from mine.models import Category, Page, UserProfile, Experiment, Passport, Stock, StockPacket, Taxonomy, Source, AccessionCollecting, Field, Locality, Location
from legacy.models import Seed
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect

def encode_url(str):
  return str.replace(' ', '_')

def decode_url(str):
  return str.replace('_', ' ')

def get_experiment_list(max_results=0, starts_with=''):
  exp_list = []
  if starts_with:
    exp_list = Experiment.objects.filter(name__like='%{}%'.format(starts_with))
  else:
    exp_list = Experiment.objects.all()
  if max_results > 0:
    if len(exp_list) > max_results:
      exp_list = exp_list[:max_results]
  for exp in exp_list:
    exp.url = encode_url(exp.name)
  return exp_list

def legacy_seed_inv(request):
  context = RequestContext(request)
  context_dict = {}
  exp_list = get_experiment_list()
  context_dict['exp_list'] = exp_list
  context_dict['logged_in_user'] = request.user.username
  return render_to_response('legacy/seed_inventory.html', context_dict, context)
