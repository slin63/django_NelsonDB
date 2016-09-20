from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from lab.forms import UploadManagerForm as UpForm
import csv

@login_required
def upload_manager(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict['user'] = request.user.username
    context_dict['logged_in_user'] = request.user.username

    if not request.user.is_superuser:
        return HttpResponse("Superuser restricted view")

    if request.method == 'POST':
        form = UpForm(request.POST)

        if form.is_valid():

            if form.cleaned_data['lab_key'] == settings.LAB_KEY:
                batch = form.cleaned_data['upload_batch']
                batch.justification = form.cleaned_data['justification']

                if form.cleaned_data['action'] == 'delete' and form.cleaned_data['confirmed'] and bool(form.cleaned_data['justification']):
                    batch.del_objs()

                    print "{} called DELETION of {} OBJECTS for REASON: {}\n{}\n{}\n{}".format(
                        request.user.username, len(batch), batch.justification, '-x'*40, batch.objs, '-x'*40
                    )

                    context_dict['form'] = UpForm()
                    context_dict['success'] = "{} objects successfully deleted!".format(len(batch))

                elif form.cleaned_data['action'] == 'preview':
                    return csv_from_upload_batch(batch)

                else:

                    context_dict['form'] = UpForm()
                    context_dict['errors'] = "Improper form or incorrect lab key! Fill out all the fields if you're deleting something."



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


def csv_from_upload_batch(upload_batch):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s.csv"' % (upload_batch)

    models = upload_batch.objs
    header = models[0].__dict__.keys()

    header.remove('_state')

    writer = csv.DictWriter(response, fieldnames=header)
    writer.writeheader()
    for model in models:
        info = model.__dict__
        model.__dict__.pop('_state', None)

        writer.writerow(info)

    return response
