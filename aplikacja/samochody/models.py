from django.db import models

# Create your models here.
class Car(models.Model):
    marka=models.CharField(max_length=50)
    rok_produkcji=models.IntegerField(default=0)
    kolor=models.CharField(max_length=20)
    rodzaj_paliwa=models.CharField(max_length=6)
    moc_silniak=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.marka}'
class Dealer(models.Model):
    marka=models.ForeignKey(Car, on_delete=models.CASCADE,blank=True,null=True)
    nazwa=models.CharField(max_length=20)
    miasto=models.CharField(max_length=20)
    adres=models.CharField(max_length=20)
    ulica_nr=models.CharField(max_length=10)
    def __str__(self):
        return f'{self.nazwa}'


class Service(models.Model):
    nazwa=models.ManyToManyField(Dealer)
    data=models.DateTimeField(default=0)
    kwota=models.IntegerField(default=0)
    def __str__(self):
        return f'{self.data}'


