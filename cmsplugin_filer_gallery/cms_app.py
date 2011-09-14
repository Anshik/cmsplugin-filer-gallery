from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class FilerGalleryApphook(CMSApp):
    name = _("Filer Gallery Apphook")
    urls = ["filer_gallery.urls"]

apphook_pool.register(FilerGalleryApphook)