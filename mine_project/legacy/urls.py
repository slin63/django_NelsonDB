from django.conf.urls import patterns, url
from legacy import views

urlpatterns = patterns('',
    url(r'^legacy_seed_inventory/$', views.legacy_seed_inv, name='legacy_seed_inventory'),
    url(r'^suggest_legacy_pedigree/$', views.suggest_legacy_pedigree, name='suggest_legacy_pedigree'),)
