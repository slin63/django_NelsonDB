from django.conf.urls import patterns, url
from legacy import views

urlpatterns = patterns('',
    url(r'^legacy_seed_inventory/$', views.checkbox_legacy_seed_inv, name='checkbox_legacy_seed_inv'),
    url(r'^legacy_seed_inventory/row/(?P<legacy_row>.+)/(?P<legacy_seed>.+)/$', views.select_legacy_row, name='select_legacy_row'),
    url(r'^select_legacy_experiment/$', views.checkbox_selected_legacy_experiment, name='checkbox_selected_legacy_experiment'),
    url(r'^select_legacy_pedigree/$', views.checkbox_selected_legacy_pedigree, name='checkbox_selected_legacy_pedigree'),
    url(r'^checkbox_suggest_legacy_experiment/$', views.checkbox_suggest_legacy_experiment, name='checkbox_suggest_legacy_experiment'),
    url(r'^checkbox_suggest_legacy_pedigree/$', views.checkbox_suggest_legacy_pedigree, name='checkbox_suggest_legacy_pedigree'),
    url(r'^legacy_seed_inventory/checkbox_clear/(?P<clear_selected>\w+)/$', views.checkbox_legacy_inventory_clear, name='checkbox_legacy_inventory_clear'),
)
