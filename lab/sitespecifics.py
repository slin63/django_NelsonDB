from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings


def sitespecifics(request):
    context_data = dict()
    context_data['site_name'] = settings.SITE_NAME
    return context_data
