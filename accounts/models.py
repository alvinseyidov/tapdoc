from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    ata_name = models.CharField(max_length=30,null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    qan_qrupu = models.CharField(max_length=30,null=True)
    gender = models.CharField(max_length=30,null=True)
    city = models.CharField(max_length=30,null=True)
    borndate = models.DateField(null=True, blank=True)
    konullu_sigorta_com = models.CharField(max_length=30, null=True, blank=True)
    konullu_sigorta_id = models.CharField(max_length=30, null=True, blank=True)
    icbari_sigorta_com = models.CharField(max_length=30, null=True, blank=True)
    icbari_sigorta_id = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.username
