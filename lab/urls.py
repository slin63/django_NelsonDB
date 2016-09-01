from django.conf.urls import patterns, url

from lab import views
from lab.moduleviews import views_genotype, views_about, views_plot, views_fieldbook, views_packet, views_upload
from lab.moduleviews import views_isolate_stock as views_is

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/goals/$', views_about.about_goals, name='about_goals'),
                       url(r'^about/help/$', views_about.about_help, name='about_help'),
                       url(r'^about/collaborators/$', views_about.about_collaborators, name='about_collaborators'),
                       url(r'^about/people/(?P<people_selection>\w+)/$', views_about.about_people, name='about_people'),
                       url(r'^about/literature/$', views_about.about_literature, name='about_literature'),
                       url(r'^about/odk/$', views_about.about_odk, name='about_odk'),

                       url(r'^error_prelim/$', views.error_prelim, name='error_prelim'),
                       url(r'^file_storage/$', views.file_storage, name='file_storage'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^change_password/$', views.profile_change_password, name ='profile_change_password'),
                       url(r'^edit_profile/$', views.edit_profile, name ='edit_profile'),
                       url(r'^goto/$', views.track_url, name='track_url'),
                       url(r'^site_map/$', views.site_map, name='site_map'),
                       url(r'^sidebar_search_results/$', views.sidebar_search_page, name='sidebar_search_page'),
                       url(r'^sidebar_search/$', views.sidebar_search, name='sidebar_search'),
                       url(r'^checkbox_clear/(?P<clear_selected>\w+)/$', views.checkbox_clear, name='checkbox_clear'),

                       url(r'^experiment/(?P<experiment_name_url>\w+)/$', views.experiment, name='experiment'),
                       url(r'^experiment_edit/(?P<experiment_id>\d+)/$', views.experiment_edit, name='experiment_edit'),
                       url(r'^profile/(?P<profile_name>\w+)/$', views.profile, name ='profile'),

                       url(r'^field_book/upload/$', views_fieldbook.field_book_upload_online, name ='fieldbook_upload'),

                       url(r'^datatable/isolate_inventory/$', views.datatable_isolate_inventory, name='datatable_isolate_inventory'),
                       url(r'^isolate/$', views.isolate_inventory, name='isolate_inventory'),
                       url(r'^isolate/update/(?P<isolate_id>\d+)/$', views.update_isolate_info, name='update_isolate_info'),
                       url(r'^isolate/(?P<isolate_table_id>\d+)/$', views.single_isolate_info, name='single_isolate_info'),
                       url(r'^data/isolate_delete/$', views_is.isolate_delete, name='isolate_delete'),

                       url(r'^datatable/seed_inventory/$', views.datatable_seed_inventory, name='datatable_seed_inventory'),
                       url(r'^seed_inventory/$', views.seed_inventory, name='seed_inventory'),
                       url(r'^seed_inventory/select_pedigree/$', views.select_pedigree, name='select_pedigree'),
                       url(r'^seed_inventory/select_taxonomy/$', views.select_taxonomy, name='select_taxonomy'),
                       url(r'^seed_inventory/select_stocks/$', views.select_stockpacket_from_stock, name='select_stockpacket_from_stock'),
                       url(r'^seed_inventory/select_parameters/$', views.select_seedinv_parameters, name='select_seedinv_parameters'),
                       url(r'^seed_inventory/suggest_pedigree/$', views.suggest_pedigree, name='suggest_pedigree'),
                       url(r'^seed_inventory/suggest_taxonomy/$', views.suggest_taxonomy, name='suggest_taxonomy'),
                       url(r'^seed_inventory/suggest_parameters/$', views.seedinv_suggest_parameters, name='seedinv_suggest_parameters'),
                       url(r'^seed_inventory/show_all_taxonomy/$', views.show_all_seedinv_taxonomy, name='show_all_seedinv_taxonomy'),
                       url(r'^seed_inventory/show_all_pedigree/$', views.show_all_seedinv_pedigree, name='show_all_seedinv_pedigree'),
                       url(r'^seed_inventory/show_all_parameters/$', views.show_all_seedinv_parameters, name='show_all_seedinv_parameters'),
                       url(r'^seed_inventory/seed_id_search/$', views.seed_id_search, name='seed_id_search'),
                       url(r'^seed_inventory/set/(?P<set_type>\w+)/$', views.seed_set_download, name='seed_set_download'),
                       url(r'^seed_inventory/update/(?P<stock_id>\d+)/$', views.update_seed_info, name='update_seed_info'),
                       url(r'^seed_inventory/packet_update/(?P<stock_id>\d+)/$', views.update_seed_packet_info, name='update_seed_packet_info'),

                       url(r'^seed_inventory/generate_packets/(?P<experiment_id>\d+)/$', views_packet.generate_packet_dataframe, name='generate_packets'),
                       url(r'^seed_inventory/generate_packets/$', views_packet.packet_menu, name='packet_menu'),


                       # Added 2/15/2016 - slin63
                       url(r'^datatable/isolatestock_inventory/$', views_is.datatable_isolatestock_inventory, name='datatable_isolatestock_inventory'),
                       url(r'^data/isolatestock_delete/$', views_is.isolatestock_delete, name='isolatestock_delete'),
                       url(r'^isolatestock_inventory/$', views_is.isolatestock_inventory, name='isolatestock_inventory'),
                       url(r'^isolatestock_inventory/select_taxonomy/$', views_is.select_taxonomy, name='select_taxonomy'),
                       url(r'^isolatestock_inventory/show_all_taxonomy/$', views_is.show_all_isolatestock_taxonomy, name='show_all_iso_taxonomy'),
                       url(r'^isolatestock_inventory/isolatestock_id_search/$', views_is.isolatestock_id_search, name='isolatestock_id_search'),
                       url(r'^isolatestock_inventory/update/(?P<isolatestock_id>\d+)/$', views_is.update_isolatestock_info, name='update_isolatestock_info'),
                       url(r'^isolatestock_inventory/select_isolatestocks/$', views_is.select_isolatestocks, name='select_isolatestocks'),
                       url(r'^isolatestock/(?P<isolatestock_table_id>\d+)/$', views_is.single_isolatestock_info, name='single_isolatestock_info'),
                       url(r'^isolatestock_inventory/suggest_isolatestock_taxonomy/$', views_is.suggest_isolatestock_taxonomy, name='suggest_isolatestock_taxonomy'),
                       url(r'^isolatestock_inventory/suggest_isolatestock_disease/$', views.suggest_isolatestock_disease, name='suggest_isolatestock_disease'),
                       url(r'^isolatestock_inventory/select_isolatestock_disease/$', views.select_isolatestock_disease, name='select_isolatestock_disease'),
                       url(r'^isolatestock_inventory/select_isolatestock_taxonomy/$', views.select_isolatestock_taxonomy, name='select_isolatestock_taxonomy'),
                       url(r'^isolatestock_inventory/show_all_disease/$', views.show_all_isolatestock_disease, name='show_all_isolatestock_disease'),

                       url(r'^data/medium/$', views.browse_medium_data, name='browse_medium_data'),
                       url(r'^data/measurement_parameter/$', views.browse_parameter_data, name='browse_parameter_data'),
                       url(r'^data/location/$', views.browse_location_data, name='browse_location_data'),
                       url(r'^data/locality/$', views.browse_locality_data, name='browse_locality_data'),
                       url(r'^data/field/$', views.browse_field_data, name='browse_field_data'),
                       url(r'^data/disease_info/$', views.browse_disease_info_data, name='browse_disease_info_data'),
                       url(r'^data/taxonomy/$', views.browse_taxonomy_data, name='browse_taxonomy_data'),
                       url(r'^data/publication/$', views.browse_publication_data, name='browse_publication_data'),
                       url(r'^data/downloads/$', views.browse_downloads, name='browse_downloads'),

                       url(r'^data/stock/measurement/plot/$', views.stock_page_measurement_plot, name='stock_page_measurement_plot'),
                       url(r'^data/stock_delete/$', views.stock_delete, name='stock_delete'),
                       url(r'^data/stock/(?P<experiment_name>\w+)/$', views.stock_for_experiment, name='stock_for_experiment'),
                       url(r'^data/stockpackets/(?P<experiment_name>\w+)/$', views.stockpackets_for_experiment, name='stockpackets_for_experiment'),
                       url(r'^data/stock/collected/(?P<experiment_name>\w+)/$', views.stock_collected_from_experiment, name='stock_collected_from_experiment'),
                       url(r'^data/stockpackets/collected/(?P<experiment_name>\w+)/$', views.stockpackets_collected_from_experiment, name='stockpackets_collected_from_experiment'),

                       url(r'^datatable/measurement_data/$', views.datatable_measurement_data, name='datatable_measurement_data'),
                       url(r'^data/measurement/$', views.measurement_data_browse, name='measurement_data_browse'),
                       url(r'^data/measurement_delete/(?P<measurement_id>\w+)/$', views.measurement_delete, name='measurement_data_delete'),
                       url(r'^data/measurement/suggest_measurement_experiment/$', views.suggest_measurement_experiment, name='suggest_measurement_experiment'),
                       url(r'^data/measurement/select_measurement_experiment/$', views.select_measurement_experiment, name='select_measurement_experiment'),
                       url(r'^data/measurement/suggest_measurement_parameter/$', views.suggest_measurement_parameter, name='suggest_measurement_parameter'),
                       url(r'^data/measurement/select_measurement_parameter/$', views.select_measurement_parameter, name='select_measurement_parameter'),
                       url(r'^data/measurement/show_all_experiment/$', views.show_all_measurement_experiment, name='show_all_measurement_experiment'),
                       url(r'^data/measurement/show_all_parameter/$', views.show_all_measurement_parameter, name='show_all_measurement_parameter'),
                       url(r'^data/measurement/(?P<experiment_name>\w+)/separations', views.separations_measurement_data_from_experiment, name='separations_measurement_data_from_experiment'),
                       url(r'^data/measurement/(?P<experiment_name>\w+)', views.measurement_data_from_experiment, name='measurement_data_from_experiment'),

                       url(r'^data/tissue/$', views.tissue_data_browse, name='tissue_data_browse'),
                       url(r'^data/tissue/suggest_tissue_experiment/$', views.suggest_tissue_experiment, name='suggest_tissue_experiment'),
                       url(r'^data/tissue/select_tissue_experiment/$', views.select_tissue_experiment, name='select_tissue_experiment'),
                       url(r'^data/tissue/show_all_experiment/$', views.show_all_tissue_experiment, name='show_all_tissue_experiment'),
                       url(r'^data/tissue/checkbox_clear/$', views.checkbox_tissue_data_clear, name='checkbox_tissue_data_clear'),
                       url(r'^data/tissue/(?P<experiment_name>\w+)/$', views.tissue_data_from_experiment, name='tissue_data_from_experiment'),

                       url(r'^data/plate/$', views.plate_data_browse, name='plate_data_browse'),
                       url(r'^data/plate/suggest_plate_experiment/$', views.suggest_plate_experiment, name='suggest_plate_experiment'),
                       url(r'^data/plate/select_plate_experiment/$', views.select_plate_experiment, name='select_plate_experiment'),
                       url(r'^data/plate/checkbox_clear/$', views.checkbox_plate_data_clear, name='checkbox_plate_data_clear'),
                       url(r'^data/plate/show_all_experiment/$', views.show_all_plate_experiment, name='show_all_plate_experiment'),
                       url(r'^data/plate/(?P<experiment_name>\w+)/$', views.plate_data_from_experiment, name='plate_data_from_experiment'),

                       url(r'^data/well/$', views.well_data_browse, name='well_data_browse'),
                       url(r'^data/well/suggest_well_experiment/$', views.suggest_well_experiment, name='suggest_well_experiment'),
                       url(r'^data/well/select_well_experiment/$', views.select_well_experiment, name='select_well_experiment'),
                       url(r'^data/well/checkbox_clear/$', views.checkbox_well_data_clear, name='checkbox_well_data_clear'),
                       url(r'^data/well/show_all_experiment/$', views.show_all_well_experiment, name='show_all_well_experiment'),
                       url(r'^data/well/(?P<experiment_name>\w+)/$', views.well_data_from_experiment, name='well_data_from_experiment'),

                       url(r'^data/plant/$', views.plant_data_browse, name='plant_data_browse'),
                       url(r'^data/plant/suggest_plant_experiment/$', views.suggest_plant_experiment, name='suggest_plant_experiment'),
                       url(r'^data/plant/select_plant_experiment/$', views.select_plant_experiment, name='select_plant_experiment'),
                       url(r'^data/plant/checkbox_clear/$', views.checkbox_plant_data_clear, name='checkbox_plant_data_clear'),
                       url(r'^data/plant/show_all_experiment/$', views.show_all_plant_experiment, name='show_all_plant_experiment'),
                       url(r'^data/plant/(?P<experiment_name>\w+)/$', views.plant_data_from_experiment, name='plant_data_from_experiment'),

                       url(r'^data/culture/$', views.culture_data_browse, name='culture_data_browse'),
                       url(r'^data/culture/suggest_culture_experiment/$', views.suggest_culture_experiment, name='suggest_culture_experiment'),
                       url(r'^data/culture/select_culture_experiment/$', views.select_culture_experiment, name='select_culture_experiment'),
                       url(r'^data/culture/show_all_experiment/$', views.show_all_culture_experiment, name='show_all_culture_experiment'),
                       url(r'^data/culture/checkbox_clear/$', views.checkbox_culture_data_clear, name='checkbox_culture_data_clear'),
                       url(r'^data/culture/(?P<experiment_name>\w+)/$', views.culture_data_from_experiment, name='culture_data_from_experiment'),

                       url(r'^data/dna/$', views.dna_data_browse, name='dna_data_browse'),
                       url(r'^data/dna/suggest_dna_experiment/$', views.suggest_dna_experiment, name='suggest_dna_experiment'),
                       url(r'^data/dna/select_dna_experiment/$', views.select_dna_experiment, name='select_dna_experiment'),
                       url(r'^data/dna/show_all_experiment/$', views.show_all_dna_experiment, name='show_all_dna_experiment'),
                       url(r'^data/dna/checkbox_clear/$', views.checkbox_dna_data_clear, name='checkbox_dna_data_clear'),
                       url(r'^data/dna/(?P<experiment_name>\w+)/$', views.dna_data_from_experiment, name='dna_data_from_experiment'),

                       url(r'^data/maize/$', views.maize_data_browse, name='maize_data_browse'),
                       url(r'^data/maize/suggest_maize_experiment/$', views.suggest_maize_experiment, name='suggest_maize_experiment'),
                       url(r'^data/maize/select_maize_experiment/$', views.select_maize_experiment, name='select_maize_experiment'),
                       url(r'^data/maize/show_all_experiment/$', views.show_all_maize_experiment, name='show_all_maize_experiment'),
                       url(r'^data/maize/checkbox_clear/$', views.checkbox_maize_data_clear, name='checkbox_maize_data_clear'),
                       url(r'^data/maize/(?P<experiment_name>\w+)/$', views.maize_data_from_experiment, name='maize_data_from_experiment'),

                       url(r'^data/microbe/$', views.microbe_data_browse, name='microbe_data_browse'),
                       url(r'^data/microbe/suggest_microbe_experiment/$', views.suggest_microbe_experiment, name='suggest_microbe_experiment'),
                       url(r'^data/microbe/select_microbe_experiment/$', views.select_microbe_experiment, name='select_microbe_experiment'),
                       url(r'^data/microbe/show_all_experiment/$', views.show_all_microbe_experiment, name='show_all_microbe_experiment'),
                       url(r'^data/microbe/checkbox_clear/$', views.checkbox_microbe_data_clear, name='checkbox_microbe_data_clear'),
                       url(r'^data/microbe/(?P<experiment_name>\w+)/$', views.microbe_data_from_experiment, name='microbe_data_from_experiment'),

                       url(r'^data/environment/$', views.env_data_browse, name='env_data_browse'),
                       url(r'^data/environment/suggest_env_experiment/$', views.suggest_env_experiment, name='suggest_env_experiment'),
                       url(r'^data/environment/select_env_experiment/$', views.select_env_experiment, name='select_env_experiment'),
                       url(r'^data/environment/show_all_experiment/$', views.show_all_env_experiment, name='show_all_env_experiment'),
                       url(r'^data/environment/checkbox_clear/$', views.checkbox_env_data_clear, name='checkbox_env_data_clear'),
                       url(r'^data/environment/(?P<experiment_name>\w+)/$', views.env_data_from_experiment, name='env_data_from_experiment'),

                       url(r'^data/isolatestocks/(?P<experiment_name>\w+)/$', views_is.isolatestock_data_from_experiment, name='isolatestock_data_from_experiment'),
                       url(r'^data/isolate/(?P<experiment_name>\w+)/$', views.isolate_data_from_experiment, name='isolate_data_from_experiment'),

                       url(r'^data/sample/$', views.sample_data_browse, name='sample_data_browse'),
                       url(r'^data/sample/suggest_sample_experiment/$', views.suggest_sample_experiment, name='suggest_sample_experiment'),
                       url(r'^data/sample/select_sample_experiment/$', views.select_sample_experiment, name='select_sample_experiment'),
                       url(r'^data/sample/show_all_experiment/$', views.show_all_sample_experiment, name='show_all_sample_experiment'),
                       url(r'^data/sample/checkbox_clear/$', views.checkbox_sample_data_clear, name='checkbox_sample_data_clear'),
                       url(r'^data/sample/(?P<experiment_name>\w+)/$', views.sample_data_from_experiment, name='sample_data_from_experiment'),

                       url(r'^data/separation/$', views.separation_data_browse, name='separation_data_browse'),
                       url(r'^data/separation/(?P<experiment_name>\w+)/$', views.separation_data_from_experiment, name='separation_data_from_experiment'),


                       url(r'^data/harvest_date/$', views_plot.add_harvest_date, name='harvest_date'),
                       url(r'^data/plot/$', views_plot.plot_loader_browse, name='plot_loader_browse'),
                       url(r'^data/plot/suggest_plot_experiment/$', views_plot.suggest_plot_experiment, name='suggest_plot_experiment'),
                       url(r'^data/plot/select_plot_experiment/$', views_plot.select_plot_experiment, name='select_plot_experiment'),
                       url(r'^data/plot/show_all_experiment/$', views_plot.show_all_plot_experiment, name='show_all_plot_experiment'),
                       url(r'^data/plot/checkbox_clear/$', views_plot.checkbox_plot_loader_clear, name='checkbox_plot_loader_clear'),
                       url(r'^data/plot/(?P<experiment_name>\w+)/$', views_plot.plot_loader_from_experiment, name='plot_loader_from_experiment'),

                       url(r'^data/genotype/$', views_genotype.genotype_data_browse, name='genotype_data_browse'),
                       url(r'^data/genotype/browse/plot/$', views_genotype.genotype_data_browse_plot, name='genotype_data_browse_plot'),

                       url(r'^inventory/passport/(?P<passport_id>\d+)/$', views.passport, name='passport'),
                       url(r'^disease_info/(?P<disease_id>\d+)/$', views.single_disease_info, name='single_disease_info'),
                       url(r'^field/(?P<field_id>\d+)/$', views.single_field_info, name='single_field_info'),
                       url(r'^stock/(?P<stock_id>\d+)/$', views.single_stock_info, name='single_stock_info'),
                       url(r'^plot/(?P<obs_plot_id>\d+)/$', views_plot.single_plot_info, name='single_plot_info'),
                       url(r'^plot/(?P<obs_plot_id>\d+)/update/$', views_plot.update_plot_info, name='plot_update'),

                       url(r'^plant/(?P<obs_plant_id>\d+)/$', views.single_plant_info, name='single_plant_info'),
                       url(r'^plate/(?P<obs_plate_id>\d+)/$', views.single_plate_info, name='single_plate_info'),
                       url(r'^well/(?P<obs_well_id>\d+)/$', views.single_well_info, name='single_well_info'),
                       url(r'^tissue/(?P<obs_tissue_id>\d+)/$', views.single_tissue_info, name='single_tissue_info'),
                       url(r'^dna/(?P<obs_dna_id>\d+)/$', views.single_dna_info, name='single_dna_info'),
                       url(r'^culture/(?P<obs_culture_id>\d+)/$', views.single_culture_info, name='single_culture_info'),
                       url(r'^measurement_parameter/(?P<parameter_id>\d+)/$', views.single_parameter_info, name='single_parameter_info'),
                       url(r'^medium/(?P<medium_id>\d+)/$', views.single_medium_info, name='single_medium_info'),
                       url(r'^location/(?P<location_id>\d+)/$', views.single_location_info, name='single_location_info'),
                       url(r'^locality/(?P<locality_id>\d+)/$', views.single_locality_info, name='single_locality_info'),
                       url(r'^taxonomy/(?P<taxonomy_id>\d+)/$', views.single_taxonomy_info, name='single_taxonomy_info'),
                       url(r'^maize/(?P<maize_id>\d+)/$', views.single_maize_info, name='single_maize_info'),
                       url(r'^sample/(?P<obs_sample_id>\d+)/$', views.single_sample_info, name='single_sample_info'),
                       url(r'^sample/update/(?P<obs_sample_id>\d+)/$', views.update_sample_info, name='update_sample_info'),
                       url(r'^extract/(?P<obs_extract_id>\d+)/$', views.single_extract_info, name='single_extract_info'),

                       url(r'^edit/(?P<obj_type>\w+)/(?P<obj_id>\d+)/$', views.edit_info, name='edit_info'),

                       url(r'^new_experiment/$', views.new_experiment, name='new_experiment'),
                       url(r'^new_treatment/$', views.new_treatment, name='new_treatment'),
                       url(r'^log_data/select_obs/$', views.log_data_select_obs, name='log_data_select_obs'),
                       url(r'^log_data/(?P<data_type>\w+)/$', views.log_data_online, name='log_data_online'),

                       url(r'^download/template/(?P<filename>\w+)/', views.serve_data_template_file, name='serve_data_template_file'),
                       url(r'^upload/(?P<data_type>\w+)/$', views.queue_upload_file, name='queue_upload_file'),

                       url(r'^upload_manager/$', views_upload.upload_manager, name='upload_manager'),



                       url(r'^download/measurement/(?P<experiment_name>\w+)/', views.download_measurement_experiment, name='download_measurement_experiment'),
                       url(r'^download/maize/(?P<experiment_name>\w+)/', views.download_maize_experiment, name='download_maize_experiment'),
                       url(r'^download/microbe/(?P<experiment_name>\w+)/', views.download_microbe_experiment, name='download_microbe_experiment'),
                       url(r'^download/plot/(?P<experiment_name>\w+)/', views_plot.download_plot_experiment, name='download_plot_experiment'),
                       url(r'^download/plot_field/(?P<field_id>\w+)/', views_plot.download_field_map_by_field, name='download_field_map_by_field'),

                       url(r'^download/fieldmap/(?P<experiment_name>\w+)/', views_plot.download_field_map_experiment, name='download_plot_experiment'),
                       url(r'^download/sample/(?P<experiment_name>\w+)/', views.download_sample_experiment, name='download_sample_experiment'),
                       url(r'^download/separation/(?P<experiment_name>\w+)/', views.download_separation_experiment, name='download_separation_experiment'),
                       url(r'^download/plate/(?P<experiment_name>\w+)/', views.download_plate_experiment, name='download_plate_experiment'),
                       url(r'^download/culture/(?P<experiment_name>\w+)/', views.download_culture_experiment, name='download_culture_experiment'),
                       url(r'^download/tissue/(?P<experiment_name>\w+)/', views.download_tissue_experiment, name='download_tissue_experiment'),
                       url(r'^download/well/(?P<experiment_name>\w+)/', views.download_well_experiment, name='download_well_experiment'),
                       url(r'^download/environment/(?P<experiment_name>\w+)/', views.download_env_experiment, name='download_env_experiment'),
                       url(r'^download/plant/(?P<experiment_name>\w+)/', views.download_plant_experiment, name='download_plant_experiment'),
                       url(r'^download/stock/used/(?P<experiment_name>\w+)/', views.download_stock_used_experiment, name='download_stock_used_experiment'),
                       url(r'^download/stock/collected/(?P<experiment_name>\w+)/', views.download_stock_collected_experiment, name='download_stock_collected_experiment'),
                       url(r'^download/stockpackets/used/(?P<experiment_name>\w+)/', views.download_stockpackets_for_experiment, name='download_seedpackets_for_experiment'),
                       url(r'^download/stockpackets/collected/(?P<experiment_name>\w+)/', views.download_stockpackets_collected_experiment, name='download_stockpackets_collected_experiment'),
                       url(r'^download/isolatestocks/(?P<experiment_name>\w+)/', views.download_isolatestocks_experiment, name='download_isolatestocks_experiment'),
                       url(r'^download/isolate/(?P<experiment_name>\w+)/', views.download_isolates_experiment, name='download_isolates_experiment'),

                       url(r'^download/data/plot/$', views_plot.download_plot_loader, name='download_plot_loader'),
                       url(r'^download/data/field/(?P<field_id>\w+)$', views_plot.download_plot_loader, name='download_field_plots'),
                       url(r'^download/data/fieldmap/$', views_plot.download_field_map, name='download_field_map'),
                       url(r'^download/data/tissue/$', views.download_tissue_data, name='download_tissue_data'),
                       url(r'^download/data/plant/$', views.download_plant_data, name='download_plant_data'),
                       url(r'^download/data/plate/$', views.download_plate_data, name='download_plate_data'),
                       url(r'^download/data/well/$', views.download_well_data, name='download_well_data'),
                       url(r'^download/data/culture/$', views.download_culture_data, name='download_culture_data'),
                       url(r'^download/data/maize/$', views.download_maize_data, name='download_maize_data'),
                       url(r'^download/data/microbe/$', views.download_microbe_data, name='download_microbe_data'),
                       url(r'^download/data/separation/$', views.download_separation_data, name='download_separation_data'),
                       url(r'^download/data/environment/$', views.download_env_data, name='download_env_data'),
                       url(r'^download/data/measurements/$', views.download_measurement_data, name='download_measurement_data'),
                       url(r'^download/file_storage/(?P<file_id>\d+)/$', views.download_file_dump, name='download_file_dump'),

                       url(r'^upload_online/(?P<template_type>\w+)/', views.upload_online, name='upload_online'),

                       url(r'^query/options/$', views.query_builder_options, name='query_builder_options'),
                       url(r'^query/fields/$', views.query_builder_fields, name='query_builder_fields'),
                       url(r'^query/$', views.query_builder, name='query_builder'),

                       url(r'^mycotoxin/templates/$', views.mycotoxin_templates, name='mycotoxin_templates'),
                       )
