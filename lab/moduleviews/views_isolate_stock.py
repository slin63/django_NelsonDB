"""Handles views for the Isolate Stock pages. Templates stored in /templates/lab/isolatestock
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

from lab.forms import LogIsolatesOnlineForm
from lab.models import Passport, Stock, StockPacket, Taxonomy, ObsRow, ObsPlant, ObsWell, ObsCulture, ObsTissue, ObsDNA, ObsPlate, ObsMicrobe, \
    ObsTracker, Isolate, Measurement, GlycerolStock
from lab.views import checkbox_session_variable_check, get_obs_tracker, get_obs_source, get_obs_measurements


def datatable_isolate_inventory(request):
    selected_isolates = checkbox_isolate_sort(request)
    #count = selected_isolates.count()
    arr = []
    for data in selected_isolates:
        arr.append({
            'input': '<input type="checkbox" name="checkbox_isolates" value="%s">'%(data.id),
            'id': data.id,
            'isolate_id': data.isolate_id,
            'isolate_name': data.isolate_name,
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


def checkbox_isolate_sort(request):
    selected_isolates = {}
    checkbox_taxonomy_list = []
    checkbox_disease_list = []
    if request.session.get('checkbox_isolate_taxonomy', None):
        checkbox_taxonomy_list = request.session.get('checkbox_isolate_taxonomy')
        if request.session.get('checkbox_isolate_disease', None):
            checkbox_disease_list = request.session.get('checkbox_isolate_disease')
            for disease_id in checkbox_disease_list:
                for taxonomy_id in checkbox_taxonomy_list:
                    isolates = Isolate.objects.filter(disease_info__id=disease_id, passport__taxonomy__id=taxonomy_id)
                    selected_isolates = list(chain(selected_isolates, isolates))
        else:
            for taxonomy_id in checkbox_taxonomy_list:
                isolates = Isolate.objects.filter(passport__taxonomy__id=taxonomy_id)
                selected_isolates = list(chain(selected_isolates, isolates))
    else:
        if request.session.get('checkbox_isolate_disease', None):
            checkbox_disease_list = request.session.get('checkbox_isolate_disease')
            for disease_id in checkbox_disease_list:
                isolates = Isolate.objects.filter(disease_info__id=disease_id)
                selected_isolates = list(chain(selected_isolates, isolates))
        else:
            selected_isolates = list(Isolate.objects.all().exclude(id=1))[:2000]
    return selected_isolates


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
def isolate_inventory(request):
    """
    ::url:: = /iso_inventory/ - To change
    ::func:: = Renders view for the seed inventory page
    ::html:: = seed_inventory.html
    """
    context = RequestContext(request)
    context_dict = {}
    context_dict = checkbox_session_variable_check(request)
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/isolatestock/isolate_inventory.html', context_dict, context)


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
    ::html:: = isolate_source_list.html, seed_inventory.html
    ::NOTES:: = Native cross functionality with Isolate Stock pages
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


def show_all_isolate_taxonomy(request):
    isolate_taxonomy_list = []
    if request.session.get('checkbox_isolate_disease', None):
        checkbox_isolate_disease = request.session.get('checkbox_isolate_disease')
        for disease_id in checkbox_isolate_disease:
            taxonomy = Isolate.objects.filter(disease_info__id=disease_id).values('passport__taxonomy__id', 'disease_info__common_name', 'passport__taxonomy__genus', 'passport__taxonomy__alias', 'passport__taxonomy__race', 'passport__taxonomy__subtaxa', 'passport__taxonomy__species').distinct()
            isolate_taxonomy_list = list(chain(taxonomy, isolate_taxonomy_list))
        for p in isolate_taxonomy_list:
            p['input'] = '<input type="checkbox" name="checkbox_isolate_taxonomy_id" value="%s">' % (p['passport__taxonomy__id'])
    else:
        isolate_taxonomy_list = list(Taxonomy.objects.filter(common_name='Isolate').values('id', 'genus', 'alias', 'race', 'subtaxa', 'species').distinct())
        for t in isolate_taxonomy_list:
            t['input'] = '<input type="checkbox" name="checkbox_isolate_taxonomy_id" value="%s">' % (t['id'])
            t['disease_info__common_name'] = ''
            t['passport__taxonomy__genus'] = t['genus']
            t['passport__taxonomy__alias'] = t['alias']
            t['passport__taxonomy__race'] = t['race']
            t['passport__taxonomy__subtaxa'] = t['subtaxa']
            t['passport__taxonomy__species'] = t['species']
    return JsonResponse({'data':isolate_taxonomy_list})


# def show_all_seedinv_pedigree(request):
#     """
#     ::func:: Not needed
#     """
#     pedigree_list = []
#     if request.session.get('checkbox_taxonomy', None):
#         checkbox_taxonomy_list = request.session.get('checkbox_taxonomy')
#         for taxonomy in checkbox_taxonomy_list:
#             pedigree = Stock.objects.filter(passport__taxonomy__population=taxonomy).values('pedigree',
#                                                                                             'passport__taxonomy__population').distinct()
#             pedigree_list = list(chain(pedigree, pedigree_list))
#         for p in pedigree_list:
#             p['input'] = '<input type="checkbox" name="checkbox_pedigree" value="%s">' % (p['pedigree'])
#     else:
#         pedigree_list = list(Stock.objects.all().values('pedigree', 'passport__taxonomy__population').distinct())
#         for p in pedigree_list:
#             p['input'] = '<input type="checkbox" name="checkbox_pedigree" value="%s">' % (p['pedigree'])
#     return JsonResponse({'data': pedigree_list})


# def show_all_seedinv_parameters(request):
#     """
#     ::func:: Not needed
#     """
#     parameter_list = []
#     if request.session.get('checkbox_taxonomy', None):
#         checkbox_taxonomy_list = request.session.get('checkbox_taxonomy')

#         if request.session.get('checkbox_pedigree', None):
#             checkbox_pedigree_list = request.session.get('checkbox_pedigree')
#             parameter_list_unique = []
#             parameter_names_unique = []
#             for taxonomy in checkbox_taxonomy_list:
#                 for pedigree in checkbox_pedigree_list:
#                     parameters = Measurement.objects.filter(obs_tracker__stock__passport__taxonomy__population=taxonomy,
#                                                             obs_tracker__stock__pedigree=pedigree).values(
#                         'measurement_parameter__parameter', 'measurement_parameter__protocol',
#                         'measurement_parameter__unit_of_measure').distinct()
#                     parameter_list = list(chain(parameters, parameter_list))
#             for p in parameter_list:
#                 if p['measurement_parameter__parameter'] not in parameter_names_unique:
#                     parameter_names_unique.append(p['measurement_parameter__parameter'])
#                     parameter_list_unique.append(
#                         {'measurement_parameter__parameter': p['measurement_parameter__parameter'],
#                          'measurement_parameter__protocol': p['measurement_parameter__protocol'],
#                          'measurement_parameter__unit_of_measure': p['measurement_parameter__unit_of_measure'],
#                          'input': '<input type="checkbox" name="checkbox_seedinv_parameters" value="%s">' % (
#                              p['measurement_parameter__parameter'])})
#             parameter_list = parameter_list_unique
#         else:
#             for taxonomy in checkbox_taxonomy_list:
#                 parameters = Measurement.objects.filter(
#                     obs_tracker__stock__passport__taxonomy__population=taxonomy).values(
#                     'measurement_parameter__parameter', 'measurement_parameter__protocol',
#                     'measurement_parameter__unit_of_measure').distinct()
#                 parameter_list = list(chain(parameters, parameter_list))
#             for p in parameter_list:
#                 p['input'] = '<input type="checkbox" name="checkbox_seedinv_parameters" value="%s">' % (
#                     p['measurement_parameter__parameter'])
#     elif request.session.get('checkbox_pedigree', None):
#         checkbox_pedigree_list = request.session.get('checkbox_pedigree')
#         for pedigree in checkbox_pedigree_list:
#             parameters = Measurement.objects.filter(obs_tracker__stock__pedigree=pedigree).values(
#                 'measurement_parameter__parameter', 'measurement_parameter__protocol',
#                 'measurement_parameter__unit_of_measure').distinct()
#             parameter_list = list(chain(parameters, parameter_list))
#         for p in parameter_list:
#             p['input'] = '<input type="checkbox" name="checkbox_seedinv_parameters" value="%s">' % (
#                 p['measurement_parameter__parameter'])
#     else:
#         parameter_list = list(
#             Measurement.objects.all().values('measurement_parameter__parameter', 'measurement_parameter__protocol',
#                                              'measurement_parameter__unit_of_measure').distinct())
#         for p in parameter_list:
#             p['input'] = '<input type="checkbox" name="checkbox_seedinv_parameters" value="%s">' % (
#                 p['measurement_parameter__parameter'])
#     return JsonResponse({'data': parameter_list})





# def sort_seed_set(set_type):
#     packet_data = []
#     if set_type == '282':
#         seed_set = ['811', '3316', '3811', '4226', '4722', 'A188', 'A214N', 'A239', 'A4415', 'A554', 'A556', 'A6',
#                     'A619', 'A632', 'A634', 'A635', 'A641', 'A654', 'A659', 'A661', 'A679', 'A680', 'A682', 'AB28A',
#                     'B10', 'B103', 'B104', 'B105', 'B109', 'B115', 'B14A', 'B164', 'B2', 'B37', 'B46', 'B52', 'B57',
#                     'B64', 'B68', 'B73', 'B73HTRHM', 'B75', 'B76', 'B77', 'B79', 'B84', 'B96', 'B97', 'C103', 'C123',
#                     'C49A', 'CH70130', 'CH9', 'CI1872', 'CI21E', 'CI28A', 'CI31A', 'CI3A', 'CI44', 'CI64', 'CI66',
#                     'CI7', 'CI90C', 'CI91B', 'CM105', 'CM174', 'CM37', 'CM7', 'CML10', 'CML103', 'CML108', 'CML11',
#                     'CML14', 'CML154Q', 'CML157Q', 'CML158Q', 'CML16', 'CML218', 'CML220', 'CML228', 'CML238', 'CML247',
#                     'CML254', 'CML258', 'CML261', 'CML264', 'CML277', 'CML281', 'CML287', 'CML311', 'CML314', 'CML321',
#                     'CML322', 'CML323', 'CML328', 'CML329', 'CML331', 'CML332', 'CML333', 'CML341', 'CML367', 'CML38',
#                     'CML40', 'CML45', 'CML48', 'CML5', 'CML52', 'CML56', 'CML61', 'CML69', 'CML9', 'CML91', 'CML92',
#                     'CMV3', 'CO106', 'CO109', 'CO125', 'CO255', 'D940Y', 'DE1', 'DE2', 'DE3', 'DE811', 'E2558W', 'EP1',
#                     'F2', 'F2834T', 'F44', 'F6', 'F7', 'FR1064', 'GA209', 'GE440', 'GT112', 'H100', 'H105W', 'H49',
#                     'H84', 'H91', 'H95', 'H99', 'HI27', 'HP301', 'HY', 'I137TN', 'I205', 'I29', 'IA2132', 'IA5125B',
#                     'IDS28', 'IDS69', 'IDS91', 'IL101T', 'IL14H', 'IL677A', 'K148', 'K4', 'K55', 'K64', 'KI11', 'KI14',
#                     'KI2007', 'KI2021', 'KI21', 'KI3', 'KI43', 'KI44', 'KUI2007', 'KY21', 'KY226', 'KY228', 'L317',
#                     'L578', 'M14', 'M162W', 'M37W', 'MO16W', 'MO17', 'MO18W', 'MO1W', 'MO24W', 'MO44', 'MO45', 'MO46',
#                     'MO47', 'MOG', 'MP313E', 'MP339', 'MP717', 'MS1334', 'MS153', 'MS71', 'MT42', 'N192', 'N28HT', 'N6',
#                     'N7A', 'NC222', 'NC230', 'NC232', 'NC236', 'NC238', 'NC250', 'NC250A', 'NC258', 'NC260', 'NC262',
#                     'NC264', 'NC268', 'NC290A', 'NC292', 'NC294', 'NC296', 'NC296A', 'NC298', 'NC300', 'NC302', 'NC304',
#                     'NC306', 'NC308', 'NC310', 'NC312', 'NC314', 'NC316', 'NC318', 'NC320', 'NC322', 'NC324', 'NC326',
#                     'NC328', 'NC33', 'NC330', 'NC332', 'NC334', 'NC336', 'NC338', 'NC340', 'NC342', 'NC344', 'NC346',
#                     'NC348', 'NC350', 'NC352', 'NC354', 'NC356', 'NC358', 'NC360', 'NC362', 'NC364', 'NC366', 'NC368',
#                     'NC370', 'NC372', 'ND246', 'OH40B', 'OH43', 'OH43E', 'OH603', 'OH7B', 'OS420', 'P39', 'PA762',
#                     'PA875', 'PA880', 'PA91', 'R109B', 'R168', 'R177', 'R229', 'R4', 'SA24', 'SC213R', 'SC357', 'SC55',
#                     'SD40', 'SD44', 'SG1533', 'SG18', 'T232', 'T234', 'T8', 'TX303', 'TX601', 'TZI10', 'TZI11', 'TZI16',
#                     'TZI18', 'TZI25', 'TZI8', 'TZI9', 'U267Y', 'VA102', 'VA14', 'VA17', 'VA22', 'VA26', 'VA35', 'VA59',
#                     'VA85', 'VA99', 'VAW6', 'W117HT', 'W153R', 'W182B', 'W22', 'W401', 'W64A', 'WF9', 'YU796NS']
#     if set_type == '282_jenny_subset':
#         seed_set = ['B105', 'B115', 'B75', 'M14', 'VA35', 'B97', 'IL677A', 'VA99', 'NC330', 'B109', 'MO44', 'MO46',
#                     'B104', 'NC260', 'W22', 'A680', 'B14A', 'HY', 'NC310', 'PA91', 'N7A', 'H100', 'NC308', 'MO1W',
#                     'VA102', 'H49', 'NC250', 'A659', 'IDS69', 'B2', 'I205', 'N28HT', 'NC364', 'B73', 'PA762', 'PA880',
#                     'VAW6', 'IDS28', 'K55', 'NC372', 'VA85', 'C103', 'HP301', 'NC290A', 'NC342', 'NC326', 'NC328',
#                     'B77', 'B79', 'H95', 'NC362', 'B84', 'SG18', 'B46', 'B73HTRHM', 'GE440', 'MO45', 'NC314', 'H91',
#                     'K148', 'NC264', 'R4', 'NC316', 'DE1', 'VA22', '3316', 'NC294', 'DE811', 'NC306']
#     seed_data = Stock.objects.filter(pedigree__in=seed_set)
#     for seed in seed_data:
#         seed_packets = StockPacket.objects.filter(stock_id=seed.id)
#         packet_data = list(chain(seed_packets, packet_data))
#     return packet_data


# @login_required
# def seed_set_download(request, set_type):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="seed_inventory_set.csv"'
#     packet_data = sort_seed_set(set_type)
#     writer = csv.writer(response)
#     writer.writerow(
#         ['Seed ID', 'Seed Name', 'Pedigree', 'Cross Type', 'Stock Status', 'Stock Date', 'Inoculated', 'Stock Comments',
#          'Weight(g)', 'Num Seeds', 'Packet Comments', 'Location Name', 'Building Name', 'Room', 'Shelf', 'Column',
#          'BoxName', 'Location Comments'])
#     for row in packet_data:
#         writer.writerow(
#             [row.stock.seed_id, row.stock.seed_name, row.stock.pedigree, row.stock.cross_type, row.stock.stock_status,
#              row.stock.stock_date, row.stock.inoculated, row.stock.comments, row.weight, row.num_seeds, row.comments,
#              row.location.location_name, row.location.building_name, row.location.room, row.location.shelf,
#              row.location.column, row.location.box_name, row.location.comments])
#     return response


@login_required
def update_isolate_info(request, isolate_id):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        obs_tracker_isolate_form = LogIsolatesOnlineForm(data=request.POST)
        if obs_tracker_isolate_form.is_valid():
            with transaction.atomic():
                try:
                    obs_tracker = ObsTracker.objects.get(obs_entity_type='isolate', isolate_id=isolate_id, experiment=obs_tracker_isolate_form.cleaned_data['experiment'])
                    obs_tracker.glycerol_stock_id = 1
                    obs_tracker.maize_sample_id = 1
                    obs_tracker.obs_extract_id = 1
                    obs_tracker.location = obs_tracker_isolate_form.cleaned_data['location']
                    obs_tracker.field = obs_tracker_isolate_form.cleaned_data['field']
                    if obs_tracker_isolate_form.cleaned_data['obs_dna__dna_id'] != '':
                        obs_tracker.obs_dna = ObsDNA.objects.get(dna_id=obs_tracker_isolate_form.cleaned_data['obs_dna__dna_id'])
                    else:
                        obs_tracker.obs_dna = ObsDNA.objects.get(dna_id='No DNA')
                    if obs_tracker_isolate_form.cleaned_data['obs_microbe__microbe_id'] != '':
                        obs_tracker.obs_microbe = ObsMicrobe.objects.get(microbe_id=obs_tracker_isolate_form.cleaned_data['obs_microbe__microbe_id'])
                    else:
                        obs_tracker.obs_microbe = ObsMicrobe.objects.get(microbe_id='No Microbe')
                    if obs_tracker_isolate_form.cleaned_data['obs_row__row_id'] != '':
                        obs_tracker.obs_row = ObsRow.objects.get(row_id=obs_tracker_isolate_form.cleaned_data['obs_row__row_id'])
                    else:
                        obs_tracker.obs_row = ObsRow.objects.get(row_id='No Row')
                    if obs_tracker_isolate_form.cleaned_data['stock__seed_id'] != '':
                        obs_tracker.stock = Stock.objects.get(seed_id=obs_tracker_isolate_form.cleaned_data['stock__seed_id'])
                    else:
                        obs_tracker.stock = Stock.objects.get(seed_id='No Stock')
                    if obs_tracker_isolate_form.cleaned_data['obs_plant__plant_id'] != '':
                        obs_tracker.obs_plant = ObsPlant.objects.get(plant_id=obs_tracker_isolate_form.cleaned_data['obs_plant__plant_id'])
                    else:
                        obs_tracker.obs_plant = ObsPlant.objects.get(plant_id='No Plant')
                    if obs_tracker_isolate_form.cleaned_data['obs_tissue__tissue_id'] != '':
                        obs_tracker.obs_tissue = ObsTissue.objects.get(tissue_id=obs_tracker_isolate_form.cleaned_data['obs_tissue__tissue_id'])
                    else:
                        obs_tracker.obs_tissue = ObsTissue.objects.get(tissue_id='No Tissue')
                    if obs_tracker_isolate_form.cleaned_data['obs_culture__culture_id'] != '':
                        obs_tracker.obs_culture = ObsCulture.objects.get(culture_id=obs_tracker_isolate_form.cleaned_data['obs_culture__culture_id'])
                    else:
                        obs_tracker.obs_culture = ObsCulture.objects.get(culture_id='No Culture')
                    if obs_tracker_isolate_form.cleaned_data['obs_plate__plate_id'] != '':
                        obs_tracker.obs_plate = ObsPlate.objects.get(plate_id=obs_tracker_isolate_form.cleaned_data['obs_plate__plate_id'])
                    else:
                        obs_tracker.obs_plate = ObsPlate.objects.get(plate_id='No Plate')
                    if obs_tracker_isolate_form.cleaned_data['obs_well__well_id'] != '':
                        obs_tracker.obs_well = ObsWell.objects.get(well_id=obs_tracker_isolate_form.cleaned_data['obs_well__well_id'])
                    else:
                        obs_tracker.obs_well = ObsWell.objects.get(well_id='No Well')

                    isolate = Isolate.objects.get(id=isolate_id)
                    isolate.isolate_id = obs_tracker_isolate_form.cleaned_data['isolate__isolate_id']
                    isolate.isolate_name = obs_tracker_isolate_form.cleaned_data['isolate__isolate_name']
                    isolate.disease_info = obs_tracker_isolate_form.cleaned_data['isolate__disease_info']
                    isolate.plant_organ = obs_tracker_isolate_form.cleaned_data['isolate__plant_organ']
                    isolate.comments = obs_tracker_isolate_form.cleaned_data['isolate__comments']
                    updated_taxonomy, created = Taxonomy.objects.get_or_create(genus=obs_tracker_isolate_form.cleaned_data['isolate__passport__taxonomy__genus'], species='', population='', common_name='Isolate', alias=obs_tracker_isolate_form.cleaned_data['isolate__passport__taxonomy__alias'], race=obs_tracker_isolate_form.cleaned_data['isolate__passport__taxonomy__race'], subtaxa=obs_tracker_isolate_form.cleaned_data['isolate__passport__taxonomy__subtaxa'])
                    updated_passport, created = Passport.objects.get_or_create(collecting=isolate.passport.collecting, people=isolate.passport.people, taxonomy=updated_taxonomy)
                    isolate.passport = updated_passport
                    isolate.save()
                    obs_tracker.save()
                    context_dict['updated'] = True
                except Exception:
                    context_dict['failed'] = True
        else:
            print(obs_tracker_isolate_form.errors)
    else:
        isolate_data = ObsTracker.objects.filter(obs_entity_type='isolate', isolate_id=isolate_id).values('experiment', 'isolate__isolate_id', 'location', 'field', 'obs_dna__dna_id', 'obs_microbe__microbe_id', 'obs_row__row_id', 'stock__seed_id', 'obs_plant__plant_id', 'obs_tissue__tissue_id', 'obs_culture__culture_id', 'obs_plate__plate_id', 'obs_well__well_id', 'isolate__isolate_name', 'isolate__disease_info', 'isolate__plant_organ', 'isolate__passport__taxonomy__genus', 'isolate__passport__taxonomy__alias', 'isolate__passport__taxonomy__race', 'isolate__passport__taxonomy__subtaxa', 'isolate__comments')
        obs_tracker_isolate_form = LogIsolatesOnlineForm(initial=isolate_data[0])
    context_dict['isolate_id'] = isolate_id
    context_dict['obs_tracker_isolate_form'] = obs_tracker_isolate_form
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/isolate_info_update.html', context_dict, context)


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
def single_isolate_info(request, isolate_table_id):
    context = RequestContext(request)
    context_dict = {}
    try:
        isolate_info = Isolate.objects.get(id=isolate_table_id)
    except Isolate.DoesNotExist:
        isolate_info = None
    if isolate_info is not None:
        obs_tracker = get_obs_tracker('isolate_id', isolate_table_id)
    try:
        # Section where glycerol stocks are added
        isolates = ObsTracker.objects.filter(isolate=isolate_info.id, obs_entity_type='glycerol_stock')
    except GlycerolStock.DoesNotExist:
        isolates = None
    context_dict['isolate_info'] = isolate_info
    context_dict['obs_tracker'] = obs_tracker
    context_dict['assocated_isolates'] = isolates
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/isolatestock/isolate_info.html', context_dict, context)


def isolate_id_search(request):
    """
    ::url:: = seed_inventory/seed_id_search/
    ::func:: = Handles search box named `Search Seed Info`
    ::html:: = seed_id_search_list.html
    """
    context = RequestContext(request)
    context_dict = {}
    isolate_id_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    else:
        starts_with = request.POST['suggestion']
    if starts_with:
        isolate_id_list = Isolate.objects.filter(isolate_id__contains=starts_with)[:2000]
    else:
        isolate_id_list = None
        context_dict = checkbox_session_variable_check(request)
    context_dict['isolate_id_list'] = isolate_id_list
    return render_to_response('lab/isolatestock/isolate_id_search_list.html', context_dict, context)









