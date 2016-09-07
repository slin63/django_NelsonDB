from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import transaction

from applets import field_map_generator
from lab.forms import UploadManagerForm as UpForm

# Clean imports in pycharm later

@login_required
def upload_manager(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict['user'] = request.user.username

    if not request.user.is_superuser:
        return HttpResponse("Superuser restricted view")

    if request.method == 'POST':
        form = UpForm(request.POST)

        if form.is_valid():

            print form.cleaned_data

            if form.cleaned_data['lab_key'] == settings.LAB_KEY and form.cleaned_data['confirmed']:
                batch = form.cleaned_data['upload_batch']
                batch.justification = form.cleaned_data['justification']
                batch.del_objs()

                print "{} called DELETION of {} OBJECTS for REASON: {}\n{}\n{}\n{}".format(
                    request.user.username, len(batch), batch.justification, '-x'*40, batch.objs, '-x'*40
                )

                context_dict['form'] = UpForm()
                context_dict['success'] = "{} objects successfully deleted!".format(len(batch))

            else:
                context_dict['errors'] = "Improper form or incorrect lab key!"
                context_dict['form'] = UpForm()

        else:
            context_dict['errors'] = "Improper form or incorrect lab key!"
            context_dict['form'] = UpForm()


    elif request.method == 'GET':
        form = UpForm()
        context_dict['form'] = form

    return render_to_response("lab/upload_manager/upload_manager_form.html", context_dict, context)
