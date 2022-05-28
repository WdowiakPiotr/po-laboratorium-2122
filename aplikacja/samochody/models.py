from datetime import datetime
from distutils.text_file import TextFile
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Model(models.Model):
    model_auta=models.CharField(max_length=10)
    rok_produkcji=models.DateTimeField(default=datetime.now)
    kolor=models.CharField(max_length=20)
    DIESEL = 'ON'
    PETROL = 'PB'
    GAS = 'LPG'
    choice=[(DIESEL,'ON'),
    (PETROL,'PB'),(GAS,'LPG')]

    rodzaj_paliwa = models.CharField(
        max_length=3,
        choices=choice,
        default=None,
    )
    moc_silniak=models.DecimalField(max_digits=7,decimal_places=3)
    def __str__(self):
        return f'{self.model_auta}'


class Brand(models.Model):
    marka=models.CharField(max_length=10)
    model=models.ForeignKey(Model, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f'{self.marka}'


class Dealer(models.Model):
    marka=models.ForeignKey(Brand, on_delete=models.CASCADE,blank=True,null=True)
    nazwa=models.CharField(max_length=20)
    miasto=models.CharField(max_length=20)
    adres=models.CharField(max_length=20)
    nr_ulicy=models.IntegerField(default=0)
    def __str__(self):
        return f'{self.marka}'


class Service(models.Model):
    marka=models.ForeignKey(Brand, on_delete=models.CASCADE,blank=True,null=True)
    model_auta=models.ManyToManyField(Model)
    nazwa_uslugi=models.CharField(max_length=20)
    opis_uslugi=models.TextField(max_length=200)
    data=models.DateTimeField(default=0)
    kwota=models.IntegerField(default=0)
    def __str__(self):
        return f'{self.nazwa_uslugi}'
