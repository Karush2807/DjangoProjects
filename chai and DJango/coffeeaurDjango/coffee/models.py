#production level pr bhi jo hm models bnayenge vo, app pr hi bnegi!!
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class coffee_varieties(models.Model):
    COFFEE_TYPE_CHOICE=[
        ('CAP', 'Capachino'),
        ('BC', 'Black Coffee'),
        ('CC', 'Cold Coffee'),
        ('EX', 'Espresso'),
        ('Pc', 'Plane Coffee')
    ]
    name=models.CharField(max_length=100)#this sets max length to 100
    image=models.ImageField(upload_to='coffees/') #ese hi images upload hoti hai
    date=models.DateTimeField(default=timezone.now)
    type= models.CharField(max_length=3, choices=COFFEE_TYPE_CHOICE) #to ye bs upar wali choices lega
    description=models.TextField(default='') #this is a text field

    def __str__(self):
        return self.name


# one to many models!!

class coffee_review(models.Model):
    coffee=models.ForeignKey(coffee_varieties, on_delete=models.CASCADE) #ye coffee_varieties se connect krega, on-delet decide krea ki review delete hoga to coffee kya hoga
    user=models.ForeignKey(User, on_delete=models.CASCADE) #ye user se connect krega
    date=models.DateTimeField(default=timezone.now)
    rating=models.IntegerField(default=1)
    review=models.TextField(default='')

    def __str__(self):
        return self.coffee.name + ' - ' + self.user.username


# many to many models