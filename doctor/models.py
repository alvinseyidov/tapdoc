from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from clinic.models import Clinic
from insurance.models import Company

from ckeditor.fields import RichTextField


# Create your models here.




class Profession(models.Model):
    name = models.CharField(verbose_name='İxtisas adı', max_length=256, null=True, blank=True)
    description = models.TextField(max_length=10000, verbose_name='Qısa Məlumat', blank=True, null=True)


    def __str__(self):
        return self.name


DEFAULT = 'defaultdoctor.png'
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
    evde_muayine = models.BooleanField(verbose_name='Evdə müayinə', null=True, blank=True)
    evde_muayine_qiymet = models.CharField(verbose_name='Evdə Müayinə Qiyməti', max_length=256,null=True, blank=True)
    usaq_hekimi = models.BooleanField(verbose_name='Uşaq həkimi?', null=True, blank=True)
    usaq_hekimi_qiymet = models.CharField(verbose_name='Uşaq Həkimi Müayinə Qiyməti', max_length=256,null=True, blank=True)
    qebula_yazilma = models.CharField(verbose_name='Həkimin Qəbulu Qiyməti', max_length=256,null=True, blank=True)
    qebula_yazilma_endirim_faiz = models.CharField(verbose_name='Həkim Qəbulu Endirim %-lə', max_length=256,null=True, blank=True)
    clinics = models.ManyToManyField(Clinic, verbose_name='İşlədiyi Klinikalar' , through='ClinicSaatlar', related_name='doctors', null=True, blank=True)
    company = models.ManyToManyField(Company, verbose_name='İşlədiyi Sığortalar' , through='InsurancePackage', related_name='doctors', null=True, blank=True)
    image = models.ImageField(verbose_name='Profil Şəkli', default=DEFAULT, null=True, blank=True)
    description = RichTextField(verbose_name='Həkim Haqqında Ətraflı Məlumat', blank=True, null=True)
    wishlist = models.ManyToManyField(User, related_name='wishlist', null=True, blank=True)
    professions = models.ManyToManyField(Profession,verbose_name='Həkimin İxtisasları',  related_name='doctors', null=True, blank=True)



    def __str__(self):
        return self.first_name +' ' + self.last_name
    def set_image_to_default(self):
        self.image.delete(save=False)  # delete old image file
        self.image = DEFAULT
        self.save()

class ClinicSaatlar(models.Model):
    clinic = models.ForeignKey(Clinic,verbose_name='Clinic', on_delete=models.CASCADE, related_name='hekimler', null=True, blank=True)
    bir_issaati = models.CharField(verbose_name='1-ci gün İş Saatı', max_length=256,null=True, blank=True)
    iki_issaati = models.CharField(verbose_name='2-ci gün İş Saatı', max_length=256,null=True, blank=True)
    uc_issaati = models.CharField(verbose_name='3-ci gün  İş Saatı', max_length=256,null=True, blank=True)
    dord_issaati = models.CharField(verbose_name='4-ci gün  İş Saatı', max_length=256,null=True, blank=True)
    bes_issaati = models.CharField(verbose_name='5-ci gün  İş Saatı', max_length=256,null=True, blank=True)
    sn_issaati = models.CharField(verbose_name='Şənbə İş Saatı', max_length=256,null=True, blank=True)
    bz_issaati = models.CharField(verbose_name='Bazar İş Saatı', max_length=256,null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.clinic.name

class InsurancePackage(models.Model):

    company = models.ForeignKey(Company,verbose_name='Company', on_delete=models.CASCADE, related_name='hekimler', null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.doctor.first_name


class Sertifikat(models.Model):
    image = models.ImageField(null=True, blank=True)
    doctor = models.ForeignKey(Doctor, related_name='sertifikatlar', on_delete=models.CASCADE, null=True, blank=True)




class Review(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='reviews', on_delete=models.CASCADE, null=True, blank=True)
    starter = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    clinic = models.ForeignKey(Clinic,on_delete=models.CASCADE,blank=True, null=True)
    star = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True)
    message = models.TextField(max_length=4000, null=True, blank=True)
    published = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], null=True, blank=True)
    def __str__(self):
        return self.doctor.first_name +' '+self.doctor.last_name+' - ' + self.message
