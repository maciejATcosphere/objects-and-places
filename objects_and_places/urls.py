# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^base', include('items.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)