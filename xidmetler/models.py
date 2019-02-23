from django.db import models


class Xidmetler(models.Model):
     name = models.CharField(max_length=256)
     description = models.TextField(max_length=10000, null=True)

     def __str__(self):
         return self.name
