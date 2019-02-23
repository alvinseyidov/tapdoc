from django.db import models
from xidmetler.models import Xidmetler
# Create your models here.

class Clinic(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    description = models.TextField(max_length=10000, null=True)
    image = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Clinic_branch(models.Model):
    clinic = models.ForeignKey(Clinic, related_name='branches', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    description = models.TextField(max_length=10000, null=True)
    image = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
