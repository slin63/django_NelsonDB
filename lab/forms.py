from django import forms

from lab.models import UserProfile, Experiment, Field, ObsRow, ObsPlant, Locality, Stock, ObsRow, ObsPlant, ObsSample, ObsEnv, MeasurementParameter
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}), help_text="Choose a username:")
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}), validators=[EmailValidator], help_text="Enter your email:")
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}), help_text="Select a password:")
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}), help_text="First name:")
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}), help_text="Last name:")

	class Meta:
		model = User
		fields = ['username', 'password', 'email', 'first_name', 'last_name']

class UserProfileForm(forms.ModelForm):
	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone Number'}), help_text="Add your phone number:")
	organization = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Organization'}), help_text="Your affiliated organization:")
	job_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Job Title'}), help_text="Type your job title:")
	notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Notes','rows': '5', 'cols': '20'}), help_text="Add any notes about yourself:")
	website = forms.URLField(widget=forms.TextInput(attrs={'placeholder':'Website'}), help_text="(Optional) Your website: ", required=False)
	picture = forms.ImageField(widget=forms.ClearableFileInput(), help_text="(Optional) Select a profile image:", required=False)

	class Meta:
		model = UserProfile
		fields = ['phone','organization','job_title','notes','website', 'picture']

class ChangePasswordForm(forms.ModelForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Old Password'}), help_text="Type your old password:")
	new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'New Password'}), help_text="Select a new password:")
	new_password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Retype New Password'}), help_text="Retype your new password:")

	class Meta:
		model = User
		fields = []

class EditUserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}), help_text="Type your password:")
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}), validators=[EmailValidator], help_text="Edit your email:", required=False)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}), help_text="Change you first name:", required=False)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}), help_text="Change your last name:", required=False)

	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name']

class EditUserProfileForm(forms.ModelForm):
	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone Number'}), help_text="Edit your phone number:", required=False)
	organization = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Organization'}), help_text="Edit your affiliated organization:", required=False)
	job_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Job Title'}), help_text="Change your job title:", required=False)
	notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Notes','rows': '5', 'cols': '20'}), help_text="Modify any notes about yourself:", required=False)
	website = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Website'}), help_text="Change your website: ", required=False)
	picture = forms.ImageField(help_text="Change your profile image:", required=False)

	class Meta:
		model = UserProfile
		fields = ['phone', 'organization', 'job_title', 'notes', 'website', 'picture']

class NewExperimentForm(forms.Form):
	user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="--- Username ---", help_text="Select the primary user:", required=True)
	field = forms.ModelChoiceField(queryset=Field.objects.all(), empty_label="--- Field Name ---", help_text="Select a field or select 'No Field':", required=True)
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Experiment Name'}), help_text="Assign an experiment name (e.g. 15XY):", required=True)
	start_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Start Date'}), help_text="Give a start date:", required=True)
	purpose = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Purpose'}), help_text="Description of purpose:", required=True)
	comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments', 'rows': '5', 'cols': '20'}), help_text="Any additional comments:", required=False)

class NewTreatmentForm(forms.Form):
	experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---", help_text="Select the experiment:", required=True)
	treatment_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Treatment ID'}), help_text="Assign a unique ID for this treatment:", required=True)
	treatment_type = forms.CharField(widget=forms.DateInput(attrs={'placeholder':'Treatment Type'}), help_text="What kind of treatment (e.g. inoculation, fertilizer):", required=True)
	date = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Treatment Date'}), help_text="On what date was treatment (01-30-2015):", required=True)
	comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments', 'rows': '5', 'cols': '20'}), help_text="Any additional comments:" , required=False)

class NewFieldForm(forms.Form):
	locality = forms.ModelChoiceField(queryset=Locality.objects.all(), empty_label="--- Locality ---", help_text="Select the correct locality:", required=True)
	field_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Field Name'}), help_text="Give a field name:", required=True)
	field_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Field Num'}), help_text="What is the field number:", required=True)
	comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments'}), help_text="Any additional comments:", required=True)

class NewLocalityForm(forms.Form):
	city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City'}), help_text="Type a city name:", required=True)
	state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'State'}), help_text="What state is the city in:", required=True)
	country = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Country'}), help_text="What country is the state in:", required=True)
	zipcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Zipcode'}), help_text="Type the zipcode:", required=False)

class NewMeasurementParameterForm(forms.Form):
	parameter = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Parameter'}), help_text="Type a new parameter:", required=True)
	parameter_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Parameter Type'}), help_text="What type of parameter is this:", required=True)
	protocol = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Protocol'}), help_text="Give a description of the protocol:", required=True)
	trait_id_buckler = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Buckler Trait ID'}), help_text="Give Buckler trait ID if exists:", required=True)
	unit_of_measure = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Unit of Measure'}), help_text="What is the unit of measure:", required=True)

class NewLocationForm(forms.Form):
	locality = forms.ModelChoiceField(queryset=Locality.objects.all(), empty_label="--- Locality ---", help_text="Select the correct locality:", required=True)
	building_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Building Name'}), help_text="Type the building name:", required=True)
	location_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Location Name'}), help_text="Type the location name:", required=True)
	room = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Room'}), help_text="Type the room name or number:", required=True)
	shelf = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Shelf'}), help_text="Give the shelf name or number:", required=True)
	column = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Column'}), help_text="Give the column name or number:", required=True)
	box_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Box Name'}), help_text="Give the box name:", required=True)
	comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments'}), help_text="Any additional comments:", required=True)

class NewDiseaseInfoForm(forms.Form):
	common_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Common Name'}), help_text="Type the disease common name:", required=True)
	abbrev = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Abbreviation'}), help_text="Type the abbreviation:", required=True)
	comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments'}), help_text="Any additional comments:", required=True)

class NewTaxonomyForm(forms.Form):
	genus = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Genus'}), help_text="Type the genus:", required=True)
	species = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Species'}), help_text="Type the species:", required=True)
	population = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Population'}), help_text="Type the population:", required=True)
	common_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Common Name Type'}), help_text="This is currently either 'Maize' or 'Isolate':", required=True)
	alias = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Alias'}), help_text="Type the alias (historically for isolates):", required=True)
	race = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Race'}), help_text="Type the race (historically for isolates):", required=True)
	subtaxa = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Sub-taxa'}), help_text="Type the sub-taxa (historically for isolates):", required=True)

class LogSeedDataOnlineForm(forms.Form):
	seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Seed ID'}), required=True)
	seed_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Seed Name'}), required=True)
	cross_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Cross Type'}), required=True)
	pedigree = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Pedigree'}), required=True)
	stock_status = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Stock Status'}), required=True)
	stock_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Stock Date'}), required=True)
	inoculated = forms.BooleanField(required=False)
	stock_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments'}), required=False)
	genus = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Genus'}), required=True)
	species = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Species'}), required=True)
	population = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Population'}), required=True)
	collection_field = forms.ModelChoiceField(queryset=Field.objects.all(), empty_label="--- Field ---", required=True)
	collection_row = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Collection Row ID'}), required=False)
	collection_plant = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Collection Plant ID'}), required=False)
	collection_user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="--- Collected By ---", required=True)
	collection_date = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Collection Date'}), required=False)
	collection_method = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Collection Method'}), required=False)
	collection_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Collection Comments'}), required=False)
	source_fname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Source First Name'}), required=False)
	source_lname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Source Last Name'}), required=False)
	source_organization = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Source Organization'}), required=False)
	source_phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Source Phone'}), required=False)
	source_email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Source Email'}), required=False)
	source_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Source Comments'}), required=False)

class LogStockPacketOnlineForm(forms.Form):
	seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Seed ID'}), required=True)
	weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Weight'}), required=True)
	num_seeds = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Num Seeds'}), required=False)
	packet_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Packet Comments'}), required=False)
	locality = forms.ModelChoiceField(queryset=Locality.objects.all(), empty_label="--- Locality ---", required=True)
	building_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Building Name'}), required=True)
	location_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Location Name'}), required=True)
	room = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Room'}), required=False)
	shelf = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Shelf'}), required=False)
	column = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Column'}), required=False)
	box_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Box Name'}), required=False)
	location_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Location Comments'}), required=False)

class LogRowsOnlineForm(forms.Form):
	experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---", required=True)
	row_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Row ID'}), required=True)
	row_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Row Name'}), required=True)
	seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Seed ID'}), required=True)
	field = forms.ModelChoiceField(queryset=Field.objects.all(), empty_label="--- Field Name ---", required=True)
	range_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Range'}), required=False)
	plot = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Plot'}), required=False)
	block = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Block'}), required=False)
	rep = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Rep'}), required=False)
	kernel_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Kernel Num'}), required=False)
	planting_date = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Planting Date'}), required=False)
	harvest_date = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Harvest Date'}), required=False)
	row_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments'}), required=False)

class LogPlantsOnlineForm(forms.Form):
	experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---", required=True)
	plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Plant ID'}), required=True)
	plant_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Plant Num'}), required=True)
	seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Seed ID'}), required=False)
	row_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Row ID'}), required=False)
	plant_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments'}), required=False)

class LogSamplesOnlineForm(forms.Form):
	experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---", required=True)
	sample_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Sample ID'}), required=True)
	sample_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Sample Type'}), required=True)
	source_seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Source Seed ID'}), required=False)
	source_row_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Source Row ID'}), required=False)
	source_plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Source Plant ID'}), required=False)
	source_sample_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Source Sample ID'}), required=False)
	weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Weight'}), required=False)
	kernel_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Kernel Num'}), required=False)
	sample_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments'}), required=False)

class LogEnvironmentsOnlineForm(forms.Form):
	experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---", required=True)
	environment_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Environment ID'}), required=True)
	field = forms.ModelChoiceField(queryset=Field.objects.all(), empty_label="--- Field Name ---", required=True)
	longitude = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Longitude'}), required=False)
	latitude = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Latitude'}), required=False)
	environment_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments'}), required=False)

class LogMeasurementsOnlineForm(forms.Form):
	row_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Row ID'}), required=False)
	plant_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Plant ID'}), required=False)
	sample_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Sample ID'}), required=False)
	environment_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Environment ID'}), required=False)
	measurement_parameter = forms.ModelChoiceField(queryset=MeasurementParameter.objects.all(), empty_label="--- Parameter ---", required=True)
	user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="--- Username ---", required=True)
	time_of_measurement = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Time of Measurement'}), required=False)
	value = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Value'}), required=True)
	measurement_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments'}), required=False)

class UploadQueueForm(forms.Form):
	experiment = forms.ModelChoiceField(queryset=Experiment.objects.all(), empty_label="--- Experiment ---", help_text="Choose the experiment that data is related to:", required=True)
	user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="--- Username ---", help_text="Select the user who produced data:", required=True)
	file_name = forms.FileField(help_text="Select your file:")
	comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments'}), help_text="Any additional comments:", required=True)
