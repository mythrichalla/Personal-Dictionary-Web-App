from django.forms import ModelForm
from .models import Set, Entry

class SetForm(ModelForm):       # Form that maps to Set

    class Meta: 
        model = Set
        fields = ['title', 'description']

class EntryForm(ModelForm):
    class Meta: 
        model = Entry
        fields = ['set', 'term', 'definition']