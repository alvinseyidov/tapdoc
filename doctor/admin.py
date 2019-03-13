from django.contrib import admin
from doctor.models import Doctor, Review, Clinic, Profession,Sertifikat
# Register your models here.


admin.site.register(Doctor)
admin.site.register(Review)
admin.site.register(Profession)
admin.site.register(Sertifikat)
