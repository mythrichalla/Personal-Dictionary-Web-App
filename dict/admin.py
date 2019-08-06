from django.contrib import admin
from .models import Set, Entry

class SetAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']

class EntryAdmin(admin.ModelAdmin):
    pass 


# Register your models here.
admin.site.register(Set, SetAdmin)
admin.site.register(Entry, EntryAdmin)

