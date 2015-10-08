
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
    all_qtl = QTL.objects.all()
    all_markers = Marker.objects.all()

    qtl_list = []
    markers_list = []
    expression_list = []

    for q in all_qtl:
        qtl_list.append([q.map_feature_interval.map_feature_start.physical_position, q.map_feature_interval.map_feature_start.chromosome, '%s Start'%(q.parameter)])
        qtl_list.append([q.map_feature_interval.map_feature_end.physical_position, q.map_feature_interval.map_feature_end.chromosome, '%s End'%(q.parameter)])
    for m in all_markers:
        markers_list.append([m.marker_map_feature.physical_position, m.marker_map_feature.chromosome, m.marker_id])

    return JsonResponse({'qtl':qtl_list, 'markers':markers_list, 'expression':expression_list}, safe=True)
