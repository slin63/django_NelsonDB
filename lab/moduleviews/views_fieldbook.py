import os, tempfile, zipfile
import csv
import loader_scripts
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from lab.models import UserProfile, Experiment, Passport, Stock, StockPacket, Taxonomy, People, Collecting, Field, Locality, Location, ObsPlot, ObsPlant, ObsSample, ObsEnv, ObsWell, ObsCulture, ObsTissue, ObsDNA, ObsPlate, ObsMicrobe, ObsExtract, ObsTracker, ObsTrackerSource, IsolateStock, DiseaseInfo, Measurement, MeasurementParameter, Treatment, UploadQueue, Medium, Citation, Publication, MaizeSample, Separation, Isolate, FileDump
from lab.forms import UserForm, UserProfileForm, ChangePasswordForm, EditUserForm, EditUserProfileForm, NewExperimentForm, LogSeedDataOnlineForm, LogStockPacketOnlineForm, LogPlantsOnlineForm, LogPlotsOnlineForm, LogEnvironmentsOnlineForm, LogSamplesOnlineForm, LogMeasurementsOnlineForm, NewTreatmentForm, UploadQueueForm, LogSeedDataOnlineForm, LogStockPacketOnlineForm, NewFieldForm, NewLocalityForm, NewMeasurementParameterForm, NewLocationForm, NewDiseaseInfoForm, NewTaxonomyForm, NewMediumForm, NewCitationForm, UpdateSeedDataOnlineForm, LogTissuesOnlineForm, LogCulturesOnlineForm, LogMicrobesOnlineForm, LogDNAOnlineForm, LogPlatesOnlineForm, LogWellOnlineForm, LogIsolateStocksOnlineForm, LogSeparationsOnlineForm, LogMaizeSurveyOnlineForm, LogIsolatesOnlineForm, FileDumpForm, UpdateIsolatesOnlineForm, UpdateStockPacketOnlineForm
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
from django.core.files import File
from django.http import JsonResponse
from django.utils.encoding import smart_str
from django.core.servers.basehttp import FileWrapper
from django.conf import settings
import mimetypes
import json

def upload_online(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('lab/fieldbook/field_book_upload.html', context_dict, context)
