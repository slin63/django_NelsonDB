from django.conf.urls import patterns, url
from legacy import views

urlpatterns = patterns('',
    url(r'^legacy_seed_inventory/$', views.legacy_seed_inv, name='legacy_seed_inventory'),)
