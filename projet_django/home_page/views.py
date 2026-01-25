from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        email = request.POST["email"]
        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            first_name=first_name,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "auth/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        
        else:
            return HttpResponse(user)
         
            # return HttpResponse("Mot de passe ou email invalide")
         
    return render(request, "auth/login.html")

def home(request):
    return render(request, 'home/index.html')
