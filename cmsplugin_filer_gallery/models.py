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

    animation = models.SmallIntegerField(_("animation"), choices=ANIMATION_CHOICES, default=0)
    animateNumberActive = models.CharField(_("active number color"), default='#FF0000', max_length=7, help_text=_('Default #FF0000 red'))


    height = models.SmallIntegerField(_("height"),default=200)
    width = models.SmallIntegerField(_("width"), default=300)
    thumb_height = models.SmallIntegerField(_("thumbnail height"), null=True, blank=True, default=None, help_text=_('Leave empty for no thumbs.'))
    thumb_width = models.SmallIntegerField(_("thumbnail width"),null=True, blank=True, default=None, help_text=_('Leave empty for no thumbs.'))
    
    class Meta:
        verbose_name = _("django filer gallery")
        verbose_name_plural = _("django filer galleries")