from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import settings
#from fbook.friend import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fbook.views.home', name='home'),
    # url(r'^fbook/', include('fbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', TemplateView.as_view(template_name='base.htm'), name='index'),
    url(r'^admin', include(admin.site.urls)),
    url(r'^user/$', TemplateView.as_view(template_name='user.html'), name='user'),
    url(r'^(?P<username>\w+)/$', TemplateView.as_view(template_name='profile.html'), name='profile'),
    url(r'^(?P<username>\w+)/follower/$', TemplateView.as_view(template_name='follower.html'), name='follower'),
    url(r'^(?P<username>\w+)/following/$', TemplateView.as_view(template_name='following.html'), name='following')
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
