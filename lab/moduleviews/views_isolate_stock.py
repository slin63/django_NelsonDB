"""Handles views for the IsolateStock pages. Templates stored in /templates/lab/isolatestock
Details at: https://docs.google.com/document/d/1IVkC0RxJe-P1xGAM4WMGCjp5JYcFlRtQj5PGvZNpAJA/edit"""

import csv
import csv
import json
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db import transaction
from django.http import HttpResponse
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import RequestContext
from itertools import chain
from itertools import chain

from lab.forms import LogIsolateStocksOnlineForm
from lab.models import Passport, Stock, StockPacket, Taxonomy, ObsRow, ObsPlant, ObsWell, ObsCulture, ObsTissue, ObsDNA, ObsPlate, ObsMicrobe, \
    ObsTracker, IsolateStock, Measurement, GlycerolStock
from lab.views import checkbox_session_variable_check, get_obs_tracker, get_obs_source, get_obs_measurements


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


# def unique_selected_stocks(selected_stocks):
#     """
#     ::url:: = None
#     ::func:: = Contacts OBS tracker and makes sure stocks in a passed list are only
#     parsed by datatable_seed_inventory once
#     ::html:: = None
#     """
#     unique_seed_id = []
#     unique_stock_list = []
#     for s in selected_stocks:
#         if s.obs_tracker.stock.seed_id not in unique_seed_id:
#             unique_seed_id.append(s.obs_tracker.stock.seed_id)
#             unique_stock_list.append({'id': s.obs_tracker.stock_id, 'seed_id': s.obs_tracker.stock.seed_id,
#                                       'cross_type': s.obs_tracker.stock.cross_type,
#                                       'pedigree': s.obs_tracker.stock.pedigree,
#                                       'population': s.obs_tracker.stock.passport.taxonomy.population,
#                                       'stock_status': s.obs_tracker.stock.stock_status,
#                                       'collector': s.obs_tracker.stock.passport.collecting.user.username,
#                                       'comments': s.obs_tracker.stock.comments})
#     return unique_stock_list


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


# def select_pedigree(request):
#     """
#     ::url:: = /seed_inventory/select_pedigree/ - To change
#     ::func:: = Supporting function for the pedigree search table in seed_inventory
#     ::ajax:: = $('#select_pedigree_form_submit')
#     ::html:: = Used in seed_inventory.html
#     """
#     pedigrees = request.POST['pedigrees']
#     pedigree_list = json.loads(pedigrees)
#     request.session['checkbox_pedigree'] = pedigree_list
#     return JsonResponse({'success': True})


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


# def select_seedinv_parameters(request):
#     """
#     ::url:: = seed_inventory/select_parameters/$
#     ::func:: = Supporting function for the parameter search table in seed_inventory
#     ::ajax:: = $('#select_seedinv_parameters_form_submit')
#     ::html:: = seed_inventory.html
#     """
#     parameters = request.POST['parameters']
#     parameters_list = json.loads(parameters)
#     request.session['checkbox_seedinv_parameters'] = parameters_list
#     return JsonResponse({'success': True})


# def select_stockpacket_from_stock(request):
#     """
#     ::url:: seed_inventory/select_stocks/
#     ::func:: Deprecated, replaced by upload_online, log_data_online,
#     ::html:: stock.html
#     """
#     context = RequestContext(request)
#     context_dict = {}
#     selected_packets = []
#     checkbox_stock_list = request.POST.getlist('checkbox_stock')
#     request.session['checkbox_stock'] = checkbox_stock_list
#     for stock in checkbox_stock_list:
#         packet = StockPacket.objects.filter(stock__id=stock)
#         selected_packets = list(chain(packet, selected_packets))
#     context_dict = checkbox_session_variable_check(request)
#     context_dict['selected_packets'] = selected_packets
#     context_dict['logged_in_user'] = request.user.username
#     return render_to_response('lab/isolatestock/stock.html', context_dict, context)


# def suggest_pedigree(request):
#     """
#     ::func:: deprecated
#     """
#     pedigree_list = []
#     starts_with = ''
#     if request.method == 'GET':
#         starts_with = request.GET.get('suggestion', False)
#     else:
#         starts_with = request.POST.get('suggestion', False)
#     if starts_with:
#         if request.session.get('checkbox_taxonomy', None):
#             checkbox_taxonomy_list = request.session.get('checkbox_taxonomy')
#             for taxonomy in checkbox_taxonomy_list:
#                 pedigree = Stock.objects.filter(
#                     pedigree__contains=starts_with,
#                     passport__taxonomy__population=taxonomy).values('pedigree','passport__taxonomy__population').distinct()
#                 pedigree_list = list(chain(pedigree, pedigree_list))
#             for p in pedigree_list:
#                 p['input'] = '<input type="checkbox" name="checkbox_pedigree" value="%s">' % (p['pedigree'])
#         else:
#             pedigree_list = list(Stock.objects.filter(pedigree__contains=starts_with).values(
#                 'pedigree', 'passport__taxonomy__population').distinct())
#             for p in pedigree_list:
#                 p['input'] = '<input type="checkbox" name="checkbox_pedigree" value="%s">' % (p['pedigree'])
#     return JsonResponse({'data': pedigree_list})


def suggest_taxonomy(request):
    """
    ::Deprecated::
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


# def seedinv_suggest_parameters(request):
#     """
#     ::func:: Not needed
#     """
#     parameter_list = []
#     starts_with = ''
#     if request.method == 'GET':
#         starts_with = request.GET.get('suggestion', False)
#     else:
#         starts_with = request.POST.get('suggestion', False)
#     if starts_with:
#         if request.session.get('checkbox_taxonomy', None):
#             checkbox_taxonomy_list = request.session.get('checkbox_taxonomy')
#             if request.session.get('checkbox_pedigree', None):
#                 checkbox_pedigree_list = request.session.get('checkbox_pedigree')
#                 parameter_list_unique = []
#                 parameter_names_unique = []
#                 for taxonomy in checkbox_taxonomy_list:
#                     for pedigree in checkbox_pedigree_list:
#                         parameters = Measurement.objects.filter(measurement_parameter__parameter__contains=starts_with,
#                                                                 obs_tracker__stock__passport__taxonomy__population=taxonomy,
#                                                                 obs_tracker__stock__pedigree=pedigree).values(
#                             'measurement_parameter__parameter', 'measurement_parameter__protocol',
#                             'measurement_parameter__unit_of_measure').distinct()
#                         parameter_list = list(chain(parameters, parameter_list))
#                 for p in parameter_list:
#                     if p['measurement_parameter__parameter'] not in parameter_names_unique:
#                         parameter_names_unique.append(p['measurement_parameter__parameter'])
#                         parameter_list_unique.append(
#                             {'measurement_parameter__parameter': p['measurement_parameter__parameter'],
#                              'measurement_parameter__protocol': p['measurement_parameter__protocol'],
#                              'measurement_parameter__unit_of_measure': p['measurement_parameter__unit_of_measure'],
#                              'input': '<input type="checkbox" name="checkbox_seedinv_parameters" value="%s">' % (
#                                  p['measurement_parameter__parameter'])})
#                 parameter_list = parameter_list_unique
#             else:
#                 for taxonomy in checkbox_taxonomy_list:
#                     parameters = Measurement.objects.filter(measurement_parameter__parameter__contains=starts_with,
#                                                             obs_tracker__stock__passport__taxonomy__population=taxonomy).values(
#                         'measurement_parameter__parameter', 'measurement_parameter__protocol',
#                         'measurement_parameter__unit_of_measure').distinct()
#                     parameter_list = list(chain(parameters, parameter_list))
#                 for p in parameter_list:
#                     p['input'] = '<input type="checkbox" name="checkbox_seedinv_parameters" value="%s">' % (
#                         p['measurement_parameter__parameter'])
#         elif request.session.get('checkbox_pedigree', None):
#             checkbox_pedigree_list = request.session.get('checkbox_pedigree')
#             for pedigree in checkbox_pedigree_list:
#                 parameters = Measurement.objects.filter(measurement_parameter__parameter__contains=starts_with,
#                                                         obs_tracker__stock__pedigree=pedigree).values(
#                     'measurement_parameter__parameter', 'measurement_parameter__protocol',
#                     'measurement_parameter__unit_of_measure').distinct()
#                 parameter_list = list(chain(parameters, parameter_list))
#             for p in parameter_list:
#                 p['input'] = '<input type="checkbox" name="checkbox_seedinv_parameters" value="%s">' % (
#                     p['measurement_parameter__parameter'])
#         else:
#             parameter_list = list(
#                 Measurement.objects.filter(measurement_parameter__parameter__contains=starts_with).values(
#                     'measurement_parameter__parameter', 'measurement_parameter__protocol',
#                     'measurement_parameter__unit_of_measure').distinct())
#             for p in parameter_list:
#                 p['input'] = '<input type="checkbox" name="checkbox_seedinv_parameters" value="%s">' % (
#                     p['measurement_parameter__parameter'])
#     return JsonResponse({'data': parameter_list})


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


# @login_required
# def single_stock_info(request, stock_id):
#     """
#     ::url:: = stock/(?P<stock_id>\d+)
#     ::func:: = Renders tables for stock information and for related stock packets
#     ::html:: = stock_info.html
#     """
#     context = RequestContext(request)
#     context_dict = {}
#     obs_tracker_seed = []
#     try:
#         stock_info = Stock.objects.get(id=stock_id)
#     except Stock.DoesNotExist:
#         stock_info = None
#     if stock_info is not None:
#         obs_tracker = get_obs_tracker('stock_id', stock_id)
#         for t in obs_tracker:
#             if t.obs_id != stock_info.seed_id:
#                 obs_tracker_seed.append(t)
#         obs_source = get_obs_source('stock_id', stock_id)
#         obs_measurements = get_obs_measurements('stock_id', stock_id)
#         measured_parameters = {}
#         for mp in obs_measurements:
#             if mp.measurement_parameter_id not in measured_parameters:
#                 measured_parameters[mp.measurement_parameter_id] = mp.measurement_parameter.parameter
#     else:
#         obs_tracker = None
#         obs_source = None
#         obs_measurements = None
#         measured_parameters = None
#     try:
#         # Section where stockpackets are added
#         stock_packets = StockPacket.objects.filter(stock_id=stock_id)
#     except StockPacket.DoesNotExist:
#         stock_packets = None
#     context_dict['stock_info'] = stock_info
#     context_dict['obs_tracker'] = obs_tracker_seed
#     context_dict['obs_source'] = obs_source
#     context_dict['obs_measurements'] = obs_measurements
#     context_dict['stock_packets'] = stock_packets
#     context_dict['measured_parameters'] = measured_parameters
#     context_dict['logged_in_user'] = request.user.username
#     return render_to_response('lab/stock_info.html', context_dict, context)


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
        isolatestock_id_list = IsolateStock.objects.filter(isolatestock_id__contains=starts_with)[:2000]
    else:
        isolatestock_id_list = None
        context_dict = checkbox_session_variable_check(request)
    context_dict['isolatestock_id_list'] = isolatestock_id_list
    return render_to_response('lab/isolatestock/isolatestock_id_search_list.html', context_dict, context)









