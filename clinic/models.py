from django.db import models
from service.models import Xidmatlar, Diaqnostikalar
from clinic.widgets import *
from ckeditor.fields import RichTextField

# Create your models here.


class Clinic(models.Model):
    MERKEZ = 'MRK'
    FILIAL = 'FLL'

    CLINIC_TYPES = (
        (MERKEZ, 'Merkez'),
        (FILIAL, 'filial')
    )

    type = models.CharField(max_length=25, choices=CLINIC_TYPES, null=True, blank=True)
    name = models.CharField(max_length=256)
    xidmetler = models.ManyToManyField(Xidmatlar, through='XidmetlerPrices',related_name='relate_name_xidmetler', blank=True)
    diaqnostikalar = models.ManyToManyField(Diaqnostikalar, through='DiaqnostikalarPrices',related_name='relate_name_diaqnostikalar', blank=True)
    filial = models.ForeignKey('self', related_name='filiallar', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=256)
    description = RichTextField(blank=True, null=True)
    descriptionmeta = models.TextField(max_length=256,blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    location = LocationField(blank=True, max_length=255)
    metro1 = models.CharField(max_length=256,null=True, blank=True)
    metro2 = models.CharField(max_length=256,null=True, blank=True)


    def __str__(self):
        return self.name


class XidmetlerPrices(models.Model):
    xidmet = models.ForeignKey(Xidmatlar, on_delete=models.CASCADE)
    klinika = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    qiymet = models.CharField(max_length=64)

    def __str__(self):
        return self.klinika.name + ' - ' + self.xidmet.name + ' - ' + self.qiymet

class DiaqnostikalarPrices(models.Model):
    diaqnostika = models.ForeignKey(Diaqnostikalar, on_delete=models.CASCADE)
    klinika = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    qiymet = models.CharField(max_length=64)

    def __str__(self):
        return self.klinika.name + ' - ' + self.diaqnostika.name + ' - ' + self.qiymet


class Gallery(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True)
    clinic = models.ForeignKey(Clinic, related_name='gallery', on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class Sertifikat(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True)
    clinic = models.ForeignKey(Clinic, related_name='sertifikatlar', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
