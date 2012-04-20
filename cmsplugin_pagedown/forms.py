from django import forms
from pagedown.widgets import AdminPagedownWidget
from cmsplugin_pagedown.models import PagedownConfig

class PagedownForm(forms.ModelForm):
    markdown = forms.CharField(widget=AdminPagedownWidget())
    
    class Meta:
        exclude = ("html", "plaintext")
        model = PagedownConfig