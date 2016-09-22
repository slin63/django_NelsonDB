import csv
import sys
import json
import mimetypes
from os import path, listdir
from datetime import datetime
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.servers.basehttp import FileWrapper
from django.db import transaction
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from itertools import chain
from operator import itemgetter


from lab.forms import UserForm, UserProfileForm, ChangePasswordForm, EditUserForm, EditUserProfileForm, \
    NewExperimentForm, \
    LogPlantsOnlineForm, LogPlotsOnlineForm, LogEnvironmentsOnlineForm, LogSamplesOnlineForm, LogMeasurementsOnlineForm, \
    NewTreatmentForm, UploadQueueForm, LogSeedDataOnlineForm, LogStockPacketOnlineForm, NewFieldForm, NewLocalityForm, \
    NewMeasurementParameterForm, NewLocationForm, NewDiseaseInfoForm, NewTaxonomyForm, NewMediumForm, NewCitationForm, \
    UpdateSeedDataOnlineForm, LogTissuesOnlineForm, LogCulturesOnlineForm, LogMicrobesOnlineForm, LogDNAOnlineForm, \
    LogPlatesOnlineForm, LogWellOnlineForm, LogIsolateStocksOnlineForm, LogSeparationsOnlineForm, \
    LogMaizeSurveyOnlineForm, LogIsolatesOnlineForm, FileDumpForm, UpdateIsolatesOnlineForm, UpdateStockPacketOnlineForm, UpdatePlotsOnlineForm
from lab.models import UserProfile, Experiment, Passport, Stock, StockPacket, Taxonomy, People, Collecting, Field, \
    Locality, Location, ObsPlot, ObsPlant, ObsSample, ObsEnv, ObsWell, ObsCulture, ObsTissue, ObsDNA, ObsPlate, \
    ObsMicrobe, ObsExtract, ObsTracker, ObsTrackerSource, IsolateStock, DiseaseInfo, Measurement, MeasurementParameter, \
    Treatment, UploadQueue, Medium, Citation, Publication, MaizeSample, Separation, Isolate, FileDump

# Clean up imports in pycharm later

@login_required
def new_treatment(request):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        new_treatment_form = NewTreatmentForm(data=request.POST)
        if new_treatment_form.is_valid():
            new_treatment_exp = new_treatment_form.cleaned_data['experiment']
            new_treatment_id = new_treatment_form.cleaned_data['treatment_id']
            new_treatment_type = new_treatment_form.cleaned_data['treatment_type']
            new_treatment_date = new_treatment_form.cleaned_data['date']
            new_treatment_comments = new_treatment_form.cleaned_data['comments']
            new_treatment = Treatment.objects.get_or_create(experiment=new_treatment_exp, treatment_id=new_treatment_id,
                                                            treatment_type=new_treatment_type, date=new_treatment_date,
                                                            comments=new_treatment_comments)

            treatment_added = True
        else:
            print(new_treatment_form.errors)
            treatment_added = False
    else:
        new_treatment_form = NewTreatmentForm()
        treatment_added = False

    treatments = Treatment.objects.exclude(id=1)

    context_dict['treatment_data'] = treatments
    context_dict['new_treatment_form'] = new_treatment_form
    context_dict['treatment_added'] = treatment_added
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/treatment/new_treatment.html', context_dict, context)
