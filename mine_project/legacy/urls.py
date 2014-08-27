from django.conf.urls import patterns, url
from legacy import views

urlpatterns = patterns('',
    url(r'^legacy_seed_inventory/$', views.legacy_seed_inv, name='legacy_seed_inventory'),
    url(r'^legacy_seed_inventory/pedigree/(?P<legacy_pedigree>.+)/$', views.select_legacy_pedigree, name='select_legacy_pedigree'),
    url(r'^legacy_seed_inventory/row/(?P<legacy_row>.+)/$', views.select_legacy_row, name='select_legacy_row'),
    url(r'^legacy_seed_inventory/experiment/(?P<legacy_experiment>\w+)/$', views.select_legacy_experiment, name='select_legacy_experiment'),
    url(r'^legacy_seed_inventory/stock/(?P<legacy_stock>\w+)/$', views.select_legacy_stock, name='select_legacy_stock'),
    url(r'^suggest_legacy_pedigree/$', views.suggest_legacy_pedigree, name='suggest_legacy_pedigree'),
    url(r'^suggest_legacy_experiment/$', views.suggest_legacy_experiment, name='suggest_legacy_experiment'),
    url(r'^legacy_seed_inventory/clear/(?P<clear_selected>\w+)/$', views.legacy_inventory_clear, name='legacy_inventory_clear'),)
