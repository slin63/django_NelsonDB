from django import forms
from django.contrib.contenttypes.models import ContentType

from lab.models import UserProfile, Experiment, Field, ObsPlot, ObsPlant, Locality, Stock, ObsPlot, ObsPlant, ObsSample, IsolateStock, \
  ObsEnv, MeasurementParameter, Citation, Medium, Location, DiseaseInfo, FileDump, StockPacket
from django.contrib.auth.models import User
from django.core.validators import EmailValidator


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),
                               help_text="Choose a username:")
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), validators=[EmailValidator],
                            help_text="Enter your email:")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               help_text="Select a password:")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}), help_text="First name:")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), help_text="Last name:")
    lab_key = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Lab Key'}), help_text="Secret lab key:")

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'lab_key']


class DownloadFieldForm(forms.ModelForm):
    field = forms.ModelChoiceField(queryset=Field.objects.exclude(id=1), empty_label="Download a field map",
    help_text='Select a field-map to download: ', required=True)

    get_csv_instead = forms.BooleanField(required=False, help_text='Check to download Plot Data for selected Field: ')

    class Meta:
      model = Field
      fields = ['field', 'get_csv_instead']


class PacketGenForm(forms.ModelForm):
    choices = (
        ('generate_labels', 'Generate labels for existing seed packets'),
        ('preview_packets', 'Preview generated stock packets for next year'),
        ('create_packets', 'Push generated stock packets from preview onto DB')
    )
    exp = forms.ModelChoiceField(queryset=Experiment.objects.all(), required=True, help_text="Select experiment to create packet data for: ")
    packet_choice = forms.ChoiceField(required=True, help_text='Select an action to perform: ', choices=choices, widget=forms.RadioSelect)
    confirm = forms.BooleanField(required=False, help_text='Check to confirm selected action: ', initial=False)

    class Meta:
      model = Experiment
      fields = ['exp', 'packet_choice', 'confirm']


class FileDumpForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="--- Username ---",
                                  help_text="Select the primary user:", required=True)
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        help_text="Select the experiment if relevant:", required=True)
    file_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'File Name'}),
                                help_text="Give an informative name to the file:")
    file = forms.FileField(help_text="Select your file:")
    file_subdirectory = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'File subdirectory'}),
                                help_text="Select a subdirectory to store your file in:")
    comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments:'}),
                               help_text="Any additional comments:", required=False)

    class Meta:
        model = FileDump
        fields = ['user', 'experiment', 'file_name', 'file_subdirectory', 'file', 'comments']


class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}),
                            help_text="Add your phone number:")
    organization = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Organization'}),
                                   help_text="Your affiliated organization:")
    job_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Job Title'}),
                                help_text="(Optional) Type your job title:", required=False)
    notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Notes', 'rows': '5', 'cols': '20'}),
                            help_text="(Optional) Add any notes about yourself:", required=False)
    website = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Website'}),
                             help_text="(Optional) Your website: ", required=False)
    picture = forms.ImageField(widget=forms.ClearableFileInput(), help_text="(Optional) Select a profile image:",
                               initial='profile_images/underwater.jpg', required=False)

    class Meta:
        model = UserProfile
        fields = ['phone', 'organization', 'job_title', 'notes', 'website', 'picture']


class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Old Password'}),
                                   help_text="Type your old password:")
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}),
                                   help_text="Select a new password:")
    new_password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Retype New Password'}),
                                          help_text="Retype your new password:")

    class Meta:
        model = User
        fields = []


class EditUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               help_text="Type your password:")
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), validators=[EmailValidator],
                            help_text="Edit your email:", required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
                                 help_text="Change you first name:", required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
                                help_text="Change your last name:", required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class EditUserProfileForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}),
                            help_text="Edit your phone number:", required=False)
    organization = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Organization'}),
                                   help_text="Edit your affiliated organization:", required=False)
    job_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Job Title'}),
                                help_text="Change your job title:", required=False)
    notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Notes', 'rows': '5', 'cols': '20'}),
                            help_text="Modify any notes about yourself:", required=False)
    website = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Website'}),
                              help_text="Change your website: ", required=False)
    picture = forms.ImageField(help_text="Change your profile image:", required=False)

    class Meta:
        model = UserProfile
        fields = ['phone', 'organization', 'job_title', 'notes', 'website', 'picture']


class NewExperimentForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="--- Username ---",
                                  help_text="Select the primary user:", required=True)
    field = forms.ModelChoiceField(queryset=Field.objects.all(), empty_label="--- Field Name ---",
                                   help_text="Select a field or select 'No Field':", required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Experiment Name'}),
                           help_text="Assign an experiment name (e.g. 15XY with NO SPACES, UNDERLINES, or SPECIAL CHARACTERS):",
                           required=True)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Start Date'}),
                                 help_text="Give a start date in format MM/DD/YYYY:", required=True)
    purpose = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Purpose'}),
                              help_text="Description of purpose:", required=True)
    comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments', 'rows': '5', 'cols': '20'}),
                               help_text="Any additional comments:", required=False)


class NewTreatmentForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        help_text="Select the experiment:", required=True)
    treatment_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Treatment ID'}),
                                   help_text="Assign a unique ID for this treatment:", required=True)
    treatment_type = forms.CharField(widget=forms.DateInput(attrs={'placeholder': 'Treatment Type'}),
                                     help_text="What kind of treatment (e.g. inoculation, fertilizer):", required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Treatment Date'}),
                           help_text="On what date was treatment (01-30-2015):", required=True)
    comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments', 'rows': '5', 'cols': '20'}),
                               help_text="Any additional comments:", required=False)


class NewFieldForm(forms.Form):
    locality = forms.ModelChoiceField(queryset=Locality.objects.all(), empty_label="--- Locality ---",
                                      help_text="Select the correct locality:", required=True)
    field_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Field Name'}),
                                 help_text="Give a field name:", required=True)
    field_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Field Num'}),
                                help_text="What is the field number:", required=False)
    planting_year = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Planting Year'}),
                                help_text="What year was it planted?:", required=True)
    dimensions = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Field Dimensions'}),
                                help_text="The range/row dimensions of the field:", required=True)
    comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}),
                               help_text="Any additional comments:", required=False)


class NewLocalityForm(forms.Form):
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}), help_text="Type a city name:",
                           required=True)
    county = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'County'}), help_text="Type a county name:",
                             required=False)
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'State'}),
                            help_text="What state is the city in:", required=False)
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country'}),
                              help_text="What country is the state in:", required=False)
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Zipcode'}), help_text="Type the zipcode:",
                              required=False)


class NewMeasurementParameterForm(forms.Form):
    parameter = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Parameter'}),
                                help_text="Type a new parameter:", required=True)
    parameter_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Parameter Type'}),
                                     help_text="What type of parameter is this:", required=True)
    protocol = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Protocol'}),
                               help_text="Give a description of the protocol:", required=False)
    # Not needed for FCP
    # trait_id_buckler = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Buckler Trait ID'}), help_text="Give Buckler trait ID if exists:", required=False)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}),
                                       help_text="Briefly describe this parameter:", required=False)
    unit_of_measure = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Unit of Measure'}),
                                      help_text="What is the unit of measure:", required=False)


class NewLocationForm(forms.Form):
    locality = forms.ModelChoiceField(queryset=Locality.objects.all(), empty_label="--- Locality ---",
                                      help_text="Select the correct locality:", required=True)
    building_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Building Name'}),
                                    help_text="Type the building name:", required=True)
    location_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location Name'}),
                                    help_text="Type the location name:", required=True)
    room = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Room'}),
                           help_text="Type the room name or number:", required=False)
    shelf = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Shelf'}),
                            help_text="Give the shelf name or number:", required=False)
    column = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Column'}),
                             help_text="Give the column name or number:", required=False)
    box_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Box Name'}),
                               help_text="Give the box name:", required=False)
    comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}),
                               help_text="Any additional comments:", required=False)


class NewDiseaseInfoForm(forms.Form):
    common_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Common Name'}),
                                  help_text="Type the disease common name:", required=True)
    abbrev = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Abbreviation'}),
                             help_text="Type the abbreviation:", required=False)
    comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}),
                               help_text="Any additional comments:", required=False)


class NewCitationForm(forms.Form):
    citation_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Citation Type'}),
                                    help_text="Type the disease common name:", required=True)
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}), help_text="Type the citation:",
                            required=False)
    url = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'URL'}),
                          help_text="A URL linking to the article:", required=False)
    pubmed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pubmed ID'}), help_text="The Pubmed ID:",
                                required=False)
    comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}),
                               help_text="Any additional comments:", required=False)


class NewMediumForm(forms.Form):
    citation = forms.ModelChoiceField(queryset=Citation.objects.all(), empty_label="--- Citation ---",
                                      help_text="Select the relevant citation:", required=True)
    media_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Media Name'}),
                                 help_text="A unique name for the media:", required=True)
    media_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Media Type'}),
                                 help_text="The type of media:", required=False)
    media_description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}),
                                        help_text="A brief description of the media and its uses:", required=False)
    media_preparation = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Preparation'}),
                                        help_text="How the media is prepared:", required=False)
    comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}),
                               help_text="Any additional comments:", required=False)


class NewTaxonomyForm(forms.Form):
    binomial = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Binomial'}),
                               help_text="Type the Binomial:",
                               required=False)
    population = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Population'}),
                                 help_text="Type the population:", required=False)
    alias = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Alias'}),
                            help_text="Type the alias (historically for isolatestocks):", required=False)
    race = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Race'}),
                           help_text="Type the race (historically for isolatestocks):", required=False)
    subtaxa = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sub-taxa'}),
                              help_text="Type the sub-taxa (historically for isolatestocks):", required=False)


class UpdateSeedDataOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        help_text="Experiment", required=True)
    stock__seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Seed ID'}), help_text="Seed ID:",
                                     required=True)
    stock__seed_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Seed Name'}),
                                       help_text="Seed Name:", required=True)
    stock__cross_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Cross Type'}),
                                        help_text="Cross Type:", required=False)
    stock__pedigree = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pedigree'}), help_text="Pedigree",
                                      required=False)
    stock__stock_status = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Stock Status'}),
                                          help_text="Stock Status", required=False)
    stock__stock_date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Stock Date'}),
                                        help_text="Stock Date", required=False)
    stock__inoculated = forms.BooleanField(help_text="Inoculated", required=False)
    stock__comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}),
                                      help_text="Stock Comments", required=False)
    stock__passport__taxonomy__binomial = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Binomial'}),
                                                          help_text="Binomial", required=False)
    stock__passport__taxonomy__population = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Population'}),
                                                            help_text="Population", required=False)
    obs_plot__plot_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plot ID'}), help_text="Plot ID",
                                      required=False)
    obs_plant__plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plant ID'}),
                                          help_text="Plant ID", required=False)
    field = forms.ModelChoiceField(queryset=Field.objects.all(), empty_label="--- Field Source ---",
                                   initial=Field.objects.get(id=1), help_text="Field Source", required=True)
    stock__passport__collecting__user = forms.ModelChoiceField(queryset=User.objects.all(),
                                                               empty_label="--- Collected By ---",
                                                               initial=User.objects.get(username='unknown_person'),
                                                               help_text="Collector", required=True)
    stock__passport__collecting__collection_date = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Collection Date'}), help_text="Date Collected", required=False)
    stock__passport__collecting__collection_method = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Collection Method'}), help_text="Collection Method",
        required=False)
    stock__passport__collecting__comments = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Collection Comments'}), help_text="Collection Comments",
        required=False)
    stock__passport__people__first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source First Name'}), help_text="Source First Name",
        required=False)
    stock__passport__people__last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source Last Name'}), help_text="Source Last Name", required=False)
    stock__passport__people__organization = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source Organization'}), help_text="Source Organization",
        required=False)
    stock__passport__people__phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Phone'}),
                                                     help_text="Source Phone", required=False)
    stock__passport__people__email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Email'}),
                                                     help_text="Source Email", required=False)
    stock__passport__people__comments = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source Comments'}), help_text="Source Comments", required=False)


class LogSeedDataOnlineForm(forms.Form):
    experiment_used = forms.BooleanField(help_text="Used", required=False)
    experiment_collected = forms.BooleanField(help_text="Collected", required=False, initial=True)
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        help_text="Experiment", required=True)
    stock__seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Seed ID'}), help_text="Seed ID:",
                                     required=True)
    stock__seed_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Seed Name'}),
                                       help_text="Seed Name:", required=True)
    stock__cross_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Cross Type'}),
                                        help_text="Cross Type:", required=False)
    stock__pedigree = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pedigree'}), help_text="Pedigree",
                                      required=False)
    stock__stock_status = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Stock Status'}),
                                          help_text="Stock Status", required=False)
    stock__stock_date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Stock Date'}),
                                        help_text="Stock Date", required=False)
    stock__inoculated = forms.BooleanField(help_text="Inoculated", required=False)
    stock__comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}),
                                      help_text="Stock Comments", required=False)
    stock__passport__taxonomy__binomial = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Binomial'}),
                                                          help_text="Binomial", required=False)
    stock__passport__taxonomy__population = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Population'}),
                                                            help_text="Population", required=False)
    obs_plot__plot_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plot ID'}), help_text="Plot ID",
                                      required=False)
    obs_plant__plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plant ID'}),
                                          help_text="Plant ID", required=False)
    field = forms.ModelChoiceField(queryset=Field.objects.all(), empty_label="--- Field Source ---",
                                   initial=Field.objects.get(id=1), help_text="Field Source", required=True)
    stock__passport__collecting__user = forms.ModelChoiceField(queryset=User.objects.all(),
                                                               empty_label="--- Collected By ---",
                                                               initial=User.objects.get(username='unknown_person'),
                                                               help_text="Collector", required=True)
    stock__passport__collecting__collection_date = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Collection Date'}), help_text="Date Collected", required=False)
    stock__passport__collecting__collection_method = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Collection Method'}), help_text="Collection Method",
        required=False)
    stock__passport__collecting__comments = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Collection Comments'}), help_text="Collection Comments",
        required=False)
    stock__passport__people__first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source First Name'}), help_text="Source First Name",
        required=False)
    stock__passport__people__last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source Last Name'}), help_text="Source Last Name", required=False)
    stock__passport__people__organization = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source Organization'}), help_text="Source Organization",
        required=False)
    stock__passport__people__phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Phone'}),
                                                     help_text="Source Phone", required=False)
    stock__passport__people__email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Email'}),
                                                     help_text="Source Email", required=False)
    stock__passport__people__comments = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source Comments'}), help_text="Source Comments", required=False)
    gen = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Generation'}), required=False)


class LogStockPacketOnlineForm(forms.Form):
    stock__seed_id = forms.ModelChoiceField(queryset=Stock.objects.all(), empty_label="--- Seed ID ---", required=True)
    weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Weight'}), required=False)
    num_seeds = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Num Seeds'}), required=False)
    comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Packet Comments'}), required=False)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label="--- Storage Location ---",
                                      required=True)
    gen = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Generation'}), required=False)


class UpdateStockPacketOnlineForm(forms.Form):
    weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Weight'}), required=False)
    num_seeds = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Num Seeds'}), required=False)
    comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Packet Comments'}), required=False)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label="--- Storage Location ---",
                                      required=True)


class LogPlotsOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        required=True)
    plot_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plot ID'}), required=True)
    plot_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plot Name'}), required=True)
    seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Seed ID'}), required=True)
    polli_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pollination type'}), required=True)

    field = forms.ModelChoiceField(queryset=Field.objects.all(), initial=Field.objects.get(id=1),
                                   empty_label="--- Field Name ---", required=True)
    row_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Row'}), required=False)
    range_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Range'}), required=False)
    plot = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plot'}), required=False)
    block = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Block'}), required=False)
    rep = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Rep'}), required=False)
    kernel_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Kernel Num'}), required=False)
    planting_date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Planting Date'}), required=False)
    harvest_date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Harvest Date'}), required=False)
    row_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}), required=False)
    gen = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Generation'}), required=False)


class LogPlantsOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        required=True)
    plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plant ID'}), required=True)
    plant_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plant Num'}), required=True)
    seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Seed ID'}), required=True)
    plot_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plot ID'}), required=False)
    plant_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}), required=False)


class LogSamplesOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        help_text="Experiment: ", required=True)
    obs_sample__sample_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sample ID'}),
                                            help_text="Sample ID (Unique):", required=True)
    obs_sample__sample_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sample Type'}),
                                              help_text="Sample Type:", required=False)
    obs_sample__sample_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sample Name'}),
                                              help_text="Sample Name:", required=False)
    stock__seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Seed ID'}),
                                     help_text="Source Seed ID:", required=False)
    obs_plot__plot_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plot ID'}),
                                      help_text="Source Plot ID:", required=False)
    obs_plant__plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plant ID'}),
                                          help_text="Source Plant ID:", required=False)
    source_sample_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Sample ID'}),
                                       help_text="Source Sample ID:", required=False)
    obs_sample__weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Weight'}),
                                         help_text="Weight (g):", required=False)
    obs_sample__volume = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Volume'}),
                                         help_text="Volume (mL):", required=False)
    obs_sample__density = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Density'}),
                                          help_text="Density (g/mL):", required=False)
    obs_sample__kernel_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Num Kernels'}),
                                             help_text="Number of Kernels:", required=False)
    obs_sample__photo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Photo'}),
                                        help_text="Photo Filename:", required=False)
    obs_sample__comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}),
                                           help_text="Additional comments:", required=False)


class LogEnvironmentsOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        required=True)
    environment_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Environment ID'}), required=True)
    field = forms.ModelChoiceField(queryset=Field.objects.all(), initial=Field.objects.get(id=1),
                                   empty_label="--- Field Name ---", required=True)
    longitude = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Longitude'}), required=False)
    latitude = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Latitude'}), required=False)
    environment_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}), required=False)


class LogTissuesOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        required=True)
    tissue_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tissue ID'}), required=True)
    plot_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plot ID'}), required=False)
    seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Seed ID'}), required=False)
    plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plant ID'}), required=False)
    culture_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Culture ID'}), required=False)
    tissue_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tissue Name'}), required=False)
    tissue_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tissue Type'}), required=False)
    date_ground = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Date Ground'}), required=False)
    tissue_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}), required=False)


class LogCulturesOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        required=True)
    culture_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Culture ID'}), required=True)
    medium = forms.ModelChoiceField(queryset=Medium.objects.all(), empty_label="--- Medium ---", required=True)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label="--- Location ---", required=True)
    plot_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plot ID'}), required=False)
    seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Seed ID'}), required=False)
    plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plant ID'}), required=False)
    tissue_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Tissue ID'}), required=False)
    microbe_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Microbe ID'}), required=False)
    culture_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Culture Name'}), required=False)
    microbe_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Microbe Type'}), required=False)
    plating_cycle = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plating Cycle'}), required=False)
    dilution = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Dilution'}), required=False)
    num_colonies = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Num Colonies'}), required=False)
    num_microbes = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Num Microbes'}), required=False)
    image = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Image'}), required=False)
    culture_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}), required=False)


class LogMicrobesOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        required=True)
    microbe_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Microbe ID'}), required=True)
    plot_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plot ID'}), required=False)
    seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Seed ID'}), required=False)
    plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plant ID'}), required=False)
    tissue_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Tissue ID'}), required=False)
    culture_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Culture ID'}), required=False)
    microbe_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Microbe Type'}), required=False)
    microbe_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}), required=False)


class LogDNAOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        required=True)
    dna_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'DNA ID'}), required=True)
    microbe_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Microbe ID'}), required=False)
    plot_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plot ID'}), required=False)
    seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Seed ID'}), required=False)
    plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plant ID'}), required=False)
    tissue_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Tissue ID'}), required=False)
    culture_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Culture ID'}), required=False)
    plate_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plate ID'}), required=False)
    well_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Well ID'}), required=False)
    sample_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Sample ID'}), required=False)
    extraction = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Extraction'}), required=False)
    date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Date'}), required=False)
    tube_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tube ID'}), required=False)
    tube_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tube Type'}), required=False)
    dna_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}), required=False)


class LogWellOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        required=True)
    well_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Well ID'}), required=True)
    microbe_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Microbe ID'}), required=False)
    plot_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plot ID'}), required=False)
    seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Seed ID'}), required=False)
    plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plant ID'}), required=False)
    tissue_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Tissue ID'}), required=False)
    culture_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Culture ID'}), required=False)
    plate_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plate ID'}), required=False)
    well = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Well'}), required=False)
    inventory = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Inventory'}), required=False)
    tube_label = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tube Label'}), required=False)
    well_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}), required=False)


class LogMaizeSurveyOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        required=True)
    maize_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Maize ID'}), required=True)
    county = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'County'}), required=False)
    sub_location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sub Location'}), required=False)
    village = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Village'}), required=False)
    weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Weight'}), required=False)
    harvest_date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Harvest Date'}), required=False)
    storage_months = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Storage Months'}), required=False)
    storage_conditions = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Storage Conditions'}),
                                         required=False)
    maize_variety = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Maize Variety'}), required=False)
    seed_source = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Seed Source'}), required=False)
    moisture_content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Moisture Content'}),
                                       required=False)
    source_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Type'}), required=False)
    appearance = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Appearance'}), required=False)
    gps_latitude = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'GPS Latitude'}), required=False)
    gps_longitude = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'GPS Longitude'}), required=False)
    gps_altitude = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'GPS Altitude'}), required=False)
    gps_accuracy = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'GPS Accuracy'}), required=False)
    photo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Photo Filename'}), required=False)


class LogPlatesOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        required=True)
    plate_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plate ID'}), required=True)
    location_id = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label="--- Location Name ---",
                                         required=True)
    plate_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plate Name'}), required=False)
    date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Date'}), required=False)
    contents = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Contents'}), required=False)
    rep = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Rep'}), required=False)
    plate_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plate Type'}), required=False)
    plate_status = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plate Status'}), required=False)
    plate_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}), required=False)


class LogSeparationsOnlineForm(forms.Form):
    sample_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sample ID'}), required=True)
    sample_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sample Name'}), required=False)
    separation_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Separation Type'}), required=False)
    apparatus = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apparatus'}), required=False)
    sg = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Specific Gravity'}), required=False)
    light_weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Light Weight'}), required=False)
    medium_weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Medium Weight'}), required=False)
    heavy_weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Heavy Weight'}), required=False)
    light_percent = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Light Percent'}), required=False)
    medium_percent = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Medium Percent'}), required=False)
    heavy_percent = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Heavy Percent'}), required=False)
    operating_factor = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Operating Factor'}),
                                       required=False)
    separation_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}), required=False)


class LogIsolateStocksOnlineForm(forms.Form):
    isolatestock__isolatestock_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'IsolateStock ID'}),
                                                    help_text="IsolateStock ID:", required=True)
    isolatestock__isolatestock_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'IsolateStock Name'}),
        help_text="IsolateStock Name:", required=False)
    isolatestock__plant_organ = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Plant Organ'}),
                                                help_text="Plant Organ:", required=False)
    isolatestock__comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}),
                                             help_text="Additional Comments:", required=False)
    isolatestock__locality = forms.ModelChoiceField(queryset=Locality.objects.all(),
                                                    empty_label="--- Locality Name ---",
                                                    help_text="Locality:", required=True)
    # Temporarily Disabled
    # field = forms.ModelChoiceField(queryset=Field.objects.all(), empty_label="--- Source Field Name ---",
    #                                help_text="Source Field Name:", required=True)

    # Passport Information -- Collecting model
    isolatestock__passport__collecting__user = forms.ModelChoiceField(queryset=User.objects.all(),
                                                               empty_label="--- Collected By ---",
                                                               initial=User.objects.get(username='unknown_person'),
                                                               help_text="Collector", required=True)
    isolatestock__passport__collecting__collection_date = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Collection Date'}), help_text="Date Collected", required=False)
    isolatestock__passport__collecting__collection_method = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Collection Method'}), help_text="Collection Method",
        required=False)
    isolatestock__passport__collecting__comments = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Collection Comments'}), help_text="Collection Comments",
        required=False)

    # Passport Information -- Taxonomy model
    isolatestock__passport__taxonomy__binomial = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Binomial'}),
        help_text="Binomial:", required=False)
    isolatestock__passport__taxonomy__alias = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Alias'}),
                                                              help_text="Alias:", required=False)
    isolatestock__passport__taxonomy__race = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Race'}),
                                                             help_text="Race:", required=False)
    isolatestock__passport__taxonomy__subtaxa = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subtaxa'}),
        help_text="Subtaxa:", required=False)

    # Passport Information -- People model (Used as the "source" of the stock)
    isolatestock__passport__people__first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source First Name'}), help_text="Source First Name",
        required=False)
    isolatestock__passport__people__last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source Last Name'}), help_text="Source Last Name", required=False)
    isolatestock__passport__people__organization = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source Organization'}), help_text="Source Organization",
        required=False)
    isolatestock__passport__people__phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source Phone'}),
        help_text="Source Phone", required=False)
    isolatestock__passport__people__email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source Email'}),
        help_text="Source Email", required=False)
    isolatestock__passport__people__comments = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Source Comments'}), help_text="Source Comments", required=False)

    # ObsTracker Related Fields
    obs_plot__plot_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plot ID'}),
                                      help_text="Source Plot ID:", required=False)
    stock__seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Seed ID'}),
                                     help_text="Source Seed ID:", required=False)
    obs_plant__plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Plant ID'}),
                                          help_text="Source Plant ID:", required=False)
    obs_tissue__tissue_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Source Tissue ID'}),
                                            help_text="Source Tissue ID:", required=False)




class LogIsolatesOnlineForm(forms.Form):
    isolate__isolate_id = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Isolate ID'}), help_text="Isolate ID:",
        required=True)
    isolate__isolatestock = forms.ModelChoiceField(queryset=IsolateStock.objects.all(), empty_label="--- Isolate Stock ---", help_text="Source IsolateStock ID:", required=True)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label="--- Storage Location ---",
                                      help_text="Storage Location:", required=True)
    isolate__locality = forms.ModelChoiceField(queryset=Locality.objects.all(), empty_label="--- Locality ---", help_text="Locality of the Isolate:", required=True)
    isolate__stock_date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Stock Date'}),
                                          help_text="Stock Date:", required=False)
    isolate__extract_color = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Extract Color'}),
                                             help_text="Extract Color:", required=False)
    isolate__organism = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Organism'}),
                                        help_text="Organism:", required=False)
    isolate__comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}),
                                        help_text="Comments:", required=False)



class UpdateIsolatesOnlineForm(forms.Form):
    isolate_id = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Isolate ID'}), help_text="Isolate ID:",
        required=True)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label="--- Storage Location ---",
                                      help_text="Storage Location:", required=True)
    locality = forms.ModelChoiceField(queryset=Locality.objects.all(), empty_label="--- Locality ---",
                                      help_text="Locality:", required=True)
    stock_date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Stock Date'}),
                                          help_text="Stock Date:", required=False)
    extract_color = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Extract Color'}),
                                             help_text="Extract Color:", required=False)
    organism = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Organism'}),
                                        help_text="Organism:", required=False)
    comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}),
                                        help_text="Comments:", required=False)


class LogMeasurementsOnlineForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        help_text="Choose the experiment that data is related to:", required=True)
    observation_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Model ID Being Measured'}), required=True)
    measurement_parameter = forms.ModelChoiceField(queryset=MeasurementParameter.objects.all(),
                                                   empty_label="--- Parameter ---", required=True)
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="--- Username ---", required=True)
    time_of_measurement = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Time of Measurement'}),
                                          required=False)
    value = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Value'}), required=True)
    measurement_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}), required=False)


class UploadQueueForm(forms.Form):
    experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---",
                                        help_text="Choose the experiment that data is related to:", required=False)
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="--- Username ---",
                                  help_text="Select the user who produced data:", required=True)
    file_name = forms.FileField(help_text="Select your file:")
    comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Comments'}),
                               help_text="Any additional comments:", required=False)
    verified = forms.BooleanField(help_text="Verified:", required=False)


class FieldBookUploadForm(forms.Form):
    supported_models = ['measurement']
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="--- Username ---",
                                  help_text="Select the user who produced data:", required=True)
    file_type = forms.ModelChoiceField(queryset=ContentType.objects.filter(name__in=supported_models), empty_label="--- Model type ---",
                               help_text="Select the model you're uploading info for:", required=True)
    file_name = forms.FileField(help_text="Select your file:")
    verified = forms.BooleanField(help_text="Verified:", required=False)
