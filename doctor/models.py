from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from clinic.models import Clinic

from ckeditor.fields import RichTextField


# Create your models here.




class Profession(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=10000,blank=True, null=True)


    def __str__(self):
        return self.name



class Doctor(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    gender = models.CharField(max_length=25, choices=GENDER, null=True, blank=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    title = models.CharField(max_length=256,null=True, blank=True)
    tecrube = models.IntegerField(null=True)
    contact_phone = models.CharField(max_length=256,null=True)
    qebula_yazilma = models.CharField(max_length=256,null=True)
    qebula_yazilma_endirim_faiz = models.CharField(max_length=256,null=True)
    clinics = models.ManyToManyField(Clinic, related_name='doctors')
    image = models.ImageField(null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    wishlist = models.ManyToManyField(User, related_name='wishlist', blank=True)
    professions = models.ManyToManyField(Profession, related_name='doctors')



    def __str__(self):
        return self.first_name



class Sertifikat(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True)
    doctor = models.ForeignKey(Doctor, related_name='sertifikatlar', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='reviews', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    clinic = models.ForeignKey(Clinic,on_delete=models.CASCADE,blank=True, null=True)
    star = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True)
    message = models.TextField(max_length=4000)
    published = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], null=True)
    def __str__(self):
        return self.doctor.first_name +' '+self.doctor.last_name+'-' + self.message
