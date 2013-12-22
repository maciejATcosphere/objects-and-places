# -*- coding: utf-8 -*-

import os

from django.views.generic import TemplateView

from items.models import Item


class PlacesView(TemplateView):
    pass


class PlaceGalleryView(TemplateView):
    template_name = 'place_gallery.html'

    def get(self, request, *args, **kwargs):
        place_id = kwargs['place_id']
        place = Item.objects.get(
            item_type='PLC', pk=place_id)

        images = place.image_set.all()
        images = [{
            'url': os.path.split(image.image.url)[1],
            'name': image.name} for image in images]

        context = self.get_context_data(**kwargs)
        context['place'] = place
        context['images'] = images
        return self.render_to_response(context)

class VideoSlideshowView(TemplateView):
    template_name = 'video_slideshow.html'

    def get(self, request, *args, **kwargs):
        videos = ['one', 'two', 'three', 'four']

        context = self.get_context_data(**kwargs)
        context['videos'] = videos
        return self.render_to_response(context)


class ObjectsView(TemplateView):
    pass


class ObjectGalleryView(TemplateView):
    pass

