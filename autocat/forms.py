from dal import autocomplete

from django import forms
from .models import *



class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('__all__')
        widgets = {
            'birth_country': autocomplete.ModelSelect2(url='country-autocomplete',
            attrs={
                'theme': 'bootstrap'
            })
        }
