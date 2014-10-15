from django.db import models
from django.contrib.auth.models import User

# orphan table
class Legacy_DiseaseInfo(models.Model):
    Trait = models.CharField(max_length=100)
    DiseaseName = models.CharField(max_length=100)
    Abbreviation = models.CharField(max_length=100)
    Topic = models.CharField(max_length=100)
    DiseaseInfo = models.CharField(max_length=100)
    upsize_ts = models.CharField(max_length=100)

    def __unicode__(self):
        return self.Abbreviation

# phenotype and row feed into it, no forein keys
class Legacy_Experiment(models.Model):
    experiment_id = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=100)
    planting_date = models.CharField(max_length=100)
    tissue_collection = models.CharField(max_length=100)
    inoculations = models.CharField(max_length=100)
    inoculation_date1 = models.CharField(max_length=100)
    inoculation_date2 = models.CharField(max_length=100)
    inoculation_date3 = models.CharField(max_length=100)
    pathogen_isolate = models.CharField(max_length=100)
    harvest_date = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    notes = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.experiment_id

# plate_name FK's into DNA later
"""Includes some FK

class genotype(models.Model):
    genotype_plate_id = models.CharField(max_length=100, primary_key=True)
    genotype_well_id = models.CharField(max_length=100)
    genotype_plate_name = models.CharField(max_length=100)
    well_A01 = models.CharField(max_length=100)
    well_01A = models.CharField(max_length=100)
    plate_size = models.CharField(max_length=100)
    dna_id = models.CharField(max_length=100)
    sample_id = models.CharField(max_length=100)
    locus_name = models.CharField(max_length=100)
    marker_id = models.CharField(max_length=100)
    marker_name = models.CharField(max_length=100)
    marker_type = models.CharField(max_length=100)
    f_primer_id = models.CharField(max_length=100)
    r_primer_id = models.CharField(max_length=100)
    f2_primer_id = models.CharField(max_length=100)
    r2_primer_id = models.CharField(max_length=100)
    label_color = models.CharField(max_length=100)
    value1 = models.CharField(max_length=100)
    value2 = models.CharField(max_length=100)
    value3 = models.CharField(max_length=100)
    value4 = models.CharField(max_length=100)
    passive_ref = models.CharField(max_length=100)
    quality_value = models.CharField(max_length=100)
    call_type = models.CharField(max_length=100)
    call = models.CharField(max_length=100)
    genotype = models.CharField(max_length=100)
    brc_plate_num = models.CharField(max_length=100)
    brc_sample_num = models.CharField(max_length=100)
    genotype_file = models.CharField(max_length=100)
    run_date = models.DateField()
    #genotype_person_id = models.ForeignKey("People")
    genotype_person_id = models.ForeignKey("People")
    notes = models.CharField(max_length=100)

    def __unicode__(self):
        return self.genotype_plate_name
    """

class Legacy_Genotype(models.Model):
    genotype_plate_id = models.CharField(max_length=100, primary_key=True)
    genotype_well_id = models.CharField(max_length=100)
    genotype_plate_name = models.CharField(max_length=100)
    well_A01 = models.CharField(max_length=100)
    well_01A = models.CharField(max_length=100)
    plate_size = models.CharField(max_length=100)
    dna_id = models.CharField(max_length=100)
    sample_id = models.CharField(max_length=100)
    locus_name = models.CharField(max_length=100)
    marker_id = models.CharField(max_length=100)
    marker_name = models.CharField(max_length=100)
    marker_type = models.CharField(max_length=100)
    f_primer_id = models.CharField(max_length=100)
    r_primer_id = models.CharField(max_length=100)
    f2_primer_id = models.CharField(max_length=100)
    r2_primer_id = models.CharField(max_length=100)
    label_color = models.CharField(max_length=100)
    value1 = models.CharField(max_length=100)
    value2 = models.CharField(max_length=100)
    value3 = models.CharField(max_length=100)
    value4 = models.CharField(max_length=100)
    passive_ref = models.CharField(max_length=100)
    quality_value = models.CharField(max_length=100)
    call_type = models.CharField(max_length=100)
    call = models.CharField(max_length=100)
    genotype = models.CharField(max_length=100)
    brc_plate_num = models.CharField(max_length=100)
    brc_sample_num = models.CharField(max_length=100)
    genotype_file = models.CharField(max_length=100)
    run_date = models.CharField(max_length=100)
    genotype_person_id = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    def __unicode__(self):
        return self.genotype_plate_name

"""This has some FK

class markers(models.Model):
    id_placeholder = models.CharField(max_length=100)
    marker_id = models.CharField(max_length=100)
    locus_name = models.CharField(max_length=100)
    chromosome = models.CharField(max_length=100)
    maize_bin = models.CharField(max_length=100)
    map_physical = models.CharField(max_length=100)
    map_physical_refgen_v1 = models.CharField(max_length=100)
    map_physical_refgen_v2 = models.CharField(max_length=100)
    map_physical_refgen_v3 = models.CharField(max_length=100)
    bac = models.CharField(max_length=100)
    nam_marker = models.CharField(max_length=100)
    map_IBM2n_cM = models.CharField(max_length=100)
    polymorphism_type = models.CharField(max_length=100)
    snp_type = models.CharField(max_length=100)
    sequence_f1 = models.CharField(max_length=100)
    sequence_f2 = models.CharField(max_length=100)
    sequence_r1 = models.CharField(max_length=100)
    sequence_r2 = models.CharField(max_length=100)
    primer_name_f1 = models.CharField(max_length=100)
    primer_name_f2 = models.CharField(max_length=100)
    primer_name_r1 = models.CharField(max_length=100)
    primer_name_r2 = models.CharField(max_length=100)
    primer_tail = models.CharField(max_length=100)
    size_range = models.CharField(max_length=100)
    Tm_min = models.CharField(max_length=100)
    Tm_max = models.CharField(max_length=100)
    chemestry = models.CharField(max_length=100)
    primer_person = models.ForeignKey("People")
    order_date = models.DateField()
    consense_sequence = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    reference_B73 = models.CharField(max_length=100)
    reference_Mo17 = models.CharField(max_length=100)
    reference_CML52 = models.CharField(max_length=100)
    reference_DK888 = models.CharField(max_length=100)
    reference_S11 = models.CharField(max_length=100)
    reference_XL380 = models.CharField(max_length=100)
    reference_Tx303 = models.CharField(max_length=100)
    MaizeGDBLink = models.CharField(max_length=100)
    MaizeSeqLink = models.CharField(max_length=100)

    def __unicode__(self):
        return self.marker_id
"""

class Legacy_Markers(models.Model):
    id_placeholder = models.CharField(max_length=100)
    marker_id = models.CharField(max_length=100)
    locus_name = models.CharField(max_length=100)
    chromosome = models.CharField(max_length=100)
    maize_bin = models.CharField(max_length=100)
    map_physical = models.CharField(max_length=100)
    map_physical_refgen_v1 = models.CharField(max_length=100)
    map_physical_refgen_v2 = models.CharField(max_length=100)
    map_physical_refgen_v3 = models.CharField(max_length=100)
    bac = models.CharField(max_length=100)
    nam_marker = models.CharField(max_length=100)
    map_IBM2n_cM = models.CharField(max_length=100)
    polymorphism_type = models.CharField(max_length=100)
    snp_type = models.CharField(max_length=100)
    sequence_f1 = models.CharField(max_length=100)
    sequence_f2 = models.CharField(max_length=100)
    sequence_r1 = models.CharField(max_length=100)
    sequence_r2 = models.CharField(max_length=100)
    primer_name_f1 = models.CharField(max_length=100)
    primer_name_f2 = models.CharField(max_length=100)
    primer_name_r1 = models.CharField(max_length=100)
    primer_name_r2 = models.CharField(max_length=100)
    primer_tail = models.CharField(max_length=100)
    size_range = models.CharField(max_length=100)
    Tm_min = models.CharField(max_length=100)
    Tm_max = models.CharField(max_length=100)
    chemestry = models.CharField(max_length=100)
    primer_person = models.CharField(max_length=100)
    order_date = models.CharField(max_length=100)
    consense_sequence = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    reference_B73 = models.CharField(max_length=100)
    reference_Mo17 = models.CharField(max_length=100)
    reference_CML52 = models.CharField(max_length=100)
    reference_DK888 = models.CharField(max_length=100)
    reference_S11 = models.CharField(max_length=100)
    reference_XL380 = models.CharField(max_length=100)
    reference_Tx303 = models.CharField(max_length=100)
    MaizeGDBLink = models.CharField(max_length=100)
    MaizeSeqLink = models.CharField(max_length=100)

    def __unicode__(self):
        return self.marker_id

"""This has some FK
# entity_id might FK to row?
# plate_id FK to Plate later
class Phenotype(models.Model):
    phenotype_id = models.CharField(max_length=100, primary_key=True)
    entity_id = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=100)
    experiment_id = models.ForeignKey(Experiment)
    trait_id = models.ForeignKey("Trait_info")
    phenotype_value = models.CharField(max_length=100)
    phenotype_date = models.DateField()
    plate_id = models.CharField(max_length=100)
    phenotype_person_id = models.ForeignKey("People")
    scoring_order = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    changed = models.CharField(max_length=100)
    technical_rep = models.CharField(max_length=100)
    biological_rep = models.CharField(max_length=100)
    trait_id_buckler = models.CharField(max_length=100)

    def __unicode__(self):
        return self.phenotype_id
"""

class Legacy_Phenotype(models.Model):
    phenotype_id = models.CharField(max_length=100, primary_key=True)
    entity_id = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=100)
    experiment_id = models.CharField(max_length=100)
    trait_id = models.CharField(max_length=100)
    phenotype_value = models.CharField(max_length=100)
    phenotype_date = models.CharField(max_length=100)
    plate_id = models.CharField(max_length=100)
    phenotype_person_id = models.CharField(max_length=100)
    scoring_order = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    changed = models.CharField(max_length=100)
    technical_rep = models.CharField(max_length=100)
    biological_rep = models.CharField(max_length=100)
    trait_id_buckler = models.CharField(max_length=100)

    def __unicode__(self):
        return self.phenotype_id

"""This has some FK
class Row(models.Model):
    row_id = models.CharField(max_length=100, primary_key=True)
    row_name = models.CharField(max_length=100)
    experiment_id = models.ForeignKey(Experiment)
    pedigree = models.CharField(max_length=100)
    line_num = models.CharField(max_length=100)
    source_seed_id = models.CharField(max_length=100)
    source_seed_name = models.CharField(max_length=100)
    range_num = models.CharField(max_length=100)
    plot = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    rep_num = models.CharField(max_length=100)
    kernel_num = models.CharField(max_length=100)
    pop = models.CharField(max_length=100)
    delay = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    row_person = models.CharField(max_length=100)

    def __unicode__(self):
        return self.row_id
"""

class Legacy_Seed(models.Model):
    seed_id = models.CharField(max_length=100, unique=True)
    plant_id_origin = models.CharField(max_length=100)
    row_id_origin = models.CharField(max_length=100)
    experiment_id_origin = models.ForeignKey(Legacy_Experiment, to_field='experiment_id')
    plant_name = models.CharField(max_length=100)
    row_name = models.CharField(max_length=100)
    seed_name = models.CharField(max_length=100)
    cross_type = models.CharField(max_length=100)
    male_parent_id = models.CharField(max_length=100)
    male_parent_name = models.CharField(max_length=100)
    program_origin = models.CharField(max_length=100)
    seed_pedigree = models.CharField(max_length=100)
    line_num = models.CharField(max_length=100)
    seed_person_id = models.CharField(max_length=100)
    disease_info = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    accession = models.CharField(max_length=100)
    lot = models.CharField(max_length=100)

    def __unicode__(self):
        return self.seed_id

"""
This Seed Model Still Has the Foreign Keys
class Seed(models.Model):
    seed_id = models.CharField(max_length=100, primary_key=True)
    plant_id_origin = models.ForeignKey(Plant)
    row_id_origin = models.ForeignKey(Row)
    experiment_id_origin = models.ForeignKey(Experiment)
    plant_name = models.CharField(max_length=100)
    row_name = models.CharField(max_length=100)
    seed_name = models.CharField(max_length=100)
    cross_type = models.CharField(max_length=100)
    male_parent_id = models.CharField(max_length=100)
    male_parent_name = models.CharField(max_length=100)
    program_origin = models.CharField(max_length=100)
    seed_pedigree = models.CharField(max_length=100)
    line_num = models.CharField(max_length=100)
    seed_person_id = models.ForeignKey(People)
    disease_info = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    accession = models.CharField(max_length=100)
    lot = models.CharField(max_length=100)

    def __unicode__(self):
        return self.seed_id
"""

class Legacy_Row(models.Model):
    row_id = models.CharField(max_length=100, primary_key=True)
    row_name = models.CharField(max_length=100)
    experiment_id = models.ForeignKey(Legacy_Experiment, to_field='experiment_id')
    pedigree = models.CharField(max_length=100)
    line_num = models.CharField(max_length=100)
    source_seed_id = models.CharField(max_length=100, default='0')
    source_seed_name = models.CharField(max_length=100)
    range_num = models.CharField(max_length=100)
    plot = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    rep_num = models.CharField(max_length=100)
    kernel_num = models.CharField(max_length=100)
    pop = models.CharField(max_length=100)
    delay = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    row_person = models.CharField(max_length=100)

    def __unicode__(self):
        return self.row_id

"""This has some FK
class Plant(models.Model):
    plant_id = models.CharField(max_length=100, primary_key=True)
    row_id = models.ForeignKey("Row")
    plant_name = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    def __unicode__(self):
        return self.plant_id
"""

class Legacy_Plant(models.Model):
    plant_id = models.CharField(max_length=100, primary_key=True)
    row_id = models.CharField(max_length=100)
    plant_name = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    def __unicode__(self):
        return self.plant_id

class Legacy_Tissue(models.Model):
    ID = models.CharField(max_length=100, primary_key=True)
    experiment_id = models.CharField(max_length=100)
    entity_id = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=100)
    pedigree = models.CharField(max_length=100)
    row_name = models.CharField(max_length=100)
    plant = models.CharField(max_length=100)
    tissue_type = models.CharField(max_length=100)
    well = models.CharField(max_length=100)
    tissue_plate_id = models.CharField(max_length=100)
    comments = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.well

class Legacy_People(models.Model):
    person_id = models.CharField(max_length=100, primary_key=True)
    person_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    URL = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    peopleorg_id = models.CharField(max_length=100)

    def __unicode__(self):
        return self.person_name

"""This has FK
class Seed_inventory(models.Model):
    ID_placeholder = models.CharField(max_length=100, primary_key=True)
    seed_id = models.CharField(max_length=100)
    seed_name = models.CharField(max_length=100)
    inventory_date = models.DateField()
    inventory_person = models.CharField(max_length=100)
    seed_person_id = models.ForeignKey(People)
    location = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    weight_g = models.CharField(max_length=100)

    def __unicode__(self):
        return self.seed_id
"""

class Legacy_Seed_Inventory(models.Model):
    ID = models.CharField(max_length=100, primary_key=True)
    seed_id = models.CharField(max_length=100)
    seed_name = models.CharField(max_length=100)
    inventory_date = models.CharField(max_length=100)
    inventory_person = models.CharField(max_length=100)
    seed_person_id = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    weight_g = models.CharField(max_length=100)

    def __unicode__(self):
        return self.seed_id

class Legacy_Trait_info(models.Model):
    trait_id = models.CharField(max_length=100, primary_key=True)
    trait_grp = models.CharField(max_length=100)
    trait_grp_id = models.CharField(max_length=100)
    trait_name = models.CharField(max_length=100)
    trait_name_id = models.CharField(max_length=100)
    trait_basis = models.CharField(max_length=100)
    trait_id_buckler = models.CharField(max_length=100)
    trait_min = models.CharField(max_length=100)
    trait_max = models.CharField(max_length=100)
    data_type = models.CharField(max_length=100)
    trait_howto = models.CharField(max_length=100)
    trait_when = models.CharField(max_length=100)

    def __unicode__(self):
        return self.trait_name
