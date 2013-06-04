from django.conf.urls import patterns, include, url, static
from socialnetwork.views import sign,login
from socialnetwork import settings
from User.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', login),
    (r'^signin/$', login),
    (r'^signup/$', sign),
    (r'^next/$', get_info),
    (r'^profile/$', signin),
    url(r'', include('django.contrib.staticfiles.urls')),
#    (r'^media/(?P</home/pearl/Desktop/project/socialnetwork/template>.*)$','django.views.static.serve',                                  {'document_root':settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'socialnetwork.views.home', name='home'),
    # url(r'^socialnetwork/', include('socialnetwork.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
