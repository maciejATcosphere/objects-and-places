# -*- coding: utf-8 -*-

from django.contrib import admin
from items.models import Item, Image, Description

admin.site.register(Item)
admin.site.register(Image)
admin.site.register(Description)
