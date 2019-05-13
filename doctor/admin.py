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
    search_fields = ('first_name', 'last_name', )
    list_display = ['first_name','last_name','gender','qebula_yazilma','image']
    list_display_links = ['first_name','last_name','gender','qebula_yazilma']
    inlines = [SertifikatTabularInline,ClinicSaatlarTabularInline,InsurancePackageTabularInline]
    class Meta:
        model = Doctor



admin.site.register(Doctor, DoctorAdmin )
admin.site.register(Review)
admin.site.register(Profession)
