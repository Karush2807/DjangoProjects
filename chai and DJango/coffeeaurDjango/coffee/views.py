from django.shortcuts import render
from .models import coffee_varieties
from django.shortcuts import get_object_or_404 

# Create your views here.
def all_coffee(request):
    coffees= coffee_varieties.objects.all() #ye db pr query krega, arryas aayenge
    return render(request, 'coffee/all_coffee.html', {'coffees':coffees}) #ab front-end mein values aajaynegi!!


def coffee_detail(request, coffee_id):
    coffee=get_object_or_404(coffee_varieties, pk=coffee_id) #ye db pr query krega, arryas aayenge
    return render(request, 'coffee/description.html', {'coffee':coffee}, {'coffee_id':coffee})

