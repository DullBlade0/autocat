from dal import autocomplete

from django import forms




class PersonForm(forms.ModelForm):
    birth_country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=autocomplete.ModelSelect2(url='country-autocomplete')
    )

    class Meta:
        model = Person
        fields = ('__all__')