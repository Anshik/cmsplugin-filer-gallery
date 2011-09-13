from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cmsplugin_filer_gallery.models import FilerGallery

class FilerGalleryPlugin(CMSPluginBase):
    model = FilerGallery
    name = _("Filer Gallery")
    render_template = "cmsplugin_filer_gallery/gallery.html"
    text_enabled = False
    raw_id_fields = ('gallery',)
    admin_preview = False
    
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance
        })
        return context

plugin_pool.register_plugin(FilerGalleryPlugin)