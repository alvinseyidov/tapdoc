from django.contrib import admin
from doctor.models import Doctor, Review, Clinic, Profession,Sertifikat,ClinicSaatlar,InsurancePackage
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

class SertifikatTabularInline(admin.TabularInline):
    model = Sertifikat

class ClinicSaatlarTabularInline(admin.TabularInline):
    model = ClinicSaatlar

class InsurancePackageTabularInline(admin.TabularInline):
    model = InsurancePackage

class DoctorAdmin(admin.ModelAdmin):
    exclude = ('wishlist',)
    search_fields = ('first_name', 'last_name', )
    list_display = ['first_name','last_name','qebula_yazilma','klinika','thumb']
    readonly_fields = ['headshot_image']

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
            )
    )

    def thumb(self, obj):
        return  render_to_string('thumb.html',{
                    'image': obj.image
                })

    thumb.allow_tags = True

    def klinika(self, obj):
        return "\n".join([p.name for p in obj.clinics.all()])


    list_display_links = ['first_name','last_name','qebula_yazilma']
    inlines = [SertifikatTabularInline,ClinicSaatlarTabularInline,InsurancePackageTabularInline]
    class Meta:
        model = Doctor



admin.site.register(Doctor, DoctorAdmin )
admin.site.register(Review)
admin.site.register(Profession)
