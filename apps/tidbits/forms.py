from django.forms.models import inlineformset_factory
from tidbits.models import Tidbit, TidbitUrl

__author__ = 'ceposta'

from django import forms

class HomepageTidbitForm(forms.ModelForm):

    class Meta:
        model = Tidbit

class TidbitUrlForm(forms.ModelForm):
    class Meta:
        model = TidbitUrl
        fields = ('url', )

