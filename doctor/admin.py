from django.contrib import admin
from doctor.models import Doctor, Review, Clinic, Profession,Sertifikat,ClinicSaatlar,InsurancePackage
from django.template.loader import render_to_string

class SertifikatTabularInline(admin.TabularInline):
    model = Sertifikat

class ClinicSaatlarTabularInline(admin.TabularInline):
    model = ClinicSaatlar

class InsurancePackageTabularInline(admin.TabularInline):
    model = InsurancePackage

class DoctorAdmin(admin.ModelAdmin):
    exclude = ('wishlist',)
    search_fields = ('first_name', 'last_name', )
    list_display = ['first_name','last_name','qebula_yazilma','get_products','thumb']

    def thumb(self, obj):
        return  render_to_string('thumb.html',{
                    'image': obj.image
                })

    thumb.allow_tags = True

    def get_products(self, obj):
        return "\n".join([p.name for p in obj.clinics.all()])


    list_display_links = ['first_name','last_name','qebula_yazilma']
    inlines = [SertifikatTabularInline,ClinicSaatlarTabularInline,InsurancePackageTabularInline]
    class Meta:
        model = Doctor



admin.site.register(Doctor, DoctorAdmin )
admin.site.register(Review)
admin.site.register(Profession)
