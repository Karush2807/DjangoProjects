#production level pr bhi jo hm models bnayenge vo, app pr hi bnegi!!
from django.db import models
from django.utils import timezone

# Create your models here.
class coffee_varieties(models.Model):
    name=models.CharField(max_length=100)#this sets max length to 100
    image=models.ImageField(upload_to='coffees/') #ese hi images upload hoti hai
    date=models.models.DateTimeField(default=timezone.now)
    
