from django.contrib import admin
from doctor.models import Doctor, Review, Clinic, Profession,Sertifikat,ClinicSaatlar,InsurancePackage

class SertifikatTabularInline(admin.TabularInline):
    model = Sertifikat

class ClinicSaatlarTabularInline(admin.TabularInline):
    model = ClinicSaatlar

class InsurancePackageTabularInline(admin.TabularInline):
    model = InsurancePackage

class DoctorAdmin(admin.ModelAdmin):
    exclude = ('wishlist',)
    inlines = [SertifikatTabularInline,ClinicSaatlarTabularInline,InsurancePackageTabularInline]
    class Meta:
        model = Doctor


admin.site.register(Doctor, DoctorAdmin )
admin.site.register(Review)
admin.site.register(Profession)
