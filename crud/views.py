from django.shortcuts import render, redirect
from .models import EventModel
from .forms import EventForm
from django.contrib.auth.models import User



# the default page for auth users
def eventList(request):
    events = EventModel.objects.all().order_by("-date")
    return render(request, "list.html", {"eventsToTemplate": events, "username": request.user})

# the page to add a new event
def newEvent(request):
    newEventForm = EventForm(request.POST or None, request.FILES or None, initial={'author': request.user})

    if newEventForm.is_valid():
        newEventForm.instance.author = request.user
        newEventForm.save()
        # aqui deve ter alguma confirmacao dq foi incluido o post
        return redirect("crud:eventList")
    
    # restricting the user's name options
    newEventForm.fields['author'].queryset = User.objects.filter(id = request.user.id)
    return render(request, "eventform.html", {"eventform": newEventForm})

# the page to edit an event
def updateEvent(request, id):
    selectedEvent = EventModel.objects.get(id = id)
    newEventForm = EventForm(request.POST or None, request.FILES or None, instance = selectedEvent)

    if newEventForm.is_valid():
        newEventForm.save()
        return redirect("crud:eventList")
    
    return render(request, "eventform.html", {"eventform": newEventForm, "id": selectedEvent})

# event deleter
def deleteEvent(request, id):
    selectedEvent = EventModel.objects.get(id = id)
    # deleting
    if request.method == "POST":
        selectedEvent.delete()
        return redirect('crud:eventList')
    
    return render(request, 'eventdelete.html', {'eventtodelete': selectedEvent})