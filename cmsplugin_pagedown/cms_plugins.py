from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_pagedown.forms import PagedownForm
from cmsplugin_pagedown.models import PagedownConfig

from django.utils.translation import ugettext as _

class PagedownPlugin(CMSPluginBase):
    form = PagedownForm
    model = PagedownConfig
    name = _("Pagedown Markdown")
    render_template = "cmsplugin_pagedown/markdown.html"
    admin_preview = False
    
    def render(self, context, instance, placeholder):
        return {
            'text' : instance, 
        }

plugin_pool.register_plugin(PagedownPlugin)