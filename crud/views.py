from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import EventModel
from .forms import EventForm
from .searcher.searcher import eventSearcher


# lost pets page
def lostList(request):
    events = EventModel.objects.all().order_by("-date")
    candidates = eventSearcher(request.user)
    amountResults = len(candidates)
    return render(request, "lostlist.html", {"eventsToTemplate": events, "username": request.user, "amountOfCandidates": amountResults})

# found pets page
def foundList(request):
    events = EventModel.objects.all().order_by("-date")
    candidates = eventSearcher(request.user)
    amountResults = len(candidates)
    return render(request, "foundlist.html", {"eventsToTemplate": events, "username": request.user, "amountOfCandidates": amountResults})

# the page to add a new event
def newEvent(request):
    newEventForm = EventForm(request.POST or None, request.FILES or None, initial = {'author': request.user})
    candidates = eventSearcher(request.user)
    amountResults = len(candidates)

    if newEventForm.is_valid():
        newEventForm.instance.author = request.user
        newEventForm.save()
        # aqui deve ter alguma confirmacao dq foi incluido o post
        return redirect("crud:lostList")
    
    # restricting the user's name options
    newEventForm.fields['author'].queryset = User.objects.filter(id = request.user.id)
    return render(request, "eventform.html", {"eventform": newEventForm, "amountOfCandidates": amountResults})

# the page to edit an event
def updateEvent(request, id):
    selectedEvent = EventModel.objects.get(id = id)
    newEventForm = EventForm(request.POST or None, request.FILES or None, instance = selectedEvent)
    candidates = eventSearcher(request.user)
    amountResults = len(candidates)

    if newEventForm.is_valid():
        newEventForm.save()
        return redirect("crud:lostList")
    
    return render(request, "eventform.html", {"eventform": newEventForm, "id": selectedEvent, "amountOfCandidates": amountResults})

# event deleter
def deleteEvent(request, id):
    selectedEvent = EventModel.objects.get(id = id)
    candidates = eventSearcher(request.user)
    amountResults = len(candidates)

    # deleting
    if request.method == "POST":        
        selectedEvent.delete()
        return redirect('crud:lostList')
    
    return render(request, 'eventdelete.html', {'eventtodelete': selectedEvent, "amountOfCandidates": amountResults})

# page to show the pic larger
def specificEvent(request, id):
    selectedEvent = EventModel.objects.get(id = id)
    candidates = eventSearcher(request.user)
    amountResults = len(candidates)
    if request.method == "GET":
        return render(request, "specificevent.html", {"event": selectedEvent, "id": selectedEvent, "amountOfCandidates": amountResults})
    else:
        return redirect("crud:lostList")
    
# page that contains the possible candidates
def possibleCandidates(request):
    candidates = eventSearcher(request.user)
    amountResults = len(candidates)
    return render(request, "possiblecandidates.html", {"possCandidates": candidates, "amountOfCandidates": amountResults})