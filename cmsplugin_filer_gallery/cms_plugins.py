from django.utils.translation import ugettext_lazy as _
from django.utils import simplejson
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
        config = simplejson.dumps({
            'navigation': True,
            'interval': 2500,
            'numbers': True,
            'label': True,
            'animation': 'random',
            'thumbs': False,
            'hideTools': False,
            'dots': False,
            'easing_default': None,
            'velocity': 1,
            'animateNumberOut': {'backgroundColor':'#000', 'color':'#ccc'},
            'animateNumberOver': {'backgroundColor':'#000', 'color':'#ccc'},
            'animateNumberActive': {'backgroundColor':'#000', 'color':'#ccc'},
            'width_label': None,
            'show_randomly': False
            }
        )
        context.update({
            'instance': instance,
            'size': (instance.height, instance.width),
            'thumb_size': (instance.thumb_height, instance.thumb_width),
            'skitter_config': config
        })
        return context

plugin_pool.register_plugin(FilerGalleryPlugin)