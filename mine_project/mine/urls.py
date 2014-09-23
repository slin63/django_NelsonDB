from django.conf.urls import patterns, url
from mine import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
		url(r'^about/$', views.about, name='about'),
		url(r'^error_prelim/$', views.error_prelim, name='error_prelim'),
		url(r'^add_category/$', views.add_category, name='add_category'),
		url(r'^category/(?P<category_name_url>\w+)/add_page/$', views.add_page, name='add_page'),
		url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
		url(r'^experiment/(?P<experiment_name_url>\w+)/$', views.experiment, name='experiment'),
		url(r'^register/$', views.register, name='register'),
		url(r'^login/$', views.user_login, name='login'),
		url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^change_password/$', views.profile_change_password, name ='profile_change_password'),
    url(r'^edit_profile/$', views.edit_profile, name ='edit_profile'),
		url(r'^profile/(?P<profile_name>\w+)/$', views.profile, name ='profile'),
		url(r'^goto/$', views.track_url, name='track_url'),
		url(r'^like_category/$', views.like_category, name='like_category'),
    url(r'^seed_inventory/$', views.seed_inventory, name='seed_inventory'),
    url(r'^seed_inventory/locality/(?P<locality_id>\w+)/$', views.seed_inventory_select_locality, name='seed_inventory_select_locality'),
    url(r'^seed_inventory/field/(?P<field_id>\w+)/$', views.seed_inventory_select_field, name='seed_inventory_select_field'),
    url(r'^seed_inventory/passport/(?P<passport_id>\w+)/$', views.seed_inventory_select_passport, name='seed_inventory_select_passport'),
    url(r'^seed_inventory/collection/(?P<collecting_id>\w+)/$', views.seed_inventory_select_collection, name='seed_inventory_select_collection'),
    url(r'^seed_inventory/taxonomy/(?P<taxonomy_id>\w+)/$', views.seed_inventory_select_taxonomy, name='seed_inventory_select_taxonomy'),
    url(r'^seed_inventory/source/(?P<source_id>\w+)/$', views.seed_inventory_select_source, name='seed_inventory_select_source'),
    url(r'^seed_inventory/stock/(?P<stock_id>\w+)/$', views.seed_inventory_select_stock, name='seed_inventory_select_stock'),
    url(r'^suggest_pedigree/$', views.suggest_pedigree, name='choose_pedigree'),
    url(r'^suggest_locality/$', views.suggest_locality, name='choose_locality'),
    url(r'^suggest_field/$', views.suggest_field, name='choose_field'),
    url(r'^suggest_source/$', views.suggest_source, name='suggest_source'),
    url(r'^suggest_taxonomy/$', views.suggest_taxonomy, name='suggest_taxonomy'),
    url(r'^suggest_collecting/$', views.suggest_collecting, name='suggest_collecting'),
    url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
    url(r'^suggest_experiment/$', views.suggest_experiment, name='suggest_experiment'),
    url(r'^seed_inventory/clear/(?P<clear_selected>\w+)/$', views.seed_inventory_clear, name='seed_inventory_clear'))
