from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=10000,blank=True, null=True)

    def __str__(self):
        return self.name
