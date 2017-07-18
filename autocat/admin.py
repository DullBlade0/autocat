from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    form = PersonForm

admin.site.register(Person, PersonAdmin)