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

class Store_Name(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    coff_varieties=models.ManyToManyField(coffee_varieties, related_name='stores') #ye many to many relation bna dega, related_name se store kis coffee ka hai vo pta chalega

    def __str__(self):
        return self.name
    
# ye models bnane ke baad, hmne migrations bnani hai, jo db mein tables bnayegi

# one to one models

class coff_certificates(models.Model):
    coffee=models.OneToOneField(coffee_varieties, on_delete=models.CASCADE) #ye one to one relation bna dega
    certificate_number=models.CharField(max_length=100)
    issed_date=models.DateTimeField(default=timezone.now)
    valid_till=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Certificate for {self.coffee.name}"