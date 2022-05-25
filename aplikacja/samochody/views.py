import django
from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.
class Carview(generic.ListView):
    model=Car
    template_name='Car_list.html'
    def get_queryset(self):
        return Car.objects.all()
    
class Dealerview(generic.ListView):
    model=Dealer
    template_name='Dealer_list.html'
    def get_queryset(self):
        return Dealer.objects.all()
    
class Serviceview(generic.ListView):    
    model=Service
    template_name='Service_list.html'
    def get_queryset(self):
        return Service.objects.all()