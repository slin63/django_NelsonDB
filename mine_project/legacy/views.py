from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from mine.models import Category, Page, UserProfile, Experiment, Passport, Stock, StockPacket, Taxonomy, Source, AccessionCollecting, Field, Locality, Location
from legacy.models import Legacy_Seed, Legacy_Row, Legacy_Experiment, Legacy_Seed_Inventory, Legacy_People
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect
from collections import defaultdict

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

def suggest_legacy_pedigree(request):
  context = RequestContext(request)
  context_dict = {}
  pedigree_list = []
  starts_with = ''
  if request.method == 'GET':
    starts_with = request.GET['suggestion']
    radio = request.GET['radio']
  else:
    starts_with = request.POST['suggestion']
    radio = request.POST['radio']
  if starts_with:
    if radio == 'variable':
      if request.session.get('selected_legacy_experiment', None):
        experiment = request.session.get('selected_legacy_experiment')
        pedigree_list = Legacy_Seed.objects.filter(seed_pedigree__like='%{}%'.format(starts_with), experiment_id_origin = experiment).values('seed_pedigree').distinct()[:1000]
      else:
        pedigree_list = Legacy_Seed.objects.filter(seed_pedigree__like='%{}%'.format(starts_with)).values('seed_pedigree').distinct()[:1000]
    if radio == 'exact':
      if request.session.get('selected_legacy_experiment', None):
        experiment = request.session.get('selected_legacy_experiment')
        pedigree_list = Legacy_Seed.objects.filter(seed_pedigree = starts_with, experiment_id_origin = experiment).values('seed_pedigree').distinct()[:1000]
      else:
        pedigree_list = Legacy_Seed.objects.filter(seed_pedigree = starts_with).values('seed_pedigree').distinct()[:1000]
  else:
    if request.session.get('selected_legacy_experiment', None):
      experiment = request.session.get('selected_legacy_experiment')
      pedigree_list = Legacy_Seed.objects.filter(experiment_id_origin = experiment).values('seed_pedigree').distinct()[:1000]
    else:
      pedigree_list = Legacy_Seed.objects.all().values('seed_pedigree').distinct()[:1000]
  context_dict['pedigree_list'] = pedigree_list
  return render_to_response('legacy/legacy_pedigree_list.html', context_dict, context)

def suggest_legacy_experiment(request):
  context = RequestContext(request)
  context_dict = {}
  experiment_list = []
  starts_with = ''
  if request.method == 'GET':
    starts_with = request.GET['suggestion']
    radio = request.GET['radio']
  else:
    starts_with = request.POST['suggestion']
    radio = request.POST['radio']
  if starts_with:
    if radio == 'variable':
      if request.session.get('selected_legacy_pedigree', None):
        pedigree = request.session.get('selected_legacy_pedigree')
        experiment_list = Legacy_Experiment.objects.filter(experiment_id__like='%{}%'.format(starts_with), legacy_seed__seed_pedigree__exact=pedigree).distinct()[:1000]
      else:
        experiment_list = Legacy_Experiment.objects.filter(experiment_id__like='%{}%'.format(starts_with)).distinct()[:1000]
    if radio == 'exact':
      if request.session.get('selected_legacy_pedigree', None):
        pedigree = request.session.get('selected_legacy_pedigree')
        experiment_list = Legacy_Experiment.objects.filter(experiment_id = starts_with, legacy_seed__seed_pedigree__exact=pedigree).distinct()[:1000]
      else:
        experiment_list = Legacy_Experiment.objects.filter(experiment_id = starts_with).distinct()[:1000]
  else:
    if request.session.get('selected_legacy_pedigree', None):
      pedigree = request.session.get('selected_legacy_pedigree')
      experiment_list = Legacy_Experiment.objects.filter(legacy_seed__seed_pedigree__exact=pedigree).distinct()[:1000]
    else:
      experiment_list = Legacy_Experiment.objects.all()
  context_dict = {'experiment_list': experiment_list}
  return render_to_response('legacy/legacy_experiment_list.html', context_dict, context)

def legacy_seed_inventory_sort(request):
  selected_stocks = []
  if request.session.get('selected_legacy_pedigree', None):
    pedigree = request.session.get('selected_legacy_pedigree')
    if request.session.get('selected_legacy_experiment', None):
      experiment = request.session.get('selected_legacy_experiment')
      selected_stocks = Legacy_Seed.objects.filter(seed_pedigree=pedigree, experiment_id_origin=experiment)
    else:
      selected_stocks = Legacy_Seed.objects.filter(seed_pedigree=pedigree)
  else:
    if request.session.get('selected_legacy_experiment', None):
      experiment = request.session.get('selected_legacy_experiment')
      selected_stocks = Legacy_Seed.objects.filter(experiment_id_origin=experiment)
    else:
      selected_stocks = Legacy_Seed.objects.all()[:1000]
  for stock in selected_stocks:
    stock.person = Legacy_People.objects.get(person_id = stock.seed_person_id)
  return selected_stocks

def legacy_session_variable_check(request):
  context_dict = {}
  if request.session.get('selected_legacy_pedigree', None):
    context_dict['selected_legacy_pedigree'] = request.session.get('selected_legacy_pedigree')
  if request.session.get('selected_legacy_experiment', None):
    context_dict['selected_legacy_experiment'] = request.session.get('selected_legacy_experiment')
  return context_dict

def legacy_seed_inv(request):
  context = RequestContext(request)
  context_dict = {}
  selected_stocks = legacy_seed_inventory_sort(request)
  context_dict = legacy_session_variable_check(request)
  context_dict['selected_stocks'] = selected_stocks
  exp_list = get_experiment_list()
  context_dict['exp_list'] = exp_list
  context_dict['logged_in_user'] = request.user.username
  return render_to_response('legacy/legacy_seed_inventory.html', context_dict, context)

def select_legacy_pedigree(request, legacy_pedigree):
  context = RequestContext(request)
  context_dict = {}
  request.session['selected_legacy_pedigree'] = legacy_pedigree
  selected_stocks = legacy_seed_inventory_sort(request)
  context_dict = legacy_session_variable_check(request)
  context_dict['selected_stocks'] = selected_stocks
  exp_list = get_experiment_list()
  context_dict['exp_list'] = exp_list
  context_dict['logged_in_user'] = request.user.username
  return render_to_response('legacy/legacy_seed_inventory.html', context_dict, context)

def select_legacy_experiment(request, legacy_experiment):
  context = RequestContext(request)
  context_dict = {}
  request.session['selected_legacy_experiment'] = legacy_experiment
  selected_stocks = legacy_seed_inventory_sort(request)
  context_dict = legacy_session_variable_check(request)
  context_dict['selected_stocks'] = selected_stocks
  exp_list = get_experiment_list()
  context_dict['exp_list'] = exp_list
  context_dict['logged_in_user'] = request.user.username
  return render_to_response('legacy/legacy_seed_inventory.html', context_dict, context)

def legacy_inventory_clear(request, clear_selected):
  context = RequestContext(request)
  context_dict = {}
  del request.session[clear_selected]
  selected_stocks = legacy_seed_inventory_sort(request)
  context_dict = legacy_session_variable_check(request)
  context_dict['selected_stocks'] = selected_stocks
  exp_list = get_experiment_list()
  context_dict['exp_list'] = exp_list
  context_dict['logged_in_user'] = request.user.username
  return render_to_response('legacy/legacy_seed_inventory.html', context_dict, context)

def select_legacy_row(request, legacy_row, legacy_seed):
  context = RequestContext(request)
  results_dict = {}
  context_dict = {}
  try:
    selected_seed = Legacy_Seed.objects.get(seed_id = legacy_seed)
    legacy_seed_person = Legacy_People.objects.get(person_id = selected_seed.seed_person_id)
    selected_seed.person = legacy_seed_person.person_name
  except Legacy_Seed.DoesNotExist:
    selected_seed = None
  results_dict['selected_seed'] = selected_seed
  try:
    row_info = Legacy_Row.objects.get(row_id = legacy_row)
  except Legacy_Row.DoesNotExist:
    row_info = None
  results_dict['selected_row'] = row_info
  try:
    storage_info = Legacy_Seed_Inventory.objects.filter(seed_id = legacy_seed)
  except Legacy_Seed_Inventory.DoesNotExist:
    storage_info = None
  results_dict['storage_info'] = storage_info

  if selected_seed is not None:
    try:
      child_rows = Legacy_Row.objects.filter(source_seed_id = legacy_seed)
    except Legacy_Row.DoesNotExist:
      child_rows = None

  step = 1
  source_row_value = row_info
  while source_row_value is not None:
    step_key = 'step{}'.format(step)
    source_row_key = 'source_row{}'.format(step)
    source_seed_key = 'source_seed{}'.format(step)
    seed_storage_key = 'seed_storage{}'.format(step)
    try:
      source_seed_value = Legacy_Seed.objects.get(seed_id = source_row_value.source_seed_id)
      seed_person_value = Legacy_People.objects.get(person_id = source_seed_value.seed_person_id)
      source_seed_value.person = seed_person_value.person_name
      try:
        seed_storage_value = Legacy_Seed_Inventory.objects.filter(seed_id = source_row_value.source_seed_id)
      except Legacy_Seed_Inventory.DoesNotExist:
        seed_storage_value = None
      try:
        source_row_value = Legacy_Row.objects.get(row_id = source_seed_value.row_id_origin)
      except Legacy_Row.DoesNotExist:
        source_row_value = None
    except Legacy_Seed.DoesNotExist:
      source_seed_value = None
      source_row_value = None
      seed_storage_value = None
    results_dict[source_seed_key] = source_seed_value
    results_dict[seed_storage_key] = seed_storage_value
    results_dict[source_row_key] = source_row_value
    results_dict[step_key] = step
    step = step + 1

  exp_list = get_experiment_list()
  context_dict['exp_list'] = exp_list
  context_dict['logged_in_user'] = request.user.username
  return render_to_response('legacy/legacy_row.html', results_dict, context)
