import os

def populate_person():
	user1 = add_user('unknown', 'unknown', 'unknown', 'unknown')
	userpa1 = add_userpass('unknown')
	userp1 = add_userp('unknown', '0000000000', 'unknown', 'profile_images/underwater.jpg', 'unknown', 'unknown')
	user2 = add_user('nm529', 'nmorales3142@gmail.com', 'Nicolas', 'Morales')
	userpa2 = add_userpass('nm529')
	userp2 = add_userp('nm529', '3216959465', 'Nelson Lab - Cornell University', 'profile_images/underwater.jpg', 'Lab Tech', 'Contracted until June 2015')
	user3 = add_user('cc435', 'cc435@cornell.edu', 'Chia-Lin', 'Chung')
	userpa3 = add_userpass('cc435')
	userp3 = add_userp('cc435', '0000000000', 'Nelson Lab - Cornell University', 'profile_images/underwater.jpg', 'PhD Student', '')
	user4 = add_user('rjw29', 'rjw29@cornell.edu', 'Randy', 'Wisser')
	userpa4 = add_userpass('rjw29')
	userp4 = add_userp('rjw29', '0000000000', 'Wisser Lab - Delaware University', 'profile_images/underwater.jpg', 'Alumni', '')
	user5 = add_user('jap226', 'jap226@cornell.edu', 'Jesse', 'Poland')
	userpa5 = add_userpass('jap226')
	userp5 = add_userp('jap226', '6072554783', 'Nelson Lab - Cornell University', 'profile_images/underwater.jpg', 'Alumni', '')
	user6 = add_user('sxm2', 'sxm2@cornell.edu', 'Santiago', 'Mideros')
	userpa6 = add_userpass('sxm2')
	userp6 = add_userp('sxm2', '6073398711', 'Nelson Lab - Cornell University', 'profile_images/underwater.jpg', 'PhD Student', '')
	user7 = add_user('jmk87', 'jmk87@cornell.edu', 'Judy', 'Kolkman')
	userpa7 = add_userpass('jmk87')
	userp7 = add_userp('jmk87', '0000000000', 'Nelson Lab - Cornell University', 'profile_images/underwater.jpg', 'Lab Manager', '')
	user8 = add_user('ooo7', 'ooo7@cornell.edu', 'Oliver', 'Ott')
	userpa8 = add_userpass('ooo7')
	userp8 = add_userp('ooo7', '4196306049', 'Nelson Lab - Cornell University', 'profile_images/underwater.jpg', 'Undergraduate Researcher', '')
	user9 = add_user('tmj35', 'tmj35@cornell.edu', 'Tiffany', 'Jamann')
	userpa9 = add_userpass('tmj35')
	userp9 = add_userp('tmj35', '4196306049', 'Nelson Lab - Cornell University', 'profile_images/underwater.jpg', 'PhD Student', '')
	user10 = add_user('lm596', 'lm596@cornell.edu', 'Laura', 'Morales')
	userpa10 = add_userpass('lm596')
	userp10 = add_userp('lm596', '6072372706', 'Nelson Lab - Cornell University', 'profile_images/underwater.jpg', 'PhD Student', '')

def populate_experiment():
	exp1 = add_experiment('Experiment Test 1', '2014-07-29', 'nm529', 'This is the first test of the experiment table', 'The experiment table holds name, date, username, purpose, and comments')
	exp2 = add_experiment('Experiment Test 2', '2014-07-29', 'nm529', 'Another test', 'The experiment table holds name, date, username, purpose, and comments')
	exp3 = add_experiment('Totally Different 3', '2014-07-29', 'nm529', 'Test number 3', 'The experiment table holds name, date, username, purpose, and comments')
	exp4 = add_experiment('05CN', '2005-05-09', 'cc435', 'NLB Trial', 'SEC 4.5, Row 165-249 in Margaret Smiths field plot')
	exp5 = add_experiment('06CN', '2006-05-24', 'cc435', 'NLB Trial', 'CC06_C, CC06_H, CC06_T, CC06_D')
	exp6 = add_experiment('07CA', '2007-05-23', 'cc435', 'ALB and ASR Trial', 'CC07_C_127-246')
	exp7 = add_experiment('07CG', '2007-05-08', 'unknown', '', '')


def add_user(username, email, fname, lname):
	u = User.objects.get_or_create(username=username, email=email, first_name=fname, last_name=lname)[0]
	return u
	
def add_userpass(user):
	pa = User.objects.get(username = user)
	pa.set_password('password1')
	pa.save()

def add_userp(user, phone, org, pic, title, notes):
	p = UserProfile.objects.get_or_create(user=User.objects.get(username=user), phone=phone, organization=org, picture=pic, job_title=title, notes=notes)[0]
	return p

def add_experiment(name, date, user, purpose, comments):
	e = Experiment.objects.get_or_create(name=name, experiment_date=date, user=User.objects.get(username=user), experiment_purpose=purpose, experiment_comments=comments)[0]
	return e	
	
def add_taxonomy(genus, species, subspecies, population, common_name):
	t = Taxonomy.objects.get_or_create(genus=genus, species=species, subspecies=subspecies, population=population, common_name=common_name)[0]
	return t

def add_locality(name, city, state, country, zip):
	l = Locality.objects.get_or_create(locality_name=name, city=city, state=state, country=country, zipcode=zip)[0]
	return l
	
def add_field(locality, name, number, latitude, longitude, altitude, comments):
	f = Field.objects.get_or_create(locality_id=Locality.objects.get(locality_name = locality), field_name = name, field_number = number, latitude = latitude, longitude=longitude, altitude = altitude, field_comments=comments)[0]
	return f


# Start execution here!
if __name__ == '__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_project.settings')
	from mine.models import Experiment, User, UserProfile, Taxonomy, Locality, Field, Passport, AccessionCollecting
	populate_person()
	populate_experiment()