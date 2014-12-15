SET FOREIGN_KEY_CHECKS = 0;

delete from lab_collecting;
delete from lab_diseaseinfo;
delete from lab_experiment;
delete from lab_field;
delete from lab_isolate;
delete from lab_locality;
delete from lab_location;
delete from lab_measurement;
delete from lab_measurementparameter;
delete from lab_obsplant;
delete from lab_obsrow;
delete from lab_obssample;
delete from lab_obsenv;
delete from lab_obsselector;
delete from lab_passport;
delete from lab_people;
delete from lab_publication;
delete from lab_stock;
delete from lab_stockpacket;
delete from lab_taxonomy;
delete from lab_treatment;

delete from legacy_legacy_diseaseinfo;
delete from legacy_legacy_experiment;
delete from legacy_legacy_genotype;
delete from legacy_legacy_isolate;
delete from legacy_legacy_markers;
delete from legacy_legacy_people;
delete from legacy_legacy_phenotype;
delete from legacy_legacy_plant;
delete from legacy_legacy_row;
delete from legacy_legacy_seed;
delete from legacy_legacy_seed_inventory;
delete from legacy_legacy_tissue;
delete from legacy_legacy_trait_info;

delete from auth_group;
delete from auth_group_permissions;
delete from auth_permission;
delete from auth_user_groups;
delete from auth_user_user_permissions;
delete from django_admin_log;
delete from django_content_type;
delete from django_migrations;
delete from django_session;

delete from auth_user;
delete from lab_userprofile;

ALTER TABLE auth_user AUTO_INCREMENT = 1;
ALTER TABLE lab_userprofile AUTO_INCREMENT = 1;

SET FOREIGN_KEY_CHECKS = 1;