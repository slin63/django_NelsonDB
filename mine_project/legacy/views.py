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
from itertools import chain

"""These two function are for handling data passed through URL, to ensure no spaces"""
def encode_url(str):
  return str.replace(' ', '_')

def decode_url(str):
  return str.replace('_', ' ')

"""This function simply handles retrieving the experiments list that is displayed on the side of legacy templates. The ajax request is handled through mine.views get_experiment_list"""
def get_experiment_list(max_results=0, starts_with=''):
  exp_list = []
  exp_list = Experiment.objects.all()
  for exp in exp_list:
    exp.url = encode_url(exp.name)
  return exp_list
"""
These functions were for single selection. They are obsolete now because of the checkbox functions, found below.

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
"""

"""This function is run when the URL legacy/legacy_seed_inventory/ is used."""
def checkbox_legacy_seed_inv(request):
  context = RequestContext(request)
  context_dict = {}
  selected_stocks = checkbox_legacy_seed_inventory_sort(request)
  context_dict = checkbox_legacy_session_variable_check(request)
  context_dict['selected_stocks'] = selected_stocks
  exp_list = get_experiment_list()
  context_dict['exp_list'] = exp_list
  context_dict['logged_in_user'] = request.user.username
  return render_to_response('legacy/legacy_seed_inventory.html', context_dict, context)

"""This function is run once a stock is selected."""
def select_legacy_row(request, legacy_row, legacy_seed):
  context = RequestContext(request)
  results_dict = {}
  try:
    """Seed info for the selected stock is pulled from the Legacy_Seed table"""
    selected_seed = Legacy_Seed.objects.get(seed_id = legacy_seed)
    """The following 2 lines of code are used to find the person_name associated with the seed_person_id and assigns person_name to selected_seed so that the person_name can be displayed in the template"""
    legacy_seed_person = Legacy_People.objects.get(person_id = selected_seed.seed_person_id)
    selected_seed.person = legacy_seed_person.person_name
  except Legacy_Seed.DoesNotExist:
    selected_seed = None
  results_dict['selected_seed'] = selected_seed

  """Row info for the selected seed is pulled from the Legacy_Row table if it exists"""
  try:
    row_info = Legacy_Row.objects.get(row_id = legacy_row)
  except Legacy_Row.DoesNotExist:
    row_info = None
  results_dict['selected_row'] = row_info

  """Storage info for the selected seed is pulled from the Legacy_Seed_Inventory table if it exists"""
  try:
    storage_info = Legacy_Seed_Inventory.objects.filter(seed_id = legacy_seed)
  except Legacy_Seed_Inventory.DoesNotExist:
    storage_info = None
  results_dict['storage_info'] = storage_info

  """The following code finds children stocks of the selected stock"""
  try:
    child_rows = Legacy_Row.objects.filter(source_seed_id = legacy_seed)
  except Legacy_Row.DoesNotExist:
    child_rows = None
  results_dict['child_rows'] = child_rows

  """The following code builds the parental pedigree tree. Note that source_row_value is defined above as row_info for the selected seed."""
  step = 1
  source_row_value = row_info
  while source_row_value is not None and step<6:
    """Unique keys for each parental generation are formed. These keys are for the results_dict"""
    source_row_key = 'source_row{}'.format(step)
    source_seed_key = 'source_seed{}'.format(step)
    seed_storage_key = 'seed_storage{}'.format(step)
    try:
      """This recursively defines source_seed_value for the parent. This pulls the seed info from the Legacy_Seed table for the parent."""
      source_seed_value = Legacy_Seed.objects.get(seed_id = source_row_value.source_seed_id)
      """Again, the person_name is matched to the seed_person_id, and assigned to source_seed_value so that it can be called in the template"""
      seed_person_value = Legacy_People.objects.get(person_id = source_seed_value.seed_person_id)
      source_seed_value.person = seed_person_value.person_name
      try:
        """This pulls storage info for the parent from the Legacy_Seed_Inventory table if it exists"""
        seed_storage_value = Legacy_Seed_Inventory.objects.filter(seed_id = source_row_value.source_seed_id)
      except Legacy_Seed_Inventory.DoesNotExist:
        seed_storage_value = None
      try:
        """This pulls row info for the parent from the Legacy_Row table if it exists"""
        source_row_value = Legacy_Row.objects.get(row_id = source_seed_value.row_id_origin)
      except Legacy_Row.DoesNotExist:
        source_row_value = None
    except Legacy_Seed.DoesNotExist:
      source_seed_value = None
      source_row_value = None
      seed_storage_value = None
    """Keys and values are then assigned to the results_dict. Note that step is incremented to ensure unique keys. If source_row_value is None, then the while loop stops"""
    results_dict[source_seed_key] = source_seed_value
    results_dict[seed_storage_key] = seed_storage_value
    results_dict[source_row_key] = source_row_value
    step = step + 1

  """I am working on a way to iterate over results_dict to display the results in the template. Right now the template is hardcoded to display up to 5 results. This is a work in progress."""
  results_dict['step_count'] = reversed(range(1,step))

  results_dict['logged_in_user'] = request.user.username
  return render_to_response('legacy/legacy_row.html', results_dict, context)

"""This function checks if experiments or pedigrees have been checkbox selected, and queries the Legacy_Seed table for stocks that match the users selections."""
def checkbox_legacy_seed_inventory_sort(request):
  selected_stocks = []
  checkbox_experiment_list = []
  checkbox_pedigree_list = []
  if request.session.get('checkbox_legacy_experiment', None):
    checkbox_experiment_list = request.session.get('checkbox_legacy_experiment')
    if request.session.get('checkbox_legacy_pedigree', None):
      checkbox_pedigree_list = request.session.get('checkbox_legacy_pedigree')
      for pedigree in checkbox_pedigree_list:
        for experiment in checkbox_experiment_list:
          stocks = Legacy_Seed.objects.filter(seed_pedigree=pedigree, experiment_id_origin=experiment)
          selected_stocks = list(chain(selected_stocks, stocks))[:500]
    else:
      for experiment in checkbox_experiment_list:
        stocks = Legacy_Seed.objects.filter(experiment_id_origin=experiment)
        selected_stocks = list(chain(selected_stocks, stocks))[:500]
  else:
    if request.session.get('checkbox_legacy_pedigree', None):
      checkbox_pedigree_list = request.session.get('checkbox_legacy_pedigree')
      for pedigree in checkbox_pedigree_list:
        stocks = Legacy_Seed.objects.filter(seed_pedigree=pedigree)
        selected_stocks = list(chain(selected_stocks, stocks))[:500]
    else:
      selected_stocks = Legacy_Seed.objects.all()[:500]
  for stock in selected_stocks:
    stock.person = Legacy_People.objects.get(person_id = stock.seed_person_id)
    stock.location = Legacy_Seed_Inventory.objects.filter(seed_id = stock.seed_id)
  return selected_stocks

"""This function checks if experiments and pedigrees have been checkbox selected by the user. It is mainly useful for displaying the user's selections on the template, through the context_dict"""
def checkbox_legacy_session_variable_check(request):
  context_dict = {}
  if request.session.get('checkbox_legacy_pedigree', None):
    context_dict['checkbox_legacy_pedigree'] = request.session.get('checkbox_legacy_pedigree')
  if request.session.get('checkbox_legacy_experiment', None):
    context_dict['checkbox_legacy_experiment'] = request.session.get('checkbox_legacy_experiment')
  return context_dict

"""When the users selects experiments and hits submit, this function gets the list of selected experiments, assigns them to a session variable, calls the sorting function above to display relevant stocks, and calls the session_variable_check function above to display any previous user selections, such as pedigrees."""
def checkbox_selected_legacy_experiment(request):
  context = RequestContext(request)
  context_dict = {}
  checkbox_experiment_list = request.POST.getlist('checkbox_legacy_experiment')
  request.session['checkbox_legacy_experiment'] = checkbox_experiment_list
  selected_stocks = checkbox_legacy_seed_inventory_sort(request)
  context_dict = checkbox_legacy_session_variable_check(request)
  context_dict['selected_stocks'] = selected_stocks
  context_dict['logged_in_user'] = request.user.username
  return render_to_response('legacy/legacy_seed_inventory.html', context_dict, context)

"""When the users selects pedigrees and hits submit, this function gets the list of selected experiments, assigns them to a session variable, calls the sorting function above to display relevant stocks, and calls the session_variable_check function above to display any previous user selections, such as experiments."""
def checkbox_selected_legacy_pedigree(request):
  context = RequestContext(request)
  context_dict = {}
  checkbox_pedigree_list = request.POST.getlist('checkbox_legacy_pedigree')
  request.session['checkbox_legacy_pedigree'] = checkbox_pedigree_list
  selected_stocks = checkbox_legacy_seed_inventory_sort(request)
  context_dict = checkbox_legacy_session_variable_check(request)
  context_dict['selected_stocks'] = selected_stocks
  context_dict['logged_in_user'] = request.user.username
  return render_to_response('legacy/legacy_seed_inventory.html', context_dict, context)

"""Working on removing duplicates from the experiment and pedigree suggestions"""
def remove_duplicates(seq, idfun=None):
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

"""This function processes AJAX requests for suggesting experiments. Note that this function checks if the user has previously selected pedigrees, and limits the suggested experiments based on those selections."""
def checkbox_suggest_legacy_experiment(request):
  context = RequestContext(request)
  context_dict = {}
  experiment_list = []
  starts_with = ''
  """Here the user's typed input and the radio button selection are passed to variables"""
  if request.method == 'GET':
    starts_with = request.GET['suggestion']
    radio = request.GET['radio']
  else:
    starts_with = request.POST['suggestion']
    radio = request.POST['radio']
  """If the user typed something"""
  if starts_with:
    if radio == 'variable':
      """If pedigrees have been selected by the user"""
      if request.session.get('checkbox_legacy_pedigree', None):
        pedigree_list = request.session.get('checkbox_legacy_pedigree')
        """Here the selected pedigrees are looped over in a for loop"""
        for pedigree in pedigree_list:
          """Here the text input and the selected pedigree are used to query the Legacy_Experiment table"""
          experiment = Legacy_Experiment.objects.filter(experiment_id__like='%{}%'.format(starts_with), legacy_seed__seed_pedigree__exact=pedigree).distinct()[:1000]
          """experiment_list is recursively defined here to create a list that includes all experiments that match the user's input and pedigree selections"""
          experiment_list = list(chain(experiment_list, experiment))
      else:
        experiment_list = Legacy_Experiment.objects.filter(experiment_id__like='%{}%'.format(starts_with)).distinct()[:1000]
    if radio == 'exact':
      if request.session.get('checkbox_legacy_pedigree', None):
        pedigree_list = request.session.get('checkbox_legacy_pedigree')
        for pedigree in pedigree_list:
          experiment = Legacy_Experiment.objects.filter(experiment_id = starts_with, legacy_seed__seed_pedigree__exact=pedigree).distinct()[:1000]
          experiment_list = list(chain(experiment, experiment_list))
      else:
        experiment_list = Legacy_Experiment.objects.filter(experiment_id = starts_with).distinct()[:1000]
  else:
    if request.session.get('checkbox_legacy_pedigree', None):
      pedigree_list = request.session.get('checkbox_legacy_pedigree')
      for pedigree in pedigree_list:
        experiment = Legacy_Experiment.objects.filter(legacy_seed__seed_pedigree__exact=pedigree).distinct()[:1000]
        experiment_list = list(chain(experiment, experiment_list))
    else:
      experiment_list = Legacy_Experiment.objects.all()
  context_dict = {'experiment_list': experiment_list}
  return render_to_response('legacy/legacy_experiment_list.html', context_dict, context)

"""This function processes AJAX requests for suggesting pedigrees. Note that this function checks if the user has previously selected experiments, and limits the suggested pedigrees based on those selections."""
def checkbox_suggest_legacy_pedigree(request):
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
      if request.session.get('checkbox_legacy_experiment', None):
        experiment_list = request.session.get('checkbox_legacy_experiment')
        for experiment in experiment_list:
          pedigree = Legacy_Seed.objects.filter(seed_pedigree__like='%{}%'.format(starts_with), experiment_id_origin = experiment).values('seed_pedigree').distinct()[:3000]
          pedigree_list = list(chain(pedigree_list, pedigree))
      else:
        pedigree_list = Legacy_Seed.objects.filter(seed_pedigree__like='%{}%'.format(starts_with)).values('seed_pedigree').distinct()[:3000]
    if radio == 'exact':
      if request.session.get('checkbox_legacy_experiment', None):
        experiment_list = request.session.get('checkbox_legacy_experiment')
        for experiment in experiment_list:
          pedigree = Legacy_Seed.objects.filter(seed_pedigree = starts_with, experiment_id_origin = experiment).values('seed_pedigree').distinct()[:3000]
          pedigree_list = list(chain(pedigree_list, pedigree))
      else:
        pedigree_list = Legacy_Seed.objects.filter(seed_pedigree = starts_with).values('seed_pedigree').distinct()[:3000]
  else:
    if request.session.get('checkbox_legacy_experiment', None):
      experiment_list = request.session.get('checkbox_legacy_experiment')
      for experiment in experiment_list:
        pedigree = Legacy_Seed.objects.filter(experiment_id_origin = experiment).values('seed_pedigree').distinct()[:3000]
        pedigree_list = list(chain(pedigree_list, pedigree))
    else:
      pedigree_list = Legacy_Seed.objects.all().values('seed_pedigree').distinct()[:3000]
  context_dict['pedigree_list'] = pedigree_list
  return render_to_response('legacy/legacy_pedigree_list.html', context_dict, context)

"""This function clears any previously selected experiments or pedigrees"""
def checkbox_legacy_inventory_clear(request, clear_selected):
  context = RequestContext(request)
  context_dict = {}
  del request.session[clear_selected]
  selected_stocks = checkbox_legacy_seed_inventory_sort(request)
  context_dict = checkbox_legacy_session_variable_check(request)
  context_dict['selected_stocks'] = selected_stocks
  context_dict['logged_in_user'] = request.user.username
  return render_to_response('legacy/legacy_seed_inventory.html', context_dict, context)
