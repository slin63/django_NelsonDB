
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from lab.models import Primer, MapFeature, MapFeatureInterval, Marker, MapFeatureAnnotation, MeasurementParameter, QTL, MapFeatureExpression
from lab.forms import FileDumpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect
from itertools import chain
from django.forms.models import inlineformset_factory
from django.forms.formsets import formset_factory
from django.conf import settings
from django.db.models import F
from django import template
from django.template.defaulttags import register
from operator import itemgetter
from django.db import transaction
from django.http import JsonResponse


@login_required
def genotype_data_browse(request):
	context = RequestContext(request)
	context_dict = {}

	context_dict['logged_in_user'] = request.user.username
	return render_to_response('lab/genotype/browse.html', context_dict, context)

def genotype_data_browse_plot(request):
    context = RequestContext(request)
    context_dict = {}
    all_qtl = QTL.objects.all().exclude(id=1)
    all_markers = Marker.objects.all().exclude(id=1)
    all_expression = MapFeatureExpression.objects.all()

    data = []

    for q in all_qtl:
        data.append({'position':q.map_feature_interval.map_feature_start.physical_position, 'chromosome':q.map_feature_interval.map_feature_start.chromosome, 'name':'%s Start'%(q.parameter), 'type':'QTL'})
        data.append({'position':q.map_feature_interval.map_feature_end.physical_position, 'chromosome':q.map_feature_interval.map_feature_end.chromosome, 'name':'%s End'%(q.parameter), 'type':'QTL'})
    for m in all_markers:
        data.append({'position':m.marker_map_feature.physical_position, 'chromosome':m.marker_map_feature.chromosome, 'name':m.marker_id, 'type':'Marker'})
        #data.append({'position':m.map_feature_interval.map_feature_start.physical_position, 'chromosome':m.map_feature_interval.map_feature_start.chromosome, 'name':'%s Start'%(m.marker_id), 'type':'MarkerR'})
        #data.append({'position':m.map_feature_interval.map_feature_end.physical_position, 'chromosome':m.map_feature_interval.map_feature_end.chromosome, 'name':'%s End'%(m.marker_id), 'type':'MarkerR'})
    for e in all_expression:
        data.append({'position':e.map_feature_interval.map_feature_start.physical_position, 'chromosome':e.map_feature_interval.map_feature_start.chromosome, 'name':'%s Start Value: %s'%(e.parameter, e.value), 'type':'Expression'})
        data.append({'position':e.map_feature_interval.map_feature_end.physical_position, 'chromosome':e.map_feature_interval.map_feature_end.chromosome, 'name':'%s End Value: %s'%(e.parameter, e.value), 'type':'Expression'})

    return JsonResponse({'data':data}, safe=True)
