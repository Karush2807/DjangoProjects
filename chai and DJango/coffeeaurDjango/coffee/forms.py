from django import forms
from .models import coffee_varieties #kyunki isi model se data lena hai, nd saari varieties isi mein available hai

class CoffeeVarietyForm(forms.Form):
    coff_var= forms.ModelChoiceField(queryset=coffee_varieties.objects.all(),
                                    label="Select Coffee Variety") #queryset=coffee_varieties.objects.all() is used to get all the data from the model