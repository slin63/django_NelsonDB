
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from mine.models import Category, Page, UserProfile, Experiment, Passport, Stock, StockPacket, Taxonomy, Source, AccessionCollecting, Field, Locality, Location
from mine.forms import CategoryForm, PageForm, UserForm, UserProfileForm, ChangePasswordForm, EditUserForm, EditUserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect

"""Used to handle data from URL, to ensure blank spaces don't mess things up"""
def encode_url(str):
	return str.replace(' ', '_')

def decode_url(str):
	return str.replace('_', ' ')

""""AJAX for suggesting category_list. This is obsolete and from the tango_with_django project
def get_category_list(max_results=0, starts_with=''):
	cat_list = []
	if starts_with:
		cat_list = Category.objects.filter(name__istartswith=starts_with)
	else:
		cat_list = Category.objects.all()
	if max_results > 0:
		if len(cat_list) > max_results:
			cat_list = cat_list[:max_results]
	for cat in cat_list:
		cat.url = encode_url(cat.name)
	return cat_list
"""

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
	exp_list = get_experiment_list()
	context_dict['exp_list'] = exp_list
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
	return render_to_response('mine/index.html', context_dict, context)

def about(request):
	context = RequestContext(request)
	context_dict={}
	exp_list = get_experiment_list()
	context_dict['exp_list'] = exp_list
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('mine/about.html', context_dict, context)

"""Was from tango_with_django project. Not used anymore."""
def category(request, category_name_url):
	context = RequestContext(request)
	category_name = decode_url(category_name_url)
	context_dict = {'category_name': category_name}
	cat_list = get_category_list()
	context_dict['cat_list'] = cat_list
	try:
		category = Category.objects.get(name=category_name)
		pages = Page.objects.filter(category=category).order_by('-views')
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('mine/category.html', context_dict, context)

"""Was from tango_with_django project. Not used anymore."""
@login_required
def like_category(request):
	context = RequestContext(request)
	cat_id = None
	if request.method == 'GET':
		cat_id = request.GET['category_id']
	likes = 0
	if cat_id:
		category = Category.objects.get(id=int(cat_id))
		if category:
			likes = category.likes + 1
			category.likes = likes
			category.save()
	return HttpResponse(likes)

"""Was from tango_with_django project. Not used anymore."""
@login_required
def add_category(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)
	else:
		form = CategoryForm()
	return render_to_response('mine/add_category.html', {'form': form}, context)

"""Was from tango_with_django project. Not used anymore."""
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
				return render_to_response('mine/add_category.html', {}, context)
			page.views = 0
			page.save()
			return category(request, category_name_url)
		else:
			print(form.errors)
	else:
		form = PageForm()
	return render_to_response('mine/add_page.html', {'category_name_url': category_name_url, 'category_name': category_name, 'form': form}, context)

def error_prelim(request, error_message):
	context = RequestContext(request)
	context_dict = {'errormessage': error_message}
	return render_to_response('mine/error_prelim.html', context_dict, context)

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
	return render_to_response('mine/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)

def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/mine/')
			else:
				return render_to_response('mine/login.html', {'disabled_account': 'disabled'}, context)
		else:
			return render_to_response('mine/login.html', {'bad_details': 'bad_details'}, context)
	else:
		return render_to_response('mine/login.html', {}, context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/mine/')

"""Was from tango_with_django project. Not used anymore."""
def suggest_category(request):
	context = RequestContext(request)
	cat_list = []
	starts_with = ''
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
	else:
		starts_with = request.POST['suggestion']
	cat_list = get_category_list(8, starts_with)
	return render_to_response('mine/category_list.html', {'cat_list': cat_list}, context)

def suggest_experiment(request):
	context = RequestContext(request)
	exp_list = []
	starts_with = ''
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
	else:
		starts_with = request.POST['suggestion']
	exp_list = get_experiment_list(200, starts_with)
	return render_to_response('mine/experiment_list.html', {'exp_list': exp_list}, context)

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
		pedigree_list = Passport.objects.filter(pedigree__like='%{}%'.format(starts_with))
	else:
		pedigree_list = Passport.objects.all()
	for pedigree in pedigree_list:
		pedigree.url = pedigree.id
	context_dict = {'pedigree_list': pedigree_list}
	return render_to_response('mine/pedigree_list.html', context_dict, context)

def suggest_locality(request):
	context = RequestContext(request)
	context_dict = {}
	locality_list = []
	starts_with = ''
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
	else:
		starts_with = request.POST['suggestion']
	if starts_with:
		locality_list = Locality.objects.filter(locality_name__like='%{}%'.format(starts_with))
	else:
		locality_list = Locality.objects.all()
	for locality in locality_list:
		locality.url = locality.id
	context_dict = {'locality_list': locality_list}
	return render_to_response('mine/locality_list.html', context_dict, context)

def suggest_field(request):
	context = RequestContext(request)
	context_dict = {}
	field_list = []
	starts_with = ''
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
	else:
		starts_with = request.POST['suggestion']
	if starts_with:
		field_list = Field.objects.filter(field_name__like='%{}%'.format(starts_with))
	else:
		field_list = Field.objects.all()
	for field in field_list:
		field.url = field.id
	context_dict = {'field_list': field_list}
	return render_to_response('mine/field_list.html', context_dict, context)

def suggest_collecting(request):
	context = RequestContext(request)
	context_dict = {}
	collecting_list = []
	starts_with = ''
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
	else:
		starts_with = request.POST['suggestion']
	if starts_with:
		collecting_list = AccessionCollecting.objects.filter(collection_date__like='%{}%'.format(starts_with))
	else:
		collecting_list = AccessionCollecting.objects.all()
	for collecting in collecting_list:
		collecting.url = collecting.id
	context_dict = {'collecting_list': collecting_list}
	return render_to_response('mine/collecting_list.html', context_dict, context)

def suggest_source(request):
	context = RequestContext(request)
	context_dict = {}
	source_list = []
	starts_with = ''
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
	else:
		starts_with = request.POST['suggestion']
	if starts_with:
		source_list = Source.objects.filter(source_name__like='%{}%'.format(starts_with))
	else:
		source_list = Source.objects.all()
	for source in source_list:
		source.url = source.id
	context_dict = {'source_list': source_list}
	return render_to_response('mine/sources_list.html', context_dict, context)

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
		taxonomy_list = Taxonomy.objects.filter(species__like='%{}%'.format(starts_with))
	else:
		taxonomy_list = Taxonomy.objects.all()
	for taxonomy in taxonomy_list:
		taxonomy.url = taxonomy.id
	context_dict = {'taxonomy_list': taxonomy_list}
	return render_to_response('mine/taxonomy_list.html', context_dict, context)

def profile(request, profile_name):
	context = RequestContext(request)
	exp_list = get_experiment_list()
	context_dict = {'exp_list': exp_list}
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
	return render_to_response('mine/profile.html', context_dict, context)

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
          return HttpResponseRedirect('/mine/login/')
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
  return render_to_response('mine/profile_change_password.html', context_dict, context)

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
	return render_to_response('mine/edit_profile.html', context_dict, context)

def track_url(request):
	context = RequestContext(request)
	page_id = None
	url = '/mine/'
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
	exp_list = get_experiment_list()
	context_dict['exp_list'] = exp_list
	try:
		experiment = Experiment.objects.get(name=experiment_name)
		context_dict['experiment'] = experiment
		u = User.objects.get(username=experiment.user)
		context_dict['user'] = u
	except Experiment.DoesNotExist:
		pass
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('mine/experiment.html', context_dict, context)

def seed_inventory_sort(request):
	if request.session.get('selected_locality_id', None):
		locality_id = request.session.get('selected_locality_id')
		if request.session.get('selected_field_id', None):
			field_id = request.session.get('selected_field_id')
			if request.session.get('selected_collecting_id', None):
				collecting_id = request.session.get('selected_collecting_id')
				if request.session.get('selected_passport_id', None):
					passport_id = request.session.get('selected_passport_id')
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id, taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.filter(id=collecting_id, field=Field.objects.filter(id=field_id, locality=Locality.objects.get(id=locality_id)))))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id,  accession_collecting=AccessionCollecting.objects.filter(id=collecting_id, field=Field.objects.filter(id=field_id, locality=Locality.objects.get(id=locality_id)))))
				else:
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.filter(id=collecting_id, field=Field.objects.filter(id=field_id, locality=Locality.objects.get(id=locality_id)))))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter( accession_collecting=AccessionCollecting.objects.filter(id=collecting_id, field=Field.objects.filter(id=field_id, locality=Locality.objects.get(id=locality_id)))))
			else:
				if request.session.get('selected_passport_id', None):
					passport_id = request.session.get('selected_passport_id')
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id, taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.filter(field=Field.objects.filter(id=field_id, locality=Locality.objects.get(id=locality_id)))))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id,  accession_collecting=AccessionCollecting.objects.filter(field=Field.objects.filter(id=field_id, locality=Locality.objects.get(id=locality_id)))))
				else:
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.filter(field=Field.objects.filter(id=field_id, locality=Locality.objects.get(id=locality_id)))))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter( accession_collecting=AccessionCollecting.objects.filter(field=Field.objects.filter(id=field_id, locality=Locality.objects.get(id=locality_id)))))
		else:
			if request.session.get('selected_collecting_id', None):
				collecting_id = request.session.get('selected_collecting_id')
				if request.session.get('selected_passport_id', None):
					passport_id = request.session.get('selected_passport_id')
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id, taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.filter(id=collecting_id, field=Field.objects.filter(locality=Locality.objects.get(id=locality_id)))))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id,  accession_collecting=AccessionCollecting.objects.filter(id=collecting_id, field=Field.objects.filter(locality=Locality.objects.get(id=locality_id)))))
				else:
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.filter(id=collecting_id, field=Field.objects.filter(locality=Locality.objects.get(id=locality_id)))))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter( accession_collecting=AccessionCollecting.objects.filter(id=collecting_id, field=Field.objects.filter(locality=Locality.objects.get(id=locality_id)))))
			else:
				if request.session.get('selected_passport_id', None):
					passport_id = request.session.get('selected_passport_id')
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id, taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.filter(field=Field.objects.filter(locality=Locality.objects.get(id=locality_id)))))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id,  accession_collecting=AccessionCollecting.objects.filter(field=Field.objects.filter(locality=Locality.objects.get(id=locality_id)))))
				else:
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.filter(field=Field.objects.filter(locality=Locality.objects.get(id=locality_id)))))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter( accession_collecting=AccessionCollecting.objects.filter(field=Field.objects.filter(locality=Locality.objects.get(id=locality_id)))))
	else:
		if request.session.get('selected_field_id', None):
			field_id = request.session.get('selected_field_id')
			if request.session.get('selected_collecting_id', None):
				collecting_id = request.session.get('selected_collecting_id')
				if request.session.get('selected_passport_id', None):
					passport_id = request.session.get('selected_passport_id')
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id, taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.filter(id=collecting_id, field=Field.objects.get(id=field_id))))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id,  accession_collecting=AccessionCollecting.objects.filter(id=collecting_id, field=Field.objects.get(id=field_id))))
				else:
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.filter(id=collecting_id, field=Field.objects.get(id=field_id))))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter( accession_collecting=AccessionCollecting.objects.filter(id=collecting_id, field=Field.objects.get(id=field_id))))
			else:
				if request.session.get('selected_passport_id', None):
					passport_id = request.session.get('selected_passport_id')
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id, taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.filter(field=Field.objects.get(id=field_id))))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id,  accession_collecting=AccessionCollecting.objects.filter(field=Field.objects.get(id=field_id))))
				else:
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.filter(field=Field.objects.get(id=field_id))))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter( accession_collecting=AccessionCollecting.objects.filter(field=Field.objects.get(id=field_id))))
		else:
			if request.session.get('selected_collecting_id', None):
				collecting_id = request.session.get('selected_collecting_id')
				if request.session.get('selected_passport_id', None):
					passport_id = request.session.get('selected_passport_id')
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id, taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.get(id=collecting_id)))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id,  accession_collecting=AccessionCollecting.objects.get(id=collecting_id)))
				else:
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(taxonomy=Taxonomy.objects.get(id=taxonomy_id), accession_collecting=AccessionCollecting.objects.get(id=collecting_id)))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter( accession_collecting=AccessionCollecting.objects.get(id=collecting_id)))
			else:
				if request.session.get('selected_passport_id', None):
					passport_id = request.session.get('selected_passport_id')
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(id=passport_id, taxonomy=Taxonomy.objects.get(id=taxonomy_id)))
					else:
						selected_stocks = Stock.objects.filter(passport=Passport.objects.get(id=passport_id))
				else:
					if request.session.get('selected_taxonomy_id', None):
						taxonomy_id = request.session.get('selected_taxonomy_id')
						selected_stocks = Stock.objects.filter(passport=Passport.objects.filter(taxonomy=Taxonomy.objects.get(id=taxonomy_id)))
					else:
						selected_stocks = Stock.objects.all()[:1000]
	return selected_stocks

def session_variable_check(request):
	context_dict = {}
	if request.session.get('selected_passport_id', None):
		context_dict['selected_passport_name'] = request.session.get('selected_passport_name')
	if request.session.get('selected_taxonomy_id', None):
		context_dict['selected_taxonomy_name'] = request.session.get('selected_taxonomy_name')
	if request.session.get('selected_source_id', None):
		context_dict['selected_source_name'] = request.session.get('selected_source_name')
	if request.session.get('selected_collecting_id', None):
		context_dict['selected_collecting_id'] = request.session.get('selected_collecting_id')
	if request.session.get('selected_field_id', None):
		context_dict['selected_field_id'] = request.session.get('selected_field_id')
	if request.session.get('selected_locality_id', None):
		context_dict['selected_locality_name'] = request.session.get('selected_locality_name')
	return context_dict

def seed_inventory(request):
	context = RequestContext(request)
	context_dict = {}
	selected_stocks = seed_inventory_sort(request)
	context_dict = session_variable_check(request)
	context_dict['selected_stocks'] = selected_stocks
	exp_list = get_experiment_list()
	context_dict['exp_list'] = exp_list
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('mine/seed_inventory.html', context_dict, context)

def seed_inventory_select_locality(request,locality_id):
	context = RequestContext(request)
	context_dict = {}
	selected_locality = Locality.objects.get(id=locality_id)
	request.session['selected_locality_name'] = selected_locality.locality_name
	request.session['selected_locality_id'] = selected_locality.id
	selected_stocks = seed_inventory_sort(request)
	context_dict = session_variable_check(request)
	context_dict['selected_stocks'] = selected_stocks
	exp_list = get_experiment_list()
	context_dict['exp_list'] = exp_list
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('mine/seed_inventory.html', context_dict, context)

def seed_inventory_select_field(request,field_id):
	context = RequestContext(request)
	context_dict = {}
	selected_field = Field.objects.get(id=field_id)
	request.session['selected_field_name'] = selected_field.field_name
	request.session['selected_field_id'] = selected_field.id
	selected_stocks = seed_inventory_sort(request)
	context_dict = session_variable_check(request)
	context_dict['selected_stocks'] = selected_stocks
	exp_list = get_experiment_list()
	context_dict['exp_list'] = exp_list
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('mine/seed_inventory.html', context_dict, context)

def seed_inventory_select_collection(request,collecting_id):
	context = RequestContext(request)
	context_dict = {}
	selected_collection = AccessionCollecting.objects.get(id=collecting_id)
	request.session['selected_collecting_name'] = selected_collection.collection_date
	request.session['selected_collecting_id'] = selected_collection.id
	selected_stocks = seed_inventory_sort(request)
	context_dict = session_variable_check(request)
	context_dict['selected_stocks'] = selected_stocks
	exp_list = get_experiment_list()
	context_dict['exp_list'] = exp_list
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('mine/seed_inventory.html', context_dict, context)

def seed_inventory_select_taxonomy(request,taxonomy_id):
	context = RequestContext(request)
	context_dict = {}
	selected_taxonomy = Taxonomy.objects.get(id=taxonomy_id)
	request.session['selected_taxonomy_name'] = selected_taxonomy.species
	request.session['selected_taxonomy_id'] = selected_taxonomy.id
	selected_stocks = seed_inventory_sort(request)
	context_dict = session_variable_check(request)
	context_dict['selected_stocks'] = selected_stocks
	exp_list = get_experiment_list()
	context_dict['exp_list'] = exp_list
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('mine/seed_inventory.html', context_dict, context)

def seed_inventory_select_source(request,source_id):
	context = RequestContext(request)
	context_dict = {}
	selected_source = Source.objects.get(id=source_id)
	request.session['selected_source_name'] = selected_source.source_name
	request.session['selected_source_id'] = selected_source.id
	selected_stocks = seed_inventory_sort(request)
	context_dict = session_variable_check(request)
	context_dict['selected_stocks'] = selected_stocks
	exp_list = get_experiment_list()
	context_dict['exp_list'] = exp_list
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('mine/seed_inventory.html', context_dict, context)

def seed_inventory_select_passport(request,passport_id):
	context = RequestContext(request)
	context_dict = {}
	selected_passport = Passport.objects.get(id=passport_id)
	request.session['selected_passport_name'] = selected_passport.pedigree
	request.session['selected_passport_id'] = selected_passport.id
	selected_stocks = seed_inventory_sort(request)
	context_dict = session_variable_check(request)
	context_dict['selected_stocks'] = selected_stocks
	exp_list = get_experiment_list()
	context_dict['exp_list'] = exp_list
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('mine/seed_inventory.html', context_dict, context)

def seed_inventory_clear(request, clear_selected):
	context = RequestContext(request)
	context_dict = {}
	clear_selected_name = '{}_name'.format(clear_selected)
	clear_selected_id = '{}_id'.format(clear_selected)
	del request.session[clear_selected_name]
	del request.session[clear_selected_id]
	selected_stocks = seed_inventory_sort(request)
	context_dict = session_variable_check(request)
	context_dict['selected_stocks'] = selected_stocks
	exp_list = get_experiment_list()
	context_dict['exp_list'] = exp_list
	context_dict['logged_in_user'] = request.user.username
	return render_to_response('mine/seed_inventory.html', context_dict, context)

def seed_inventory_select_stock(request, stock_id):
	context = RequestContext(request)
	context_dict = {}
	exp_list = get_experiment_list()
	context_dict['exp_list'] = exp_list
	selected_packets = StockPacket.objects.filter(stock=Stock.objects.get(id=stock_id))
	context_dict['selected_packets'] = selected_packets
	return render_to_response('mine/stock.html', context_dict, context)
