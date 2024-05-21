from django.shortcuts import render

# Create your views here.
def all_coffee(request):
    return render(request, 'coffee/all_coffee.html')
