from django.contrib import admin
from .models import Car,Service,Dealer

# Register your models here.
admin.site.register(Car)
admin.site.register(Service)
admin.site.register(Dealer)