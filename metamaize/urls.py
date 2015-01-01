from django.conf.urls import patterns,url
from metamaize import views

# calls django.conf.urls.url()
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'))

