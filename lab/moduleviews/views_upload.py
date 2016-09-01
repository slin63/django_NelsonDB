import csv
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import transaction
from itertools import chain
from openpyxl.writer.excel import save_virtual_workbook

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

    if request.method == 'GET':
        form = UpForm()

    context_dict['form'] = form
    return render_to_response("lab/upload_manager/upload_manager_form.html", context_dict, context)
