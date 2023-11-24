from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from crud.searcher.searcher import eventSearcher

# main page
def index(request):
    return render(request, "index.html")

# registering page
def signup_view(request):
    if request.method == "POST":
        signupForm = UserCreationForm(request.POST)

        #registering and login in the user
        if signupForm.is_valid():
            validatedUser = signupForm.save()
            login(request, validatedUser)
            return redirect("crud:lostList")
    else:
        signupForm = UserCreationForm()
    return render(request, "signup.html", {"signupform": signupForm})

# login page
def login_view(request):
    if request.method == "POST":
        authForm = AuthenticationForm(data = request.POST)

        # login in the user
        if authForm.is_valid():
            validatedUser = authForm.get_user()
            login(request, validatedUser)
            return redirect("crud:lostList")
    else:
        authForm = AuthenticationForm()
    return render(request, "login.html", {"authform": authForm}) 

# logout page
def logout_view(request):
    candidates = eventSearcher(request.user)
    amountResults = len(candidates)
    if request.method == "POST":
        logout(request)
        return redirect("users:index")
    else:
        return render(request, "logout.html", {"username": request.user, "amountOfCandidates": amountResults})