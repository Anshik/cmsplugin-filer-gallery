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
             'animation': instance.get_animation_display(),                     # fade, horizontal-slide, vertical-slide, horizontal-push
             'animationSpeed': instance.speed,                                  # how fast animations are
             'timer': instance.timer,                                           # True or False to have the timer
             'advanceSpeed': instance.advanced_speed,                           # if timer is enabled, time between transitions 
             'pauseOnHover': instance.pause_on_hover,                           # if you hover pauses the slider
             'startClockOnMouseOut': instance.start_on_mouseout,                # if clock should start on MouseOut
             'startClockOnMouseOutAfter': instance.start_after,                 # how long after MouseOut should the timer start again
             'directionalNav': instance.directional_nav,                        # manual advancing directional navs
             'captions': instance.captions,                                     # do you want captions?
             'captionAnimation': instance.aption_animation and 
                 instance.get_caption_animation_display() or 'none',             # fade, slideOpen, none
             'captionAnimationSpeed': instance.caption_speed,                   # if so how quickly should they animate in
             'bullets': instance.bullets                                        # True or False to activate the bullet navigation
        })
        context.update({
            'instance': instance,
            'size': (instance.height, instance.width),
            'orbit_config': config
        })
        return context

plugin_pool.register_plugin(FilerGalleryPlugin)