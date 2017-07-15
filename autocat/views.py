from django.shortcuts import render
from django.views.generic import CreateView

from dal import autocomplete

from .models import Country, Person

# Create your views here.
class PersonCreateView(CreateView):
    model = Person
    fields = ('__all__')
    template_name = 'person_form.html'

class CountryAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Country.objects.none()

        qs = Country.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)
        
        return qs
