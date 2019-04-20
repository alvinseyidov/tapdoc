from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from service.models import Xidmatlar, Diaqnostikalar
from django.contrib.auth.models import User
from clinic.widgets import *
from ckeditor.fields import RichTextField



# Create your models here.

DEFAULT = 'default.jpg'
class Clinic(models.Model):
    MERKEZ = 'MRK'
    FILIAL = 'FLL'

    CLINIC_TYPES = (
        (MERKEZ, 'Merkez'),
        (FILIAL, 'filial')
    )

    type = models.CharField(max_length=25,verbose_name='Klinika Növü', choices=CLINIC_TYPES, null=True, blank=True)
    name = models.CharField(max_length=256, verbose_name='Klinika Adı', blank=True, null=True)
    xidmetler = models.ManyToManyField(Xidmatlar, verbose_name='Xidmətlər və qiymətləri', through='XidmetlerPrices',related_name='relate_name_xidmetler', blank=True)
    diaqnostikalar = models.ManyToManyField(Diaqnostikalar,verbose_name='Diaqnostik Xidmətlər və qiymətləri',  through='DiaqnostikalarPrices',related_name='relate_name_diaqnostikalar', blank=True)
    filial = models.ForeignKey('self', verbose_name='Aid olduğu mərkəz klinika', related_name='filiallar', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=256,verbose_name='Klinika Ünvanı' , blank=True, null=True)
    phone = models.CharField(max_length=256,verbose_name='Əlaqə Telefonu', blank=True, null=True)
    description = RichTextField(verbose_name='Klinika Profil Məlumatı', blank=True, null=True)
    descriptionmeta = models.TextField(max_length=256,verbose_name='Klinika Kard Məlumatı', blank=True, null=True)
    image = models.ImageField(verbose_name='Profil Şəkli', default=DEFAULT, null=True, blank=True)
    location = LocationField(verbose_name='Klinika Xəritədə Yeri', blank=True, max_length=255)
    be_cm_issaati = models.CharField(verbose_name='BE - Cümə İş Saatı', max_length=256,null=True, blank=True)
    sn_issaati = models.CharField(verbose_name='Şənbə İş Saatı', max_length=256,null=True, blank=True)
    bz_issaati = models.CharField(verbose_name='Bazar İş Saatı', max_length=256,null=True, blank=True)
    metro1 = models.CharField(verbose_name='Yaxın Olduğu 1-ci Metro', max_length=256,null=True, blank=True)
    metro1distance = models.CharField(verbose_name='1-ci Metroya olan Məsafə', max_length=256,null=True, blank=True)
    metro2 = models.CharField(verbose_name='Yaxın Olduğu 2-ci Metro', max_length=256,null=True, blank=True)
    metro2distance = models.CharField(verbose_name='2-ci Metroya olan Məsafə', max_length=256,null=True, blank=True)
    wishlist = models.ManyToManyField(User, related_name='clinicwishlist', blank=True)


    def __str__(self):
        return self.name
    def set_image_to_default(self):
        self.image.delete(save=False)  # delete old image file
        self.image = DEFAULT
        self.save()

class XidmetlerPrices(models.Model):
    xidmet = models.ForeignKey(Xidmatlar,verbose_name='Xidmətin Adı', on_delete=models.CASCADE, related_name='qiymetler')
    klinika = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    qiymet = models.CharField(verbose_name='Qiymət',max_length=64)

    def __str__(self):
        return self.klinika.name + ' - ' + self.xidmet.name + ' - ' + self.qiymet

class DiaqnostikalarPrices(models.Model):
    diaqnostika = models.ForeignKey(Diaqnostikalar, verbose_name='Diaqnpstik Xidmətin Adı',on_delete=models.CASCADE,  related_name='qiymetler')
    klinika = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    qiymet = models.CharField(verbose_name='Adı',max_length=64)

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
