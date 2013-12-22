# -*- coding: utf-8 -*-

import os

from django.db import models
from django.conf import settings


class Item(models.Model):
    OBJECT = 'OBJ'
    PLACE = 'PLC'
    ITEM_TYPE_CHOICES = (
        (OBJECT, 'object'),
        (PLACE, 'place'),
    )
    name = models.CharField(max_length=200)
    item_type = models.CharField(
        max_length=3, default=OBJECT, choices=ITEM_TYPE_CHOICES)

    def __unicode__(self):
        return self.name


class Image(models.Model):
    item = models.ForeignKey(Item)
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200,
        blank=True, null=True)
    keywords = models.CharField(max_length=400,
        blank=True, null=True)
    image = models.ImageField(upload_to=os.path.join(
        settings.MEDIA_ROOT, 'images'))

    def __unicode__(self):
        return self.name

class Description(models.Model):
    image = models.ManyToManyField(Image)
    title = models.CharField(max_length=200)
    text = models.TextField()
