#main logic yhi likha jayga, poora program ka hmara!!

from django.http import  HttpResponse
from django.shortcuts import render #used for redering the templates file

#this will be home page of our django page
def home(request):
    #return HttpResponse("namaste, duniya!!")
    return render (request, 'website/index.html')

#this will be about page of our django page
def about(request):
    #return HttpResponse("about page")
    return render (request, 'website/about.html' )

#this will be contact page of our django page
def contact(request):
    #return HttpResponse("contact page")
    return render (request, 'website/contact.html')