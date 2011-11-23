# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin, Page

ANIMATION_CHOICES=('fade', 'horizontal-slide', 'vertical-slide', 'horizontal-push')
ANIMATION_CHOICES=tuple(enumerate(ANIMATION_CHOICES))
CAPTION_ANIMATION_CHOICES=('fade', 'slideOpen')
CAPTION_ANIMATION_CHOICES=tuple(enumerate(CAPTION_ANIMATION_CHOICES))

class FilerGallery(CMSPlugin):

    gallery = models.ForeignKey('filer_gallery.Gallery')
    height = models.SmallIntegerField(default=200)
    width = models.SmallIntegerField(default=300)
    thumb_height = models.SmallIntegerField(null=True, blank=True, default=None, help_text='Leave empty for no thumbs.')
    thumb_width = models.SmallIntegerField(null=True, blank=True, default=None, help_text='Leave empty for no thumbs.')
    
    class Meta:
        verbose_name = _("django filer gallery")
        verbose_name_plural = _("django filer galleries")