# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'schedule.views.home', name='home'),
    url(r'^$', 'schedule_app.views.schedule_page', name='schedule_page'),
    url(r'^group_(?P<id>\d{1,2})/$', 'schedule_app.views.group_page', name='group_page'),
    url(r'^teacher_(?P<id>\d{1,2})/$', 'schedule_app.views.teacher_page', name='teacher_page'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) 