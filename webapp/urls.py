from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^metamaize/', include('metamaize.urls')),
    url(r'^$', include('lab.urls')),
    url(r'^lab/', include('lab.urls')),
    url(r'^legacy/', include('legacy.urls')),
    url(r'^admin/', include(admin.site.urls))
)

if settings.DEBUG:
	urlpatterns += patterns(
			'django.views.static',
			(r'media/(?P<path>.*)',
			'serve',
			{'document_root': settings.MEDIA_ROOT}), )
