import os
import csv

#----------------------------------------------------------------------------------------
#  Populates User and UserProfile Models using data from current people table. Adds a password of 123123 for all users and adds a default profile picture for all users.
#----------------------------------------------------------------------------------------

def csv_import_people():
	ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/person.csv'), dialect='excel')
	for row in ifile:
		user = row["user"]
		email = row["email"]
		first_name = row["first_name"]
		last_name = row["last_name"]
		phone = row["phone"]
		location = row["location"]
		title = row["title"]
		notes_file = row["notes"]
		web = row["web"]
		notes = "%s || %s" % (location, notes_file)

		add_user(user, email, first_name, last_name)
		add_userpass(user)
		add_userp(user, phone, location, 'profile_images/underwater.jpg', title, web, notes)
		print(user)

def add_user(username, email, fname, lname):
	u = User.objects.get_or_create(username=username, email=email, first_name=fname, last_name=lname)[0]
	return u

def add_userpass(user):
	pa = User.objects.get(username = user)
	pa.set_password('123123')
	pa.save()

def add_userp(user, phone, org, pic, title, web, notes):
	p = UserProfile.objects.get_or_create(user=User.objects.get(username=user), phone=phone, organization=org, picture=pic, job_title=title, website=web, notes=notes)[0]
	return p

#----------------------------------------------------------------------------------------
#  Populates ExperimentFactor and Experiment Models using data from current experiment table.
#----------------------------------------------------------------------------------------

def experiment_factor_pop():
	add_exp_factor('Example Experimental Factor', 'Field Experiment Factor', 'Disease Resistance Trial', 'This is simply an example of what an experiment_factor could be. Real experimental factors need to be added and linked to experiments. Or this ExperimentFactor table can be eliminated if it is not useful.')

def add_exp_factor(name, factor_type, description, comments):
	ef = ExperimentFactor.objects.get_or_create(factor_name=name, factor_type=factor_type, description=description, comments=comments)[0]
	return ef

def csv_import_experiment():
	ifile = csv.DictReader(open('C://Users/Nick/Documents/GitHub/django_NelsonDB/mine_project/mine_data/experiments.csv'), dialect='excel')
	for row in ifile:
		name = row["name"]
		date = row["date"]
		location = row["location"]
		user = row["person"]
		purpose = row["desc"]
		notes = row["notes"]
		tissue_collection = row["tissue_collection"]
		inoculations = row["inoculations"]
		inoculations_dates = "%s, %s, %s" % (row["inoculations_date1"], row["inoculations_date2"], row["inoculations_date3"])
		pathogen = row["pathogen"]
		comments = "Location: %s || Inoculations: %s || Inoculations Dates: %s || Pathogen: %s || Tissue_collection: %s || %s" % (location, inoculations, inoculations_dates, pathogen, tissue_collection, notes)

		add_experiment(name, date, user, purpose, comments)
		print(name)

def add_experiment(name, date, user, purpose, comments):
	e = Experiment.objects.get_or_create(factor=ExperimentFactor.objects.get(factor_name='Example Experimental Factor'), name=name, start_date=date, user=User.objects.get(username=user), purpose=purpose, comments=comments)[0]
	return e

#----------------------------------------------------------------------------------------
#  Populates
#----------------------------------------------------------------------------------------

def csv_import_seed():
		ifile = csv.DictReader(open('c://seed.csv'), dialect='excel')
		for row in ifile:
			tagname = row["Current_barcode"]
			timestamp = row["Timestamp_barcode"]
			weight = row["Weight (g)"]
			pedigree = row["Pedigree"]
			row_num = row["Row"]
			year = row["Year"]
			person = row["Person"]
			cross = row["Cross Type"]
			ear_num = row["Ear Num"]
			source_state = row["Source State"]
			source_name = row["Source Name"]
			source_year = row["Source Year"]
			population = row["Population"]
			box = row["NewStorageBox"]
			range_num = row["Range"]
			purpose = row["Purpose"]
			male_parent_name = row["Male_parent_name"]
			male_parent_id = row["male_parent_id"]

			add_taxonomy('Zea', 'Zea mays', 'mays', population, 'Maize')
			add_locality(source_name, source_state)
			add_field(source_name, source_state)
			add_collecting(source_name, source_state, person, source_year)
			add_passport(source_name, source_state, person, source_year, 'Zea', 'Zea mays', 'mays', population, 'Maize', pedigree)
			add_stock(source_name, source_state, person, source_year, 'Zea', 'Zea mays', 'mays', population, 'Maize', pedigree, cross, tagname, ear_num, year)
			add_stockpacket(timestamp, weight, box, source_name, source_state, person, source_year, 'Zea', 'Zea mays', 'mays', population, 'Maize', pedigree, cross, tagname, ear_num, year)

def table_pop():
		add_source('No Source')
		add_locality('Cold Storage', 'NY')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '1', '09JR_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '1', '09JR_Box002')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '2', '09,10,11JH_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '3', '11PR_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '3', '11PR_Box002')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '2', '11PR_Box003')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '4', '11PR_Box004')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '4', '11PR_Box005')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', '', '', '11PR_Box006')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', '', '', '11PR_Box007')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'A', '1', '07FL_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'A', '1', '05FL_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'A', '1', '05FL_Box002')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'A', '2', '08PN_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '5', '10SX01 10SX14')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '5', '11PR526-11PR545')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '5', '08SB')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '6', '07PK_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '6', '10SN+10SX')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '6', '10SX15 10SX20')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '3', '10PR_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '8', '12MY_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '8', '12MY_Box002')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '9', '12MY_Box003')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '9', '12MN_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '10', '09SX_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'B', '10', '06FL_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09JR_Box003')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '12MN_Box002')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09PN_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09PN_Box002')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09PN_Box003')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09PN_Box004')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09PN_Box005')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09PN_Box006')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09PN_Box007')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09PR_Box007')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09PR_Box008')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09PT_Box001')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09PT_Box002')
		add_location('Cold Storage Bldg 212', 'Freezer', '9', 'C', '', '09PT_Box003')

def add_source(name):
	so = Source.objects.get_or_create(source_name=name)
	return so

def add_taxonomy(genus, species, subspecies, population, common_name):
	t = Taxonomy.objects.get_or_create(genus=genus, species=species, subspecies=subspecies, population=population, common_name=common_name)[0]
	return t

def add_locality(name, state):
	l = Locality.objects.get_or_create(locality_name=name, state=state)[0]
	return l

def add_location(building, room, section, column, shelf, box):
	lo = Location.objects.get_or_create(locality=Locality.objects.get(locality_name='Cold Storage', state='NY'), building_name=building, room=room, section=section, column=column, shelf=shelf, box_name=box)
	return lo

def add_field(name, state):
	f = Field.objects.get_or_create(locality=Locality.objects.get(locality_name=name, state=state))[0]
	return f

def add_collecting(name, state, person, year):
	c = AccessionCollecting.objects.get_or_create(field=Field.objects.get(locality=Locality.objects.get(locality_name=name, state=state)), user=User.objects.get(username=person), collection_date=year)[0]
	return c

def add_passport(locality_name, state, person, year, genus, species, subspecies, population, common_name, pedigree):
	r = Passport.objects.get_or_create(source=Source.objects.get(source_name='No Source'), accession_collecting=AccessionCollecting.objects.get(field=Field.objects.get(locality=Locality.objects.get(locality_name=locality_name, state=state)), user=User.objects.get(username=person), collection_date=year), taxonomy=Taxonomy.objects.get(genus=genus, species=species, subspecies=subspecies, population=population, common_name=common_name), pedigree=pedigree)
	return r

def add_stock(locality_name, state, person, source_year, genus, species, subspecies, population, common_name, pedigree, cross, tagname, ear_num, year):
	s = Stock.objects.get_or_create(passport=Passport.objects.get(source=Source.objects.get(source_name='No Source'), accession_collecting=AccessionCollecting.objects.get(field=Field.objects.get(locality=Locality.objects.get(locality_name=locality_name, state=state)), user=User.objects.get(username=person), collection_date=source_year), taxonomy=Taxonomy.objects.get(genus=genus, species=species, subspecies=subspecies, population=population, common_name=common_name), pedigree=pedigree), cross_type=cross, stock_date=year, source_tagname=tagname, ear_num=ear_num)
	return s

def add_stockpacket(timestamp, weight, box, locality_name, state, person, source_year, genus, species, subspecies, population, common_name, pedigree, cross, tagname, ear_num, year):
	sp = StockPacket.objects.get_or_create(timestamp=timestamp, stock=Stock.objects.get(passport=Passport.objects.get(source=Source.objects.get(source_name='No Source'), accession_collecting=AccessionCollecting.objects.get(field=Field.objects.get(locality=Locality.objects.get(locality_name=locality_name, state=state)), user=User.objects.get(username=person), collection_date=source_year), taxonomy=Taxonomy.objects.get(genus=genus, species=species, subspecies=subspecies, population=population, common_name=common_name), pedigree=pedigree), cross_type=cross, stock_date=year, source_tagname=tagname, ear_num=ear_num), location=Location.objects.get(locality=Locality.objects.get(locality_name='Cold Storage', state='NY'), box_name=box), weight=weight)

#-------------------------------------------------------------------------
#  Start execution here!
#-------------------------------------------------------------------------

if __name__ == '__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_project.settings')
	from mine.models import Experiment, ExperimentFactor, User, UserProfile, Taxonomy, Locality, Field, Passport, AccessionCollecting, Source, Stock, StockPacket, Location
	csv_import_people()
	experiment_factor_pop()
	csv_import_experiment()
