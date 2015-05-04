from django.conf.urls import patterns, url
from legacy import views

urlpatterns = patterns('',
    url(r'^experiment/$', views.legacy_experiment, name='legacy_experiment'),
    url(r'^markers/$', views.legacy_markers, name='legacy_markers'),
    url(r'^seed/$', views.legacy_seed, name='legacy_seed'),
    url(r'^row/$', views.legacy_row, name='legacy_row'),
    url(r'^genotype/$', views.legacy_genotype, name='legacy_genotype'),
    url(r'^tissue/$', views.legacy_tissue, name='legacy_tissue'),

    url(r'^legacy_seed_inventory/$', views.checkbox_legacy_seed_inv, name='checkbox_legacy_seed_inv'),
    url(r'^legacy_seed_inventory/row/(?P<legacy_row>.+)/(?P<legacy_seed>.+)/$', views.select_legacy_row, name='select_legacy_row'),
    url(r'^select_legacy_experiment/$', views.checkbox_selected_legacy_experiment, name='checkbox_selected_legacy_experiment'),
    url(r'^select_legacy_pedigree/$', views.checkbox_selected_legacy_pedigree, name='checkbox_selected_legacy_pedigree'),
    url(r'^checkbox_suggest_legacy_experiment/$', views.checkbox_suggest_legacy_experiment, name='checkbox_suggest_legacy_experiment'),
    url(r'^checkbox_suggest_legacy_pedigree/$', views.checkbox_suggest_legacy_pedigree, name='checkbox_suggest_legacy_pedigree'),
    url(r'^legacy_seed_inventory/checkbox_clear/(?P<clear_selected>\w+)/$', views.checkbox_legacy_inventory_clear, name='checkbox_legacy_inventory_clear'),
)
