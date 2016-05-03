from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from lab.models import UserProfile, Experiment, Passport, Stock, StockPacket, Taxonomy, People, Collecting, Field, \
    Locality, Location, ObsPlot, ObsPlant, ObsSample, ObsEnv, ObsWell, ObsCulture, ObsTissue, ObsDNA, ObsPlate, \
    ObsMicrobe, ObsExtract, ObsTracker, ObsTrackerSource, IsolateStock, DiseaseInfo, Measurement, MeasurementParameter, \
    Treatment, UploadQueue, Medium, Citation, Publication, MaizeSample, Separation, Isolate, FileDump
from lab.forms import UserForm, UserProfileForm, ChangePasswordForm, EditUserForm, EditUserProfileForm, \
    NewExperimentForm, LogSeedDataOnlineForm, LogStockPacketOnlineForm, LogPlantsOnlineForm, LogRowsOnlineForm, \
    LogEnvironmentsOnlineForm, LogSamplesOnlineForm, LogMeasurementsOnlineForm, NewTreatmentForm, UploadQueueForm, \
    LogSeedDataOnlineForm, LogStockPacketOnlineForm, NewFieldForm, NewLocalityForm, NewMeasurementParameterForm, \
    NewLocationForm, NewDiseaseInfoForm, NewTaxonomyForm, NewMediumForm, NewCitationForm, UpdateSeedDataOnlineForm, \
    LogTissuesOnlineForm, LogCulturesOnlineForm, LogMicrobesOnlineForm, LogDNAOnlineForm, LogPlatesOnlineForm, \
    LogWellOnlineForm, LogIsolateStocksOnlineForm, LogSeparationsOnlineForm, LogMaizeSurveyOnlineForm, \
    LogIsolatesOnlineForm, FileDumpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db.models import ObjectDoesNotExist


def about_people(request, people_selection):
    context = RequestContext(request)
    context_dict = {}
    if people_selection == 'all':
        people_all_button = True
        people_staff_button = None
        people_active_button = None
        people_collaborator_button = None
        users = User.objects.all().exclude(username='NULL').exclude(username='unknown_person').exclude(
            username='unknown')
        for user in users:
            try:
                user_profile = UserProfile.objects.get(user=user)
                user.job_title = user_profile.job_title
                user.picture = user_profile.picture
            except ObjectDoesNotExist:
                pass

    elif people_selection == 'staff':
        people_all_button = None
        people_staff_button = True
        people_active_button = None
        people_collaborator_button = None
        users = User.objects.filter(is_staff='1').exclude(username='NULL').exclude(username='unknown_person').exclude(
            username='unknown')
        for user in users:
            user_profile = UserProfile.objects.get(user=user)
            user.job_title = user_profile.job_title
            user.picture = user_profile.picture
    elif people_selection == 'active':
        people_all_button = None
        people_staff_button = None
        people_active_button = True
        people_collaborator_button = None
        users = User.objects.filter(is_active='1').exclude(username='NULL').exclude(username='unknown_person').exclude(
            username='unknown')
        for user in users:
            user_profile = UserProfile.objects.get(user=user)
            user.job_title = user_profile.job_title
            user.picture = user_profile.picture
    elif people_selection == 'collaborators':
        people_all_button = None
        people_staff_button = None
        people_active_button = None
        people_collaborator_button = True
        collaborators = []
        users = User.objects.filter(is_active='1').exclude(username='NULL').exclude(username='unknown_person').exclude(
            username='unknown')
        for user in users:
            user_profile = UserProfile.objects.get(user=user)
            if ('|Collaborator|' in user_profile.notes):
                user.job_title = user_profile.job_title
                user.picture = user_profile.picture
                collaborators.append(user)
        users = collaborators
    else:
        people_all_button = None
        people_staff_button = None
        people_active_button = None
        people_collaborator_button = None
        users = None
    context_dict['people_all_button'] = people_all_button
    context_dict['people_staff_button'] = people_staff_button
    context_dict['people_active_button'] = people_active_button
    context_dict['people_collaborator_button'] = people_collaborator_button
    context_dict['users'] = users
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


def about_help(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/help.html', context_dict, context)


def about_odk(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/odk.html', context_dict, context)


def about_collaborators(request):
    context = RequestContext(request)
    context_dict = {}
    collaborators = People.objects.all()
    context_dict['collaborators'] = collaborators
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/collaborators.html', context_dict, context)
