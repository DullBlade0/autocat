from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', PersonCreateView.as_view(), name='create-person'),
    url(r'^country-autocomplete/$', CountryAutocompleteView.as_view(), name='country-autocomplete'),
]