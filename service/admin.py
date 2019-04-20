from django.contrib import admin
from .models import Xidmatlar,XidmatlarGroup, DiaqnostikalarGroup, Diaqnostikalar
# Register your models here.
class XidmatlarTabularInline(admin.TabularInline):
    model = Xidmatlar

class XidmatlarGroupAdmin(admin.ModelAdmin):
    inlines = [XidmatlarTabularInline]
    class Meta:
        model = XidmatlarGroup

admin.site.register(XidmatlarGroup, XidmatlarGroupAdmin )




class DiaqnostikalarTabularInline(admin.TabularInline):
    model = Diaqnostikalar

class DiaqnostikalarGroupAdmin(admin.ModelAdmin):
    inlines = [DiaqnostikalarTabularInline]
    class Meta:
        model = DiaqnostikalarGroup

admin.site.register(DiaqnostikalarGroup, DiaqnostikalarGroupAdmin )
