from tkinter.tix import Form


from django import forms
from .models import *
class Form(forms.ModelForm):
    class Meta:
        model = Model
        fields = "__all__"
