from django.shortcuts import render
from .models import coffee_varieties

# Create your views here.
def all_coffee(request):
    coffees= coffee_varieties.objects.all() #ye db pr query krega, arryas aayenge
    return render(request, 'coffee/all_coffee.html', {'coffees':coffees}) #ab front-end mein values aajaynegi!!


