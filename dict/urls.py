from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('sets/', views.sets, name='Sets'),
    path('sets/create/', views.createSet, name='createSet'),
    re_path(r'sets/edit/(?P<set_id>[\d]+)', views.editSet, name='editSet'),
    re_path(r'sets/delete/(?P<set_id>[\d]+)', views.deleteSet, name='deleteSet'), 
    re_path(r'sets/view/(?P<set_id>[\d]+)', views.editTerms, name='editEntries'),
    re_path(r'sets/viewComplete/(?P<set_id>[\d]+)', views.viewCompleteSet, name='viewCompleteSet'),
    re_path(r'entrys/create/(?P<set_id>[\d]+)', views.createEntry, name='createEntry'),
    re_path(r'entrys/edit/(?P<entry_id>[\d]+)', views.editEntry, name='editEntry'),
    re_path(r'entrys/delete/(?P<entry_id>[\d]+)', views.deleteEntry, name='deleteEntry'),
]

# from django.conf.urls import url

# from . import views

# urlpatterns = [
#     url(r'^$', views.home, name='Home'),
#     url(r'about/', views.about, name = 'About'),
#     url(r'sets/', views.sets, name = 'Sets'),
#     url(r'sets/create/', views.createSet, name = 'createSet'),
#     url(r'sets/edit/(?P<set_id>[\d]+)', views.editSet, name='editSet'),
#     url(r'sets/delete/(?P<set_id>[\d]+)', views.deleteSet, name='deleteSet'),
#     url(r'sets/view/(?P<set_id>[\d]+)', views.editTerms, name='editEntries'),
#     url(r'sets/viewComplete/(?P<set_id>[\d]+)', views.viewCompleteSet, name='viewCompleteSet'),
#     url(r'entrys/create/(?P<set_id>[\d]+)', views.createEntry, name='createEntry'),
#     url(r'entrys/edit/(?P<entry_id>[\d]+)', views.editEntry, name='editEntry'),
#     url(r'entrys/delete/(?P<entry_id>[\d]+)', views.deleteEntry, name='deleteEntry'),
# ]