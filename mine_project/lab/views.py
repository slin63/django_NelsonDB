
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from lab.models import UserProfile, Experiment, Passport, Stock, StockPacket, Taxonomy, People, Collecting, Field, Locality, Location, ObsRow, ObsSelector, Isolate, DiseaseInfo
from lab.forms import UserForm, UserProfileForm, ChangePasswordForm, EditUserForm, EditUserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect
from itertools import chain

"""Used to handle data from URL, to ensure blank spaces don't mess things up"""
def encode_url(str):
	return str.replace(' ', '_')

def decode_url(str):
	return str.replace('_', ' ')


"""This is used to process AJAX requests when something is typed in the "find an experiment" input. It is used to display the experiments on the left side of the templates."""
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

def index(request):
	context = RequestContext(request)
	context_dict = {}
	if request.session.get('last_visit'):
		last_visit = request.session.get('last_visit')
		visits = request.session.get('visits', 0)
		if(datetime.now() - datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")).days > 0:
			request.session['visits'] = visits + 1
			request.session['last_visit'] = str(datetime.now())
	else:
		request.session['last_visit'] = str(datetime.now())
		request.session['visits'] = 1
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/index.html', context_dict, context)

def about_people(request):
	context = RequestContext(request)
	context_dict = {}
	context_dict['users'] = zip(User.objects.all(), UserProfile.objects.all())
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/people.html', context_dict, context)

def about_literature(request):
	context = RequestContext(request)
	context_dict = {}
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/literature.html', context_dict, context)

def about_goals(request):
	context = RequestContext(request)
	context_dict = {}
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/goals.html', context_dict, context)

def about_collaborators(request):
	context = RequestContext(request)
	context_dict = {}
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/collaborators.html', context_dict, context)


"""Was from tango_with_django project. Not used anymore.

def add_page(request, category_name_url):
	context = RequestContext(request)
	category_name = decode_url(category_name_url)
	context_dict = {'category_name': category_name}
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			page = form.save(commit=False)
			try:
				cat = Category.objects.get(name=category_name)
				page.category = cat
			except Category.DoesNotExist:
				return render_to_response('lab/add_category.html', {}, context)
			page.views = 0
			page.save()
			return category(request, category_name_url)
		else:
			print(form.errors)
	else:
		form = PageForm()
	return render_to_response('lab/add_page.html', {'category_name_url': category_name_url, 'category_name': category_name, 'form': form}, context)
"""

def error_prelim(request, error_message):
	context = RequestContext(request)
	context_dict = {'errormessage': error_message}
	return render_to_response('lab/error_prelim.html', context_dict, context)

def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render_to_response('lab/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)

def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/lab/')
			else:
				return render_to_response('lab/login.html', {'disabled_account': 'disabled'}, context)
		else:
			return render_to_response('lab/login.html', {'bad_details': 'bad_details'}, context)
	else:
		return render_to_response('lab/login.html', {}, context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/lab/')

def profile(request, profile_name):
	context = RequestContext(request)
	context_dict = {}
	u = User.objects.get(username=profile_name)
	try:
		up = UserProfile.objects.get(user=u)
	except:
		up = None
	context_dict['user'] = u
	context_dict['userprofile'] = up
	if User.is_authenticated and profile_name == request.user.username:
		context_dict['checked_user'] = True
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/profile.html', context_dict, context)

def profile_change_password(request):
  context = RequestContext(request)
  context_dict = {}
  if request.method == 'POST':
    change_password_form = ChangePasswordForm(data=request.POST)
    if change_password_form.is_valid():
      if change_password_form.cleaned_data['new_password'] == change_password_form.cleaned_data['new_password_repeat']:
        user = authenticate(username=request.user.username, password=change_password_form.cleaned_data['old_password'])
        if user is not None:
          user.set_password(change_password_form.cleaned_data['new_password'])
          user.save()
          logout(request)
          return HttpResponseRedirect('/lab/login/')
        else:
          context_dict['wrong_password'] = 'wrong_password'
      else:
        context_dict['wrong_repeat'] = 'wrong_repeat'
    else:
      print(change_password_form.errors)
  else:
    change_password_form = ChangePasswordForm()
  context_dict['change_password_form'] = change_password_form
  context_dict['logged_in_user'] = request.user.username
  return render_to_response('lab/profile_change_password.html', context_dict, context)

def edit_profile(request):
	context = RequestContext(request)
	context_dict = {}
	user_instance = request.user
	profile_instance = UserProfile.objects.get(user=user_instance)
	user_form = EditUserForm(request.POST or None, instance=user_instance)
	profile_form = EditUserProfileForm(request.POST or None, instance=profile_instance)
	if user_form.is_valid() and profile_form.is_valid():
		user = authenticate(username=request.user.username, password=user_form.cleaned_data['password'])
		if user is not None:
			user_form.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			context_dict['edit_complete'] = 'edit_complete'
		else:
			context_dict['wrong_password'] = 'wrong_password'
	else:
		print(user_form.errors, profile_form.errors)
	context_dict['user_form'] = user_form
	context_dict['profile_form'] = profile_form
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/edit_profile.html', context_dict, context)

def track_url(request):
	context = RequestContext(request)
	page_id = None
	url = '/lab/'
	if request.method == 'GET':
		if 'page_id' in request.GET:
			page_id = request.GET['page_id']
			try:
				page = Page.objects.get(id=page_id)
				page.views = page.views + 1
				page.save()
				url = page.url
			except:
				pass
	return redirect(url)

def experiment(request, experiment_name_url):
	context = RequestContext(request)
	experiment_name = decode_url(experiment_name_url)
	context_dict = {'experiment_name': experiment_name}
	if experiment_name is not 'search':
		try:
			experiment = Experiment.objects.get(name=experiment_name)
			context_dict['experiment'] = experiment
			u = User.objects.get(username=experiment.user)
			context_dict['user'] = u
		except Experiment.DoesNotExist:
			pass
	if experiment_name == 'search':
		exp_list = get_experiment_list()
		context_dict['exp_list'] = exp_list
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/experiment.html', context_dict, context)

def checkbox_seed_inventory_sort(request):
	selected_stocks = {}
	checkbox_taxonomy_list = []
	checkbox_pedigree_list = []
	if request.session.get('checkbox_taxonomy', None):
		checkbox_taxonomy_list = request.session.get('checkbox_taxonomy')
		if request.session.get('checkbox_pedigree', None):
			checkbox_pedigree_list = request.session.get('checkbox_pedigree')
			for pedigree in checkbox_pedigree_list:
				for taxonomy in checkbox_taxonomy_list:
					stocks = Stock.objects.filter(pedigree=pedigree, passport__taxonomy__population=taxonomy)
					selected_stocks = list(chain(selected_stocks, stocks))[:1000]
		else:
			for taxonomy in checkbox_taxonomy_list:
				stocks = Stock.objects.filter(passport__taxonomy__population=taxonomy)
				selected_stocks = list(chain(selected_stocks, stocks))[:1000]
	else:
		if request.session.get('checkbox_pedigree', None):
			checkbox_pedigree_list = request.session.get('checkbox_pedigree')
			for pedigree in checkbox_pedigree_list:
				stocks = Stock.objects.filter(pedigree=pedigree)
				selected_stocks = list(chain(selected_stocks, stocks))[:1000]
		else:
			selected_stocks = Stock.objects.all()[:1000]
	return selected_stocks

def checkbox_session_variable_check(request):
	context_dict = {}
	if request.session.get('checkbox_pedigree', None):
		context_dict['checkbox_pedigree'] = request.session.get('checkbox_pedigree')
	if request.session.get('checkbox_taxonomy', None):
		context_dict['checkbox_taxonomy'] = request.session.get('checkbox_taxonomy')
	if request.session.get('checkbox_isolate_disease', None):
		context_dict['checkbox_isolate_disease'] = request.session.get('checkbox_isolate_disease')
	if request.session.get('checkbox_isolate_taxonomy', None):
		context_dict['checkbox_isolate_taxonomy'] = request.session.get('checkbox_isolate_taxonomy')
	return context_dict

def seed_inventory(request):
	context = RequestContext(request)
	context_dict = {}
	selected_stocks = checkbox_seed_inventory_sort(request)
	context_dict = checkbox_session_variable_check(request)
	context_dict['selected_stocks'] = selected_stocks
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/seed_inventory.html', context_dict, context)

def suggest_pedigree(request):
	context = RequestContext(request)
	context_dict = {}
	pedigree_list = []
	starts_with = ''
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
	else:
		starts_with = request.POST['suggestion']
	if starts_with:
		if request.session.get('checkbox_taxonomy', None):
			checkbox_taxonomy_list = request.session.get('checkbox_taxonomy')
			for taxonomy in checkbox_taxonomy_list:
				pedigree = Stock.objects.filter(pedigree__contains=starts_with, passport__taxonomy__population=taxonomy).values('pedigree', 'passport__taxonomy__population').distinct()[:1000]
				pedigree_list = list(chain(pedigree, pedigree_list))
		else:
			pedigree_list = Stock.objects.filter(pedigree__contains=starts_with).values('pedigree').distinct()[:1000]
	else:
		if request.session.get('checkbox_taxonomy', None):
			checkbox_taxonomy_list = request.session.get('checkbox_taxonomy')
			for taxonomy in checkbox_taxonomy_list:
				pedigree = Stock.objects.filter(passport__taxonomy__population=taxonomy).values('pedigree', 'passport__taxonomy__population').distinct()[:1000]
				pedigree_list = list(chain(pedigree, pedigree_list))
		else:
			pedigree_list = Stock.objects.all().values('pedigree').distinct()[:1000]
	context_dict = checkbox_session_variable_check(request)
	context_dict['pedigree_list'] = pedigree_list
	return render_to_response('lab/seed_pedigree_list.html', context_dict, context)

def suggest_taxonomy(request):
	context = RequestContext(request)
	context_dict = {}
	taxonomy_list = []
	starts_with = ''
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
	else:
		starts_with = request.POST['suggestion']
	if starts_with:
		if request.session.get('checkbox_pedigree', None):
			checkbox_pedigree_list = request.session.get('checkbox_pedigree')
			for pedigree in checkbox_pedigree_list:
				taxonomy = Stock.objects.filter(pedigree=pedigree, passport__taxonomy__population__contains=starts_with).values('pedigree', 'passport__taxonomy__population', 'passport__taxonomy__species').distinct()[:1000]
				taxonomy_list = list(chain(taxonomy, taxonomy_list))
		else:
			taxonomy_list = Taxonomy.objects.filter(population__contains=starts_with, common_name='Maize')[:1000]
	else:
		if request.session.get('checkbox_pedigree', None):
			checkbox_pedigree_list = request.session.get('checkbox_pedigree')
			for pedigree in checkbox_pedigree_list:
				taxonomy = Stock.objects.filter(pedigree=pedigree).values('pedigree', 'passport__taxonomy__population', 'passport__taxonomy__species').distinct()[:1000]
				taxonomy_list = list(chain(taxonomy, taxonomy_list))
		else:
			taxonomy_list = Taxonomy.objects.filter(common_name='Maize')[:1000]
	context_dict = checkbox_session_variable_check(request)
	context_dict['taxonomy_list'] = taxonomy_list
	return render_to_response('lab/seed_taxonomy_list.html', context_dict, context)

def select_pedigree(request):
	context = RequestContext(request)
	context_dict = {}
	checkbox_pedigree_list = request.POST.getlist('checkbox_pedigree')
	request.session['checkbox_pedigree'] = checkbox_pedigree_list
	selected_stocks = checkbox_seed_inventory_sort(request)
	context_dict = checkbox_session_variable_check(request)
	context_dict['selected_stocks'] = selected_stocks
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/seed_inventory.html', context_dict, context)

def select_taxonomy(request):
	context = RequestContext(request)
	context_dict = {}
	checkbox_taxonomy_list = request.POST.getlist('checkbox_taxonomy')
	request.session['checkbox_taxonomy'] = checkbox_taxonomy_list
	selected_stocks = checkbox_seed_inventory_sort(request)
	context_dict = checkbox_session_variable_check(request)
	context_dict['selected_stocks'] = selected_stocks
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/seed_inventory.html', context_dict, context)

def checkbox_seed_inventory_clear(request, clear_selected):
	context = RequestContext(request)
	context_dict = {}
	del request.session[clear_selected]
	selected_stocks = checkbox_seed_inventory_sort(request)
	context_dict = checkbox_session_variable_check(request)
	context_dict['selected_stocks'] = selected_stocks
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/seed_inventory.html', context_dict, context)

def select_stockpacket_from_stock(request):
	context = RequestContext(request)
	context_dict = {}
	selected_packets = []
	checkbox_stock_list = request.POST.getlist('checkbox_stock')
	request.session['checkbox_stock'] = checkbox_stock_list
	for stock in checkbox_stock_list:
		packet = StockPacket.objects.filter(stock__id=stock)
		selected_packets = list(chain(packet, selected_packets))
	context_dict = checkbox_session_variable_check(request)
	context_dict['selected_packets'] = selected_packets
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/stock.html', context_dict, context)

def row_data_from_experiment(request, experiment_name):
	context = RequestContext(request)
	context_dict = {}
	context_dict = checkbox_session_variable_check(request)
	row_data = ObsRow.objects.filter(obs_selector__experiment__name=experiment_name)
	context_dict['row_data'] = row_data
	context_dict['experiment_name'] = experiment_name
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/row.html', context_dict, context)

def passport(request, passport_id):
	context = RequestContext(request)
	context_dict = {}
	passport = Passport.objects.get(id=passport_id)
	try:
		collecting_row = ObsRow.objects.get(obs_selector=passport.collecting.obs_selector)
	except ObsRow.DoesNotExist:
		collecting_row = None
	if passport.collecting.field.field_name != 'No Field':
		collecting_field = True
	else:
		collecting_field = None
	if passport.people.organization != 'No Source' and passport.people.organization != '':
		collecting_source = True
	else:
		collecting_source = None
	context_dict['passport'] = passport
	context_dict['collecting_row'] = collecting_row
	context_dict['collecting_field'] = collecting_field
	context_dict['collecting_source'] = collecting_source
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/passport.html', context_dict, context)

def isolate_inventory(request):
	context = RequestContext(request)
	context_dict = {}
	context_dict = checkbox_session_variable_check(request)
	selected_isolates = checkbox_isolate_sort(request)
	context_dict['selected_isolates'] = selected_isolates
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/isolate_inventory.html', context_dict, context)

def checkbox_isolate_sort(request):
	selected_isolates = {}
	checkbox_taxonomy_list = []
	checkbox_disease_list = []
	if request.session.get('checkbox_isolate_taxonomy', None):
		checkbox_taxonomy_list = request.session.get('checkbox_isolate_taxonomy')
		if request.session.get('checkbox_isolate_disease', None):
			checkbox_disease_list = request.session.get('checkbox_isolate_disease')
			for disease in checkbox_disease_list:
				for genus in checkbox_taxonomy_list:
					isolates = Isolate.objects.filter(disease_info__common_name=disease, passport__taxonomy__genus=genus)
					selected_isolates = list(chain(selected_isolates, isolates))[:1000]
		else:
			for genus in checkbox_taxonomy_list:
				isolates = Isolate.objects.filter(passport__taxonomy__genus=genus)
				selected_isolates = list(chain(selected_isolates, isolates))[:1000]
	else:
		if request.session.get('checkbox_isolate_disease', None):
			checkbox_disease_list = request.session.get('checkbox_isolate_disease')
			for disease in checkbox_disease_list:
				isolates = Isolate.objects.filter(disease_info__common_name=disease)
				selected_isolates = list(chain(selected_isolates, isolates))[:1000]
		else:
			selected_isolates = Isolate.objects.all()[:1000]
	return selected_isolates

def suggest_isolate_taxonomy(request):
	context = RequestContext(request)
	context_dict = {}
	isolate_taxonomy_list = []
	starts_with = ''
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
	else:
		starts_with = request.POST['suggestion']
	if starts_with:
		if request.session.get('checkbox_isolate_disease', None):
			checkbox_isolate_disease = request.session.get('checkbox_isolate_disease')
			for disease in checkbox_isolate_disease:
				taxonomy = Isolate.objects.filter(disease_info__common_name=disease, passport__taxonomy__genus__contains=starts_with).values('disease_info__common_name', 'passport__taxonomy__genus', 'passport__taxonomy__alias', 'passport__taxonomy__race', 'passport__taxonomy__subtaxa', 'passport__taxonomy__species').distinct()[:1000]
				isolate_taxonomy_list = list(chain(taxonomy, isolate_taxonomy_list))
		else:
			isolate_taxonomy_list = Taxonomy.objects.filter(genus__contains=starts_with, common_name='Isolate')[:1000]
	else:
		if request.session.get('checkbox_isolate_disease', None):
			checkbox_isolate_disease = request.session.get('checkbox_isolate_disease')
			for disease in checkbox_isolate_disease:
				taxonomy = Isolate.objects.filter(disease_info__common_name=disease).values('disease_info__common_name', 'passport__taxonomy__genus', 'passport__taxonomy__alias', 'passport__taxonomy__race', 'passport__taxonomy__subtaxa', 'passport__taxonomy__species').distinct()[:1000]
				isolate_taxonomy_list = list(chain(taxonomy, isolate_taxonomy_list))
		else:
			isolate_taxonomy_list = Taxonomy.objects.filter(common_name='Isolate')[:1000]
	context_dict = checkbox_session_variable_check(request)
	context_dict['isolate_taxonomy_list'] = isolate_taxonomy_list
	return render_to_response('lab/isolate_taxonomy_list.html', context_dict, context)

def suggest_isolate_disease(request):
	context = RequestContext(request)
	context_dict = {}
	isolate_disease_list = []
	starts_with = ''
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
	else:
		starts_with = request.POST['suggestion']
	if starts_with:
		if request.session.get('checkbox_isolate_taxonomy', None):
			checkbox_isolate_taxonomy = request.session.get('checkbox_isolate_taxonomy')
			for genus in checkbox_isolate_taxonomy:
				disease = Isolate.objects.filter(disease_info__common_name=starts_with, passport__taxonomy__genus=genus).values('disease_info__common_name', 'passport__taxonomy__genus').distinct()[:1000]
				isolate_disease_list = list(chain(disease, isolate_disease_list))
		else:
			isolate_disease_list = DiseaseInfo.objects.filter(common_name__contains=starts_with)[:1000]
	else:
		if request.session.get('checkbox_isolate_taxonomy', None):
			checkbox_isolate_taxonomy = request.session.get('checkbox_isolate_taxonomy')
			for genus in checkbox_isolate_taxonomy:
				disease = Isolate.objects.filter(passport__taxonomy__genus=genus).values('disease_info__common_name', 'passport__taxonomy__genus').distinct()[:1000]
				isolate_disease_list = list(chain(disease, isolate_disease_list))
		else:
			isolate_disease_list = DiseaseInfo.objects.all()[:1000]
	context_dict = checkbox_session_variable_check(request)
	context_dict['isolate_disease_list'] = isolate_disease_list
	return render_to_response('lab/isolate_disease_list.html', context_dict, context)

def select_isolate_taxonomy(request):
	context = RequestContext(request)
	context_dict = {}
	checkbox_isolate_taxonomy = request.POST.getlist('checkbox_isolate_taxonomy')
	request.session['checkbox_isolate_taxonomy'] = checkbox_isolate_taxonomy
	selected_isolates = checkbox_isolate_sort(request)
	context_dict = checkbox_session_variable_check(request)
	context_dict['selected_isolates'] = selected_isolates
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/isolate_inventory.html', context_dict, context)

def select_isolate_disease(request):
	context = RequestContext(request)
	context_dict = {}
	checkbox_isolate_disease = request.POST.getlist('checkbox_isolate_disease')
	request.session['checkbox_isolate_disease'] = checkbox_isolate_disease
	selected_isolates = checkbox_isolate_sort(request)
	context_dict = checkbox_session_variable_check(request)
	context_dict['selected_isolates'] = selected_isolates
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/isolate_inventory.html', context_dict, context)

def checkbox_isolate_inventory_clear(request, clear_selected):
	context = RequestContext(request)
	context_dict = {}
	del request.session[clear_selected]
	selected_isolates = checkbox_isolate_sort(request)
	context_dict = checkbox_session_variable_check(request)
	context_dict['selected_isolates'] = selected_isolates
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/isolate_inventory.html', context_dict, context)

def select_isolates(request):
	context = RequestContext(request)
	context_dict = {}
	selected_isolates = []
	checkbox_isolates_list = request.POST.getlist('checkbox_isolates')
	request.session['checkbox_isolates'] = checkbox_isolates_list
	for isolate in checkbox_isolates_list:
		isolate = Isolate.objects.filter(id=isolate)
		selected_isolates = list(chain(isolate, selected_isolates))
	context_dict = checkbox_session_variable_check(request)
	context_dict['selected_isolates'] = selected_isolates
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/isolate.html', context_dict, context)

def disease_info(request, disease_id):
	context = RequestContext(request)
	context_dict = {}
	try:
		disease_info = DiseaseInfo.objects.get(id=disease_id)
	except DiseaseInfo.DoesNotExist:
		disease_info = None
	context_dict['disease_info'] = disease_info
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/disease_info.html', context_dict, context)
