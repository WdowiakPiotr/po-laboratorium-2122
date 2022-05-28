import django
from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
# Create your views here.
class Modelview(generic.ListView):
    model=Model
    template_name='Model_list.html'
    def get_queryset(self):
        return Model.objects.all()
    
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

class Brandview(generic.ListView):    
    model=Brand
    template_name='Brand_list.html'
    def get_queryset(self):
        return Brand.objects.all()

def create_forms(request):
    form = Form(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "Forms.html", context)