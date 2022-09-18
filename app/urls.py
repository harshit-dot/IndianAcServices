from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('jabdjagdjahlduagdiuagdyuafdyagdygaudgauda', admin.site.urls),
    path('', views.main, name='main'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

]