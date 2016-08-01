from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from lab.forms import FieldBookUploadForm
from lab.models import UploadQueue
from ..loader_scripts import *


@login_required
def field_book_upload_online(request):
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        sent = True
        upload_form = FieldBookUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            new_upload_user = upload_form.cleaned_data['user']
            new_upload_filename = upload_form.cleaned_data['file_name']
            new_upload_filetype = upload_form.cleaned_data['file_type'].model_class().__name__.lower()
            new_upload_verified = upload_form.cleaned_data['verified']
            upload_added = True

            if new_upload_filetype == 'measurement':
                results_dict = measurement_loader_prep(
                    upload_file=request.FILES['file_name'], user=new_upload_user, field_book_upload=True
                )
            else:
                results_dict = None

            if results_dict is not None:
                if new_upload_verified == False:
                    upload_complete = False

                    if new_upload_filetype == 'measurement':
                        output = measurement_loader_prep_output(
                            results_dict=results_dict, new_upload_exp='No Experiment', template_type=new_upload_filetype
                        )
                    else:
                        output = None
                    return output
                elif new_upload_verified == True:
                    if new_upload_filetype == 'measurement':
                        uploaded = measurement_loader(
                                results_dict=results_dict
                            )
                    else:
                        uploaded = False

                    if uploaded == True:
                        new_upload, created = UploadQueue.objects.get_or_create(
                            experiment_id=1, user=new_upload_user, file_name=new_upload_filename, upload_type=new_upload_filetype
                        )
                        new_upload.verified = new_upload_verified
                        new_upload.completed = True
                        new_upload.save()
                        upload_complete = True
                    else:
                        upload_complete = False
                else:
                    upload_complete = False
            else:
                upload_complete = False
        else:
            print(upload_form.errors)
            upload_added = False
            upload_complete = False
    else:
        sent = False
        upload_form = FieldBookUploadForm()
        upload_added = False
        upload_complete = False

    context_dict['upload_form'] = upload_form
    context_dict['upload_added'] = upload_added
    context_dict['upload_complete'] = upload_complete
    context_dict['sent'] = sent
    context_dict['logged_in_user'] = request.user.username
    return render_to_response('lab/fieldbook/field_book_upload.html', context_dict, context)
