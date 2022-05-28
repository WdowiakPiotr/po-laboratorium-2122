from django.urls import URLPattern, path
from .views import *
app_name = 'cars'

urlpatterns=[
    path('models',Modelview.as_view(),name='index'),
    path('dealers',Dealerview.as_view(),name='index'),
    path('services',Serviceview.as_view(),name='index'),
    path('brands',Brandview.as_view(),name='index'),
    path('',create_forms),

]
