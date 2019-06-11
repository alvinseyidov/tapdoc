from django.contrib import admin
from clinic.models import Clinic, Gallery, Sertifikat, XidmetlerPrices, DiaqnostikalarPrices, Review, City
from django.template.loader import render_to_string
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
    list_display = ['name','type','address','thumb']

    def thumb(self, obj):
        return  render_to_string('thumb.html',{
                    'image': obj.image
                })

    thumb.allow_tags = True

    list_display_links = ['name','type','address']

    inlines = [XidmetlerPricesTabularInline, DiaqnostikalarPricesTabularInline, GalleryTabularInline, SertifikatTabularInline]
    class Meta:
        model = Clinic

admin.site.register(Clinic, ClinicAdmin )


admin.site.register(Review)
admin.site.register(City)
