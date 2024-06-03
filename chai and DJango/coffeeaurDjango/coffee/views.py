from django.shortcuts import render
from .models import coffee_varieties, Store_Name
from django.shortcuts import get_object_or_404 
from .forms import CoffeeVarietyForm #yhn jis naam se form ki class create hogi, use import kiya hai!!

# Create your views here.
def all_coffee(request):
    coffees= coffee_varieties.objects.all() #ye db pr query krega, arryas aayenge
    return render(request, 'coffee/all_coffee.html', {'coffees':coffees}) #ab front-end mein values aajaynegi!!


def coffee_detail(request, coffee_id):
    coffee=get_object_or_404(coffee_varieties, pk=coffee_id) #ye db pr query krega, arryas aayenge
    return render(request, 'coffee/coffee_details.html', {'coffee':coffee})


#Any request that could be used to change the state of the system - for example, a request that makes changes in the database - should use POST.
#GET should be used only for requests that do not affect the state of the system.

def coffee_Store_view(request):
    stores=None
    # if this is a POST request we need to process the form data

    if request.method=='POST':
        # create a form instance and populate it with data from the request:

        form=CoffeeVarietyForm(request.POST)
        if form.is_valid():
            coffee_variety=form.cleaned_data['coff_var'] #ye name, form.py se aaya hai
            stores=Store_Name.objects.filter(coff_varieties=coffee_variety) #ye db pr query krega, arryas aayenge , jinpr stores pr availabe hogi whi show honge bs
    else:
        form=CoffeeVarietyForm()

    
    return render(request, 'coffee/coffee_stores.html', {'stores':stores, 'form':form})
