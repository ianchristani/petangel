from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('lost/', views.lostList, name = 'lostList'),
    path('found/', views.foundList, name = 'foundList'),
    path('new/', views.newEvent, name = 'newEvent'),
    path('update/<int:id>', views.updateEvent, name = 'updateEvent'),
    path('delete/<int:id>', views.deleteEvent, name = 'deleteEvent'),
    path('event/<int:id>', views.specificEvent, name = 'specificEvent'),
    path('possiblecandidates/', views.possibleCandidates, name = 'possibleCandidates'),
]