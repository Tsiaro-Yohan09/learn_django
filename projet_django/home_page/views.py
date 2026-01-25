from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    template = loader.get_template("home.html")
    
    return HttpResponse(template.render())
    # return render(request, template)
    # return HttpResponse("Hello bonjour")
