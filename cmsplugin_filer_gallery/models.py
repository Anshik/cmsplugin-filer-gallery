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
    animation = models.SmallIntegerField(choices=ANIMATION_CHOICES)
    speed = models.SmallIntegerField(default=600)
    timer = models.BooleanField(default=True)
    advanced_speed = models.IntegerField(default=4000)
    pause_on_hover = models.BooleanField(default=True)
    start_on_mouseout = models.BooleanField(default=True)
    start_after = models.IntegerField(default=1000)
    directional_nav = models.BooleanField(default=False)
    captions = models.BooleanField(default=False)
    caption_animation = models.SmallIntegerField(choices=CAPTION_ANIMATION_CHOICES, null=True, blank=True)
    caption_speed = models.SmallIntegerField(default=800)
    bullets = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = _("django filer gallery")
        verbose_name_plural = _("django filer galleries")