"""Handles views for the IsolateStock pages. Templates stored in /templates/lab/isolatestock
Details at: https://docs.google.com/document/d/1IVkC0RxJe-P1xGAM4WMGCjp5JYcFlRtQj5PGvZNpAJA/edit"""

import json
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from itertools import chain

from lab.forms import LogIsolateStocksOnlineForm
from lab.models import Passport, Stock, Taxonomy, ObsRow, ObsPlant, ObsWell, ObsCulture, ObsTissue, ObsDNA, ObsPlate, ObsMicrobe, \
    ObsTracker, IsolateStock, GlycerolStock
from lab.views import checkbox_session_variable_check, get_obs_tracker


def select_isolatestocks(request):
    context = RequestContext(request)
    context_dict = {}
    selected_isolatestocks = []
    checkbox_isolatestocks_list = request.POST.getlist('checkbox_isolatestocks')
    request.session['checkbox_isolatestocks'] = checkbox_isolatestocks_list
    for isolatestock in checkbox_isolatestocks_list:
        isolatestock = IsolateStock.objects.filter(id=isolatestock)
        selected_isolatestocks = list(chain(isolatestock, selected_isolatestocks))
    context_dict = checkbox_session_variable_check(request)
    context_dict['selected_isolatestocks'] = selected_isolatestocks
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/isolatestock/isolatestock.html', context_dict, context)


def datatable_isolatestock_inventory(request):
    selected_isolatestocks = checkbox_isolatestock_sort(request)
    #count = selected_isolatestocks.count()
    arr = []
    for data in selected_isolatestocks:
        arr.append({
            'input': '<input type="checkbox" name="checkbox_isolatestocks" value="%s">'%(data.id),
            'id': data.id,
            'isolatestock_id': data.isolatestock_id,
            'isolatestock_name': data.isolatestock_name,
            'disease_name': data.disease_info.common_name,
            'disease_id': data.disease_info.id,
            'plant_organ': data.plant_organ,
            'genus': data.passport.taxonomy.genus,
            'alias': data.passport.taxonomy.alias,
            'race': data.passport.taxonomy.race,
            'subtaxa': data.passport.taxonomy.subtaxa,
            'comments': data.comments,
        })
    return JsonResponse({'data':arr}, safe=True)


def checkbox_isolatestock_sort(request):
    selected_isolatestocks = {}
    checkbox_taxonomy_list = []
    checkbox_disease_list = []
    if request.session.get('checkbox_isolatestock_taxonomy', None):
        checkbox_taxonomy_list = request.session.get('checkbox_isolatestock_taxonomy')
        if request.session.get('checkbox_isolatestock_disease', None):
            checkbox_disease_list = request.session.get('checkbox_isolatestock_disease')
            for disease_id in checkbox_disease_list:
                for taxonomy_id in checkbox_taxonomy_list:
                    isolatestocks = IsolateStock.objects.filter(disease_info__id=disease_id, passport__taxonomy__id=taxonomy_id)
                    selected_isolatestocks = list(chain(selected_isolatestocks, isolatestocks))
        else:
            for taxonomy_id in checkbox_taxonomy_list:
                isolatestocks = IsolateStock.objects.filter(passport__taxonomy__id=taxonomy_id)
                selected_isolatestocks = list(chain(selected_isolatestocks, isolatestocks))
    else:
        if request.session.get('checkbox_isolatestock_disease', None):
            checkbox_disease_list = request.session.get('checkbox_isolatestock_disease')
            for disease_id in checkbox_disease_list:
                isolatestocks = IsolateStock.objects.filter(disease_info__id=disease_id)
                selected_isolatestocks = list(chain(selected_isolatestocks, isolatestocks))
        else:
            selected_isolatestocks = list(IsolateStock.objects.all().exclude(id=1))[:2000]
    return selected_isolatestocks


@login_required
def isolatestock_inventory(request):
    """
    ::url:: = /iso_inventory/ - To change
    ::func:: = Renders view for the seed inventory page
    ::html:: = seed_inventory.html
    """
    context = RequestContext(request)
    context_dict = {}
    context_dict = checkbox_session_variable_check(request)
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/isolatestock/isolatestock_inventory.html', context_dict, context)


def select_taxonomy(request):
    """
    ::url:: = /seed_inventory/select_taxonomy/ - To change
    ::func:: = Supporting function for the Population (taxonomy) search table in seed_inventory
    ::ajax:: = $('#select_taxonomy_form_submit').
    ::html:: = isolatestock_source_list.html, seed_inventory.html
    ::NOTES:: = Native cross functionality with IsolateStock pages
    """
    taxonomy = request.POST['taxonomy']
    taxonomy_list = json.loads(taxonomy)
    request.session['checkbox_taxonomy'] = taxonomy_list
    return JsonResponse({'success': True})


def suggest_taxonomy(request):
    """
    ::Func:: Handles taxonomy search box
    """
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
                taxonomy = Stock.objects.filter(
                    pedigree=pedigree,
                    passport__taxonomy__population__contains=starts_with).values(
                    'pedigree', 'passport__taxonomy__population', 'passport__taxonomy__species').distinct()
                taxonomy_list = list(chain(taxonomy, taxonomy_list))
            for t in taxonomy_list:
                t['input'] = '<input type="checkbox" name="checkbox_taxonomy" value="%s">' % (
                    t['passport__taxonomy__population'])
        else:
            taxonomy_list = list(
                Taxonomy.objects.filter(population__contains=starts_with, common_name='Maize').values('population',
                                                                                                      'species').distinct())
            for t in taxonomy_list:
                t['input'] = '<input type="checkbox" name="checkbox_taxonomy" value="%s">' % (t['population'])
                t['passport__taxonomy__population'] = t['population']
                t['passport__taxonomy__species'] = t['species']
                t['pedigree'] = ''
    return JsonResponse({'data': taxonomy_list})


def show_all_isolatestock_taxonomy(request):
    isolatestock_taxonomy_list = []
    if request.session.get('checkbox_isolatestock_disease', None):
        checkbox_isolatestock_disease = request.session.get('checkbox_isolatestock_disease')
        for disease_id in checkbox_isolatestock_disease:
            taxonomy = IsolateStock.objects.filter(disease_info__id=disease_id).values('passport__taxonomy__id', 'disease_info__common_name', 'passport__taxonomy__genus', 'passport__taxonomy__alias', 'passport__taxonomy__race', 'passport__taxonomy__subtaxa', 'passport__taxonomy__species').distinct()
            isolatestock_taxonomy_list = list(chain(taxonomy, isolatestock_taxonomy_list))
        for p in isolatestock_taxonomy_list:
            p['input'] = '<input type="checkbox" name="checkbox_isolatestock_taxonomy_id" value="%s">' % (p['passport__taxonomy__id'])
    else:
        isolatestock_taxonomy_list = list(Taxonomy.objects.filter(common_name='IsolateStock').values('id', 'genus', 'alias', 'race', 'subtaxa', 'species').distinct())
        for t in isolatestock_taxonomy_list:
            t['input'] = '<input type="checkbox" name="checkbox_isolatestock_taxonomy_id" value="%s">' % (t['id'])
            t['disease_info__common_name'] = ''
            t['passport__taxonomy__genus'] = t['genus']
            t['passport__taxonomy__alias'] = t['alias']
            t['passport__taxonomy__race'] = t['race']
            t['passport__taxonomy__subtaxa'] = t['subtaxa']
            t['passport__taxonomy__species'] = t['species']
    return JsonResponse({'data':isolatestock_taxonomy_list})


def isolatestock_data_from_experiment(request, experiment_name):
    context = RequestContext(request)
    context_dict = {}
    isolatestock_data = find_isolatestock_for_experiment(experiment_name)
    context_dict['isolatestock_data'] = isolatestock_data
    context_dict['experiment_name'] = experiment_name
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/isolatestock/isolatestock_from_experiment.html', context_dict, context)


def find_isolatestock_for_experiment(experiment_name):
    try:
        isolatestock_data = ObsTracker.objects.filter(experiment__name=experiment_name, obs_entity_type='isolatestock')
    except ObsTracker.DoesNotExist:
        isolatestock_data = None
    return isolatestock_data


@login_required
def update_isolatestock_info(request, isolatestock_id):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        obs_tracker_isolatestock_form = LogIsolateStocksOnlineForm(data=request.POST)
        if obs_tracker_isolatestock_form.is_valid():
            # context_dict['form'] = obs_tracker_isolatestock_form
            # return render_to_response('lab/test.html', context_dict, context)
            with transaction.atomic():
                try:
                    obs_tracker = ObsTracker.objects.get(obs_entity_type='isolatestock', isolatestock_id=isolatestock_id, experiment=obs_tracker_isolatestock_form.cleaned_data['experiment'])
                    obs_tracker.glycerol_stock_id = 1
                    obs_tracker.maize_sample_id = 1
                    obs_tracker.obs_extract_id = 1
                    obs_tracker.locality = obs_tracker_isolatestock_form.cleaned_data['isolatestock__locality']
                    obs_tracker.field = obs_tracker_isolatestock_form.cleaned_data['field']
                    if obs_tracker_isolatestock_form.cleaned_data['obs_dna__dna_id'] != '':
                        obs_tracker.obs_dna = ObsDNA.objects.get(dna_id=obs_tracker_isolatestock_form.cleaned_data['obs_dna__dna_id'])
                    else:
                        obs_tracker.obs_dna = ObsDNA.objects.get(dna_id='No DNA')
                    if obs_tracker_isolatestock_form.cleaned_data['obs_microbe__microbe_id'] != '':
                        obs_tracker.obs_microbe = ObsMicrobe.objects.get(microbe_id=obs_tracker_isolatestock_form.cleaned_data['obs_microbe__microbe_id'])
                    else:
                        obs_tracker.obs_microbe = ObsMicrobe.objects.get(microbe_id='No Microbe')
                    if obs_tracker_isolatestock_form.cleaned_data['obs_row__row_id'] != '':
                        obs_tracker.obs_row = ObsRow.objects.get(row_id=obs_tracker_isolatestock_form.cleaned_data['obs_row__row_id'])
                    else:
                        obs_tracker.obs_row = ObsRow.objects.get(row_id='No Row')
                    if obs_tracker_isolatestock_form.cleaned_data['stock__seed_id'] != '':
                        obs_tracker.stock = Stock.objects.get(seed_id=obs_tracker_isolatestock_form.cleaned_data['stock__seed_id'])
                    else:
                        obs_tracker.stock = Stock.objects.get(seed_id='No Stock')
                    if obs_tracker_isolatestock_form.cleaned_data['obs_plant__plant_id'] != '':
                        obs_tracker.obs_plant = ObsPlant.objects.get(plant_id=obs_tracker_isolatestock_form.cleaned_data['obs_plant__plant_id'])
                    else:
                        obs_tracker.obs_plant = ObsPlant.objects.get(plant_id='No Plant')
                    if obs_tracker_isolatestock_form.cleaned_data['obs_tissue__tissue_id'] != '':
                        obs_tracker.obs_tissue = ObsTissue.objects.get(tissue_id=obs_tracker_isolatestock_form.cleaned_data['obs_tissue__tissue_id'])
                    else:
                        obs_tracker.obs_tissue = ObsTissue.objects.get(tissue_id='No Tissue')
                    if obs_tracker_isolatestock_form.cleaned_data['obs_culture__culture_id'] != '':
                        obs_tracker.obs_culture = ObsCulture.objects.get(culture_id=obs_tracker_isolatestock_form.cleaned_data['obs_culture__culture_id'])
                    else:
                        obs_tracker.obs_culture = ObsCulture.objects.get(culture_id='No Culture')
                    if obs_tracker_isolatestock_form.cleaned_data['obs_plate__plate_id'] != '':
                        obs_tracker.obs_plate = ObsPlate.objects.get(plate_id=obs_tracker_isolatestock_form.cleaned_data['obs_plate__plate_id'])
                    else:
                        obs_tracker.obs_plate = ObsPlate.objects.get(plate_id='No Plate')
                    if obs_tracker_isolatestock_form.cleaned_data['obs_well__well_id'] != '':
                        obs_tracker.obs_well = ObsWell.objects.get(well_id=obs_tracker_isolatestock_form.cleaned_data['obs_well__well_id'])
                    else:
                        obs_tracker.obs_well = ObsWell.objects.get(well_id='No Well')

                    isolatestock = IsolateStock.objects.get(id=isolatestock_id)
                    isolatestock.isolatestock_id = obs_tracker_isolatestock_form.cleaned_data['isolatestock__isolatestock_id']
                    isolatestock.isolatestock_name = obs_tracker_isolatestock_form.cleaned_data['isolatestock__isolatestock_name']
                    isolatestock.disease_info = obs_tracker_isolatestock_form.cleaned_data['isolatestock__disease_info']
                    isolatestock.plant_organ = obs_tracker_isolatestock_form.cleaned_data['isolatestock__plant_organ']
                    isolatestock.comments = obs_tracker_isolatestock_form.cleaned_data['isolatestock__comments']
                    isolatestock.locality = obs_tracker_isolatestock_form.cleaned_data['isolatestock__locality']
                    updated_taxonomy, created = Taxonomy.objects.get_or_create(genus=obs_tracker_isolatestock_form.cleaned_data['isolatestock__passport__taxonomy__genus'], species='', population='', common_name='IsolateStock', alias=obs_tracker_isolatestock_form.cleaned_data['isolatestock__passport__taxonomy__alias'], race=obs_tracker_isolatestock_form.cleaned_data['isolatestock__passport__taxonomy__race'], subtaxa=obs_tracker_isolatestock_form.cleaned_data['isolatestock__passport__taxonomy__subtaxa'])
                    updated_passport, created = Passport.objects.get_or_create(collecting=isolatestock.passport.collecting, people=isolatestock.passport.people, taxonomy=updated_taxonomy)
                    isolatestock.passport = updated_passport
                    isolatestock.save()
                    obs_tracker.save()
                    context_dict['updated'] = True
                except Exception:
                    context_dict['failed'] = True
        else:
            print(obs_tracker_isolatestock_form.errors)
    else:
        isolatestock_data = ObsTracker.objects.filter(obs_entity_type='isolatestock', isolatestock_id=isolatestock_id).values('experiment', 'isolatestock__isolatestock_id', 'isolatestock__locality', 'field', 'obs_dna__dna_id', 'obs_microbe__microbe_id', 'obs_row__row_id', 'stock__seed_id', 'obs_plant__plant_id', 'obs_tissue__tissue_id', 'obs_culture__culture_id', 'obs_plate__plate_id', 'obs_well__well_id', 'isolatestock__isolatestock_name', 'isolatestock__disease_info', 'isolatestock__plant_organ', 'isolatestock__passport__taxonomy__genus', 'isolatestock__passport__taxonomy__alias', 'isolatestock__passport__taxonomy__race', 'isolatestock__passport__taxonomy__subtaxa', 'isolatestock__comments')
        obs_tracker_isolatestock_form = LogIsolateStocksOnlineForm(initial=isolatestock_data[0])
    context_dict['isolatestock_id'] = isolatestock_id
    context_dict['obs_tracker_isolatestock_form'] = obs_tracker_isolatestock_form
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/isolatestock/isolatestock_info_update.html', context_dict, context)


@login_required
def single_isolatestock_info(request, isolatestock_table_id):
    context = RequestContext(request)
    context_dict = {}
    try:
        isolatestock_info = IsolateStock.objects.get(id=isolatestock_table_id)
    except IsolateStock.DoesNotExist:
        isolatestock_info = None
    if isolatestock_info is not None:
        obs_tracker = get_obs_tracker('isolatestock_id', isolatestock_table_id)
    try:
        # Section where glycerol stocks are added
        associated_isolates = ObsTracker.objects.filter(isolatestock=isolatestock_info.id, obs_entity_type='glycerol_stock')
    except GlycerolStock.DoesNotExist:
        associated_isolates = None
    context_dict['isolatestock_info'] = isolatestock_info
    context_dict['obs_tracker'] = obs_tracker
    context_dict['associated_isolates'] = associated_isolates
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/isolatestock/isolatestock_info.html', context_dict, context)


def isolatestock_id_search(request):
    """
    ::url:: = seed_inventory/seed_id_search/
    ::func:: = Handles search box named `Search Seed Info`
    ::html:: = seed_id_search_list.html
    """
    context = RequestContext(request)
    context_dict = {}
    isolatestock_id_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    else:
        starts_with = request.POST['suggestion']
    if starts_with:
        # __icontains method calls for case insensitive search
        isolatestock_id_list = IsolateStock.objects.filter(isolatestock_id__icontains=starts_with)[:2000]
    else:
        isolatestock_id_list = None
        context_dict = checkbox_session_variable_check(request)
    context_dict['isolatestock_id_list'] = isolatestock_id_list
    return render_to_response('lab/isolatestock/isolatestock_id_search_list.html', context_dict, context)









