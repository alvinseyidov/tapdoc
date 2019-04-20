from django.contrib import admin
from doctor.models import Doctor, Review, Clinic, Profession,Sertifikat

class SertifikatTabularInline(admin.TabularInline):
    model = Sertifikat

class DoctorAdmin(admin.ModelAdmin):
    exclude = ('wishlist',)
    inlines = [SertifikatTabularInline]
    class Meta:
        model = Doctor

admin.site.register(Doctor, DoctorAdmin )
admin.site.register(Review)
admin.site.register(Profession)
