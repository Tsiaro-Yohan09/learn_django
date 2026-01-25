from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login

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

    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # print(email)
        # print(password)
        # print('>> DEBUG USER', user)
        if user is not None:
            login(request, user)
            return redirect("home")
        
        else:
            return HttpResponse(user)
            # return HttpResponse("Mot de passe ou email invalide")
         
    return render(request, "login.html")   
    # template = loader.get_template("login.html")
    # return HttpResponse(template.render())

def home(request):
    template = loader.get_template("home/index.html")
    
    return HttpResponse(template.render())
    # return render(request, template)
    # return HttpResponse("Hello bonjour")
