from django.contrib import admin
from clinic.models import Clinic, Gallery, Sertifikat, XidmetlerPrices, DiaqnostikalarPrices
# Register your models here.

admin.site.register(Clinic)
admin.site.register(Gallery)
admin.site.register(Sertifikat)
admin.site.register(XidmetlerPrices)
admin.site.register(DiaqnostikalarPrices)
