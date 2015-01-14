from django import forms

from lab.models import UserProfile, Experiment, Field, ObsRow, ObsPlant
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
	comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments', 'rows': '5', 'cols': '20'}), help_text="Any additional comments:")

class LogSeedDataOnlineForm(forms.Form):
	seed_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Seed ID'}), required=True)
	seed_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Seed Name'}), required=True)
	cross_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Cross Type'}), required=True)
	pedigree = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Pedigree'}), required=True)
	population = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Population'}), required=True)
	stock_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Stock Date'}), required=True)
	inoculated = forms.BooleanField()
	stock_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Comments'}), required=False)
	collection_field = forms.ModelChoiceField(queryset=Field.objects.all(), empty_label="--- Field ---", required=True)
	collection_row = forms.ModelChoiceField(queryset=ObsRow.objects.all()[:1000], empty_label="--- Row ID ---", required=True)
	collection_plant = forms.ModelChoiceField(queryset=ObsPlant.objects.all()[:1000], empty_label="--- Plant ID ---", required=True)
	collection_user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="--- Collected By ---", required=True)
	collection_date = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Collection Date'}), required=False)
	collection_method = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Collection Method'}), required=False)
	collection_comments = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Collection Comments'}), required=False)
