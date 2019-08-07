from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Set, Entry
from .forms import SetForm, EntryForm
from django.forms import ModelForm
from django.forms.models import modelformset_factory, formset_factory

# Create your views here.
def home(request):
    return render (request, 'dictTemplates/home.html')  

def about(request): 
    return render (request, 'dictTemplates/about.html')

def sets(request):
    obj = Set.objects.order_by('title')
    context = {'sets': obj}
    return render (request, 'dictTemplates/sets.html', context)

def createSet(request):           # Template to accept POST requests to create new sets 
        if request.method == 'POST':
                # create a form and fill w/ data
                form = SetForm(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/sets')
        else:
                form = SetForm()

        context={'form':form}
        return render(request, 'dictTemplates/createAndEditSet.html', context)

def editSet(request, set_id):           # Template to edit sets
        set_obj=get_object_or_404(Set, id=set_id)       # Calls Set.objects.get(id being passed in) or returns 404 if DNE
        
        if request.method == 'POST':
                # create a form and fill w/ data
                form = SetForm(request.POST, instance=set_obj)  # everytime a form is edited, a copy of it is passed
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/sets')
        else:
                form = SetForm(instance=set_obj)

        context={'form':form, 'editing':True, 'set_obj':set_obj}
        return render(request, 'dictTemplates/createAndEditSet.html', context)

def deleteSet(request, set_id):
        set_obj=get_object_or_404(Set, id=set_id)
        set_obj.delete()
        return HttpResponseRedirect('/sets')

def viewSet(request, set_id):   # Returns the first card from the set (by default) from the database

        set_obj = get_object_or_404(Set, id=set_id)
        entry_list = set_obj.entry_set.all()
        entry_obj = entry_list.first()
        if request.method == 'GET' and 'entry' in request.GET:
                entry_obj = get_object_or_404(Entry, id=request.GET['entry'])
    
        context = {'set_obj': set_obj, 'entry_obj':entry_obj}
        return render (request, 'dictTemplates/viewSet.html', context)

def viewCompleteSet(request, set_id):
        set_obj=Set.objects.get(id=set_id)
        entry_list = set_obj.entry_set.order_by("term")
        
        context = {'set_obj': set_obj, 'entries':entry_list}
        return render (request, 'dictTemplates/viewCompleteSet.html', context)

def createEntry(request, set_id):
        set_obj = get_object_or_404(Set, id=set_id)
        if request.method == 'POST':
                # create a form and fill w/ data
                form = EntryForm(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/sets')
        else:
                form = EntryForm(initial={'set': set_obj})
                #return HttpResponse("Not reaching POST request")

        context={'form':form}
        return render(request, 'dictTemplates/createAndEditEntry.html', context)

def editEntry(request, entry_id):
        entry_obj = get_object_or_404(Entry, id = entry_id)
        if request.method == 'POST': 
                form = EntryForm(request.POST, instance=entry_obj)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/sets')

        else: 
                form = EntryForm(instance = entry_obj)
        context={'form':form, 'editing': True, 'entry_obj': entry_obj}
        return render(request, 'dictTemplates/createAndEditEntry.html', context)

def deleteEntry(request, entry_id):
        entry_obj=get_object_or_404(Entry, id=entry_id)
        entry_obj.delete()
        return HttpResponseRedirect('/sets')