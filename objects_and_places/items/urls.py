# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from items.views import (
    PlaceGalleryView,
    VideoSlideshowView,
)


urlpatterns = patterns('',
    # url(r'^places/$', PlacesView.as_view()),
    url(r'places/(?P<place_name>\w+)/(?P<place_id>\d+)/$', PlaceGalleryView.as_view()),
    url(r'video/$', VideoSlideshowView.as_view()),

    # url(r'^objects/$', ObjectsView.as_view()),
    # url(r'^objects/(?P<object_name>)/(?P<object_id>)/$', ObjectGalleryView.as_view()),
)
