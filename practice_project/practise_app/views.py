from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    name = "Aakash"
    return render(request,"index.html",{'name':name})

def about(request):
    return render(request,"about.html")

def welcome(request):
    greeting = "Edubridge"
    return render(request,"welcome.html",{'greeting':greeting})
# Create your views here.
