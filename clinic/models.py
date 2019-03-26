from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from service.models import Xidmatlar, Diaqnostikalar
from django.contrib.auth.models import User
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
    phone = models.CharField(max_length=256,blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    descriptionmeta = models.TextField(max_length=256,blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    location = LocationField(blank=True, max_length=255)
    metro1 = models.CharField(max_length=256,null=True, blank=True)
    metro2 = models.CharField(max_length=256,null=True, blank=True)
    wishlist = models.ManyToManyField(User, related_name='clinicwishlist', blank=True)


    def __str__(self):
        return self.name


class XidmetlerPrices(models.Model):
    xidmet = models.ForeignKey(Xidmatlar, on_delete=models.CASCADE, related_name='qiymetler')
    klinika = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    qiymet = models.CharField(max_length=64)

    def __str__(self):
        return self.klinika.name + ' - ' + self.xidmet.name + ' - ' + self.qiymet

class DiaqnostikalarPrices(models.Model):
    diaqnostika = models.ForeignKey(Diaqnostikalar, on_delete=models.CASCADE,  related_name='qiymetler')
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


class Review(models.Model):
    clinic = models.ForeignKey(Clinic, related_name='clinicreviews', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='clinicreviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    star = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True)
    message = models.TextField(max_length=4000)

    published = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], null=True)
    def __str__(self):
        return self.clinic.name
