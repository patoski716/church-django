from django.contrib import admin

# Register your models here.
from .models import *

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name',  'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email')
  list_per_page = 25

class DonateAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name',  'email', 'contact_date')
  list_display_links = ('id', 'first_name')
  search_fields = ('first_name', 'email')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)
admin.site.register(Donate, DonateAdmin)
