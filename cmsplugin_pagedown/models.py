from django.db import models
from django.template.defaultfilters import striptags
from cms.models import CMSPlugin
import markdown 

class PagedownConfig(CMSPlugin):
    markdown = models.TextField()
    html = models.TextField()
    plaintext = models.TextField()
    
    def save(self, *args, **kwargs):
        self.html = markdown.markdown(self.markdown)
        self.plaintext = striptags(self.html)
        super(PagedownConfig, self).save(args, kwargs)
        
    def __unicode__(self):
        return self.plaintext[:50]
    
    @property
    def wordcount(self):
        return len(self.plaintext)