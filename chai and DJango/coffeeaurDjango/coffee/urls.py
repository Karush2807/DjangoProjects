
from django.urls import path, include
from . import views

# localhost:8000/coffee/
# localhost:8000/coffee/order
urlpatterns = [
    path('', views.all_coffee, name='all_coffee'),
    path('<int:coffee_id>/', views.coffee_detail, name='coffee_detail'),
    path('coffeeStores/', views.coffee_Store_view, name='coffee_Store'),

]
