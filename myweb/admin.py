from django.contrib import admin
from .models import Thaistory, CountryStory, Destination

admin.site.register(Destination)
admin.site.register(Thaistory)
admin.site.register(CountryStory)