from django.db import models
from django.contrib.auth.models import User

# orphan table
class Legacy_DiseaseInfo(models.Model):
    trait = models.CharField(max_length=100)
    disease_name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    disease_info = models.CharField(max_length=100)

    def __unicode__(self):
        return self.abbreviation

# phenotype and row feed into it, no foreign keys
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
    genotype_plate_id = models.CharField(max_length=100)
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
    call_name = models.CharField(max_length=100)
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

class Legacy_Isolate(models.Model):
    ID = models.CharField(max_length=100, primary_key=True)
    isolate_id = models.CharField(max_length=100)
    isolate_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    other_sname = models.CharField(max_length=100)
    pathotype_race = models.CharField(max_length=100)
    mating_type = models.CharField(max_length=100)
    disease_common_name = models.CharField(max_length=100)
    collection_site = models.CharField(max_length=100)
    collection_date = models.CharField(max_length=100)
    plant_organ = models.CharField(max_length=100)
    collector = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    glycerol_stock_n80c = models.CharField(max_length=100)
    mycelium_4c = models.CharField(max_length=100)
    cite = models.CharField(max_length=100)
    notes = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.isolate_id

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

class Legacy_DivPanel_Association(models.Model):
    disease = models.CharField(max_length=100)
    trait = models.CharField(max_length=100)
    marker_set = models.CharField(max_length=100)
    marker = models.CharField(max_length=100)
    chromosome = models.CharField(max_length=100)
    position_agpv1 = models.CharField(max_length=100)
    position_agpv2 = models.CharField(max_length=100)
    marker_f = models.CharField(max_length=100)
    marker_p = models.CharField(max_length=100)
    perm_p = models.CharField(max_length=100)
    markerr2 = models.CharField(max_length=100)
    markerdf = models.CharField(max_length=100)
    markerms = models.CharField(max_length=100)
    errordf = models.CharField(max_length=100)
    errorms = models.CharField(max_length=100)
    modeldf = models.CharField(max_length=100)
    modelms = models.CharField(max_length=100)
    geneticvar = models.CharField(max_length=100)
    residualvar = models.CharField(max_length=100)
    neg2LnLikelihood = models.CharField(max_length=100)
    gene_id = models.CharField(max_length=100)
    start_agpv1 = models.CharField(max_length=100)
    stop_agpv1 = models.CharField(max_length=100)
    strand = models.CharField(max_length=100)
    relationship_to_hit = models.CharField(max_length=100)
    interpro_domain = models.CharField(max_length=100)
    distance_from_gene = models.CharField(max_length=100)

    def __unicode__(self):
        return self.position_agpv1

class Legacy_DNA(models.Model):
    id_placeholder = models.CharField(max_length=100)
    plate_id = models.CharField(max_length=100)
    plate_name = models.CharField(max_length=100)
    well_id = models.CharField(max_length=100)
    well_A01 = models.CharField(max_length=100)
    well_01A = models.CharField(max_length=100)
    tissue_id = models.CharField(max_length=100)
    tissue_name = models.CharField(max_length=100)
    tissue_type = models.CharField(max_length=100)
    dna_person = models.CharField(max_length=100)
    dna_date = models.CharField(max_length=100)
    notes = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.well_id

class Legacy_NAM_GWAS(models.Model):
    disease = models.CharField(max_length=100)
    marker_set = models.CharField(max_length=100)
    chromosome = models.CharField(max_length=100)
    location_agpv1 = models.CharField(max_length=100)
    allele = models.CharField(max_length=100)
    NAM_GWAS_class = models.CharField(max_length=100)
    bpp = models.CharField(max_length=100)
    effect = models.CharField(max_length=100)
    cM = models.CharField(max_length=100)
    pvalue = models.CharField(max_length=100)
    consequence = models.CharField(max_length=100)
    gene_id = models.CharField(max_length=100)
    start_agpv1 = models.CharField(max_length=100)
    stop_agpv1 = models.CharField(max_length=100)
    strand = models.CharField(max_length=100)
    relationship_to_hit = models.CharField(max_length=100)
    interpro_domain = models.CharField(max_length=100)
    distance_from_gene = models.CharField(max_length=100)

    def __unicode__(self):
        return self.location_agpv1

class Legacy_Plate(models.Model):
    Plate_ID = models.CharField(max_length=100)
    Plate_Name = models.CharField(max_length=100)
    Plate_Type = models.CharField(max_length=100)
    Plate_Rep = models.CharField(max_length=100)
    Plate_Person_ID = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Shelf = models.CharField(max_length=100)
    Container_Name = models.CharField(max_length=100)
    Notes = models.CharField(max_length=100)

    def __unicode__(self):
        return self.Plate_ID

class Legacy_ProtocolTopics(models.Model):
    Topic = models.CharField(max_length=100)
    ID_placeholder = models.CharField(max_length=100)

    def __unicode__(self):
        return self.Topic

class Legacy_Protocols(models.Model):
    ID_placeholder = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Filename = models.CharField(max_length=100)
    Filetype = models.CharField(max_length=100)
    Keywords = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Reference = models.CharField(max_length=100)
    ProtocolTopic_ID = models.CharField(max_length=100)

    def __unicode__(self):
        return self.Title

class Legacy_QTLSummarys(models.Model):
    ID_placeholder = models.CharField(max_length=100)
    ReferenceID = models.CharField(max_length=100)
    Pathogen = models.CharField(max_length=100)
    AnalysisMethod = models.CharField(max_length=100)
    pValueThreshold = models.CharField(max_length=100)
    LODThreshold = models.CharField(max_length=100)
    Phenotype = models.CharField(max_length=100)
    Population = models.CharField(max_length=100)
    Germplasm = models.CharField(max_length=100)
    Chromosome = models.CharField(max_length=100)
    Significant_marker = models.CharField(max_length=100)
    Sig_cM = models.CharField(max_length=100)
    Sig_bp_agpv1 = models.CharField(max_length=100)
    BinPub = models.CharField(max_length=100)
    LBinIBM2Neighbors = models.CharField(max_length=100)
    Lbin = models.CharField(max_length=100)
    LMarkerSpecific_panzea = models.CharField(max_length=100)
    LMarker_m = models.CharField(max_length=100)
    LcM = models.CharField(max_length=100)
    Lbp_agpv1 = models.CharField(max_length=100)
    QTL_95_CI = models.CharField(max_length=100)
    Chr = models.CharField(max_length=100)
    RBinIBM2Neighbors = models.CharField(max_length=100)
    Rbin = models.CharField(max_length=100)
    RMarkerSpecific_panzea = models.CharField(max_length=100)
    RMarker_m = models.CharField(max_length=100)
    RcM = models.CharField(max_length=100)
    Rbp_agpv1 = models.CharField(max_length=100)
    Donor = models.CharField(max_length=100)
    DonorNotes = models.CharField(max_length=100)
    ENVobsENVexp = models.CharField(max_length=100)
    YRobsYRexp = models.CharField(max_length=100)
    DetectedInCombinedAnalysis = models.CharField(max_length=100)
    LOD = models.CharField(max_length=100)
    PVE = models.CharField(max_length=100)
    NOTES = models.CharField(max_length=100)
    Authority = models.CharField(max_length=100)
    DiseaseInfo_ID = models.CharField(max_length=100)

    def __unicode__(self):
        return self.Chromosome
