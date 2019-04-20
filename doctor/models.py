from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from clinic.models import Clinic

from ckeditor.fields import RichTextField


# Create your models here.




class Profession(models.Model):
    name = models.CharField(verbose_name='İxtisas adı',default='İxtisas Adı', max_length=256)
    description = models.TextField(max_length=10000, verbose_name='Qısa Məlumat', blank=True, null=True)


    def __str__(self):
        return self.name



class Doctor(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER = (
        (MALE, 'Kişi'),
        (FEMALE, 'Qadın')
    )
    gender = models.CharField(verbose_name='Həkimin Cinsi', max_length=25, choices=GENDER, null=True, blank=True)
    first_name = models.CharField(verbose_name='Həkimin Adı', max_length=256,null=True, blank=True)
    last_name = models.CharField(verbose_name='Həkimin Soyadı', max_length=256,null=True, blank=True)
    title = models.CharField(verbose_name='Həkimin titulu', max_length=256,null=True, blank=True)
    tecrube = models.IntegerField(verbose_name='Həkimin Təcrübəsi', null=True, blank=True)
    contact_phone = models.CharField(verbose_name='Qəbul Üçün Telefon', max_length=256,null=True, blank=True)
    qebula_yazilma = models.CharField(verbose_name='Həkimin Qəbulu Qiyməti', max_length=256,null=True, blank=True)
    qebula_yazilma_endirim_faiz = models.CharField(verbose_name='Həkim Qəbulu Endirim %-lə', max_length=256,null=True, blank=True)
    clinics = models.ManyToManyField(Clinic, verbose_name='İşlədiyi Klinikalar',  related_name='doctors')
    image = models.ImageField(verbose_name='Profil Şəkli', null=True, blank=True)
    description = RichTextField(verbose_name='Həkim Haqqında Ətraflı Məlumat', blank=True, null=True)
    wishlist = models.ManyToManyField(User, related_name='wishlist', blank=True)
    professions = models.ManyToManyField(Profession,verbose_name='Həkimin İxtisasları',  related_name='doctors')



    def __str__(self):
        return self.first_name +' ' + self.last_name



class Sertifikat(models.Model):
    image = models.ImageField(null=True, blank=True)
    doctor = models.ForeignKey(Doctor, related_name='sertifikatlar', on_delete=models.CASCADE)




class Review(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='reviews', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    clinic = models.ForeignKey(Clinic,on_delete=models.CASCADE,blank=True, null=True)
    star = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True)
    message = models.TextField(max_length=4000)
    published = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], null=True)
    def __str__(self):
        return self.doctor.first_name +' '+self.doctor.last_name+' - ' + self.message
