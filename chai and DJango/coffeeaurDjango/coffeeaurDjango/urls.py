"""
URL configuration for coffeeaurDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#ROOT_URLCONF = "coffeeaurDjango.urls"
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static #seetings mein se, media path ko load krega!!
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('coffee/', include('coffee.urls')), #ye app mein transfer krenge

    #path('coffee/', include('coffeeaurDjango.urls')),


    #path("__reload__/", include("django_browser_reload.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #ye additonal line added, khud se likhna pdega

