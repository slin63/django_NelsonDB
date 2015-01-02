from django.conf.urls import patterns,url
from metamaize import views

# calls django.conf.urls.url()
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^pedigree/$', views.pedigree, name='pedigree'),
	url(r'^row/$', views.row, name='row'),
	url(r'^person/$', views.person, name='person'),
	url(r'^culture/$', views.culture, name='culture'),
	url(r'^tissue/$', views.tissue, name='tissue'),
	)

