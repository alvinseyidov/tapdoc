from django.contrib import admin
from .models import Xidmatlar,XidmatlarGroup, DiaqnostikalarGroup, Diaqnostikalar
# Register your models here.

admin.site.register(Xidmatlar)
admin.site.register(XidmatlarGroup)
admin.site.register(Diaqnostikalar)
admin.site.register(DiaqnostikalarGroup)
