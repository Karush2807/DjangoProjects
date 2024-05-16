#main logic yhi likha jayga, poora program ka hmara!!

from django.http import  HttpResponse

#this will be home page of our django page
def home(request):
    return HttpResponse("namaste, duniya!!")

#this will be about page of our django page
def about(request):
    return HttpResponse("about page")

#this will be contact page of our django page
def contact(request):
    return HttpResponse("contact page")
