from django.shortcuts import render
from .models import coffee_varieties, Store_Name
from django.shortcuts import get_object_or_404 
from .forms import CoffeeVarietyForm

# Create your views here.
def all_coffee(request):
    coffees= coffee_varieties.objects.all() #ye db pr query krega, arryas aayenge
    return render(request, 'coffee/all_coffee.html', {'coffees':coffees}) #ab front-end mein values aajaynegi!!


def coffee_detail(request, coffee_id):
    coffee=get_object_or_404(coffee_varieties, pk=coffee_id) #ye db pr query krega, arryas aayenge
    return render(request, 'coffee/coffee_details.html', {'coffee':coffee})

def coffee_Store_view(request):
    stores=None
    if request.method=='POST':
        form=CoffeeVarietyForm(request.POST)
        if form.is_valid():
            coffee_variety=form.cleaned_data['coff_var'] #ye name, form.py se aaya hai
            stores=Store_Name.objects.filter(coff_varieties=coffee_variety) #ye db pr query krega, arryas aayenge  
    else:
        form=CoffeeVarietyForm()

    
    return render(request, 'coffee/coffee_stores.html', {'stores':stores, 'form':form})
