from django.contrib import admin
from clinic.models import Clinic, Gallery, Sertifikat, XidmetlerPrices, DiaqnostikalarPrices, Review

# Register your models here.
class XidmetlerPricesTabularInline(admin.TabularInline):
    model = XidmetlerPrices

class DiaqnostikalarPricesTabularInline(admin.TabularInline):
    model = DiaqnostikalarPrices

class GalleryTabularInline(admin.TabularInline):
    model = Gallery

class SertifikatTabularInline(admin.TabularInline):
    model = Sertifikat

class ClinicAdmin(admin.ModelAdmin):
    exclude = ('wishlist',)
    inlines = [XidmetlerPricesTabularInline, DiaqnostikalarPricesTabularInline, GalleryTabularInline, SertifikatTabularInline]
    class Meta:
        model = Clinic

admin.site.register(Clinic, ClinicAdmin )


admin.site.register(Review)
