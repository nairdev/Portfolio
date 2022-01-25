from importlib.resources import contents
import re
from django.shortcuts import render, HttpResponse
from django.template import context
from Home.models import Contact

# Create your views here.

def home(request):
    #return HttpResponse ("This is my home page corresponding to http://127.0.0.1:8000")
    context = {'name':'Devi Nair', 'city':'Waterloo'}
    return render(request, 'home.html', context)

def about(request):
    #return HttpResponse ("This is my web page corresponding to http://127.0.0.1:8000/about")
    return render(request, 'about.html')

def projects(request):
    #return HttpResponse ("This is my web page corresponding to http://127.0.0.1:8000/projects")
    return render(request, 'projects.html')

def resources(request):
    #return HttpResponse ("This is my web page corresponding to http://127.0.0.1:8000/resources")
    return render(request, 'resources.html')

def contact(request):
    #return HttpResponse ("This is my web page corresponding to http://127.0.0.1:8000/contact") 
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        contact_instance = Contact(name = name, email = email, phone = phone, message = message)
        contact_instance.save()
        print ("The data has been saved into the db")
    return render(request, 'contact.html')