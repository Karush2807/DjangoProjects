from django import forms #imported the form class of Django
from .models import coffee_varieties #coffee varieties model, consists of the necessary detials required in form submission

class CoffeeVarietyForm(forms.Form): #new model class created
    
    
    # Dropdown field for selecting a coffee variety
    coff_var = forms.ModelChoiceField(
        queryset=coffee_varieties.objects.all(),
        label="Select Coffee Variety"
    )
