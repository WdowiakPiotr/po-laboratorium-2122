from django.contrib import admin
from .models import Brand, Model, Service, Dealer

# Register your models here.
admin.site.register(Model)
admin.site.register(Service)
admin.site.register(Dealer)
admin.site.register(Brand)