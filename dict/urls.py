from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('sets/', views.sets, name='Sets'),
    path('sets/create/', views.createSet, name='createSet'),
    path('sets/edit/(?P<set_id>[\d]+)', views.editSet, name='editSet'),
    path('sets/delete/(?P<set_id>[\d]+)', views.deleteSet, name='deleteSet'), 
    path('sets/view/(?P<set_id>[\d]+)', views.viewSet, name='viewSet'),
    path('entrys/create/(?P<set_id>[\d]+)', views.createEntry, name='createEntry'),
    path('entrys/edit/(?P<entry_id>[\d]+)', views.editEntry, name='editEntry'),
    path('entrys/delete/(?P<entry_id>[\d]+)', views.deleteEntry, name='deleteEntry'),
]

