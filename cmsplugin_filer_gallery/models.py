# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin, Page

class FilerGallery(CMSPlugin):
                     )
    gallery = models.ForeignKey('filer_gallery.Gallery')

    class Meta:
        verbose_name = _("django filer gallery")
        verbose_name_plural = _("django filer galleries")
