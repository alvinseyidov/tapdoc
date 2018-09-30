from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Clinic(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    description = models.TextField(max_length=10000, null=True)

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    clinics = models.ManyToManyField(Clinic, related_name='doctors')
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=10000, null=True)
    professions = models.ManyToManyField(Profession, related_name='doctors')
    wishlist = models.ManyToManyField(User, related_name='wishlist', blank=True)


    def __str__(self):
        return self.first_name


class Review(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='reviews', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    star = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True)
    message = models.TextField(max_length=4000)
    clinic = models.ForeignKey(Clinic, related_name='reviews', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message
