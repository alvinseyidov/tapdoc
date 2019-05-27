from django.contrib import admin
from .models import  Xidmatlar, XidmatlarGroup, DiaqnostikalarGroup, Diaqnostikalar, Xidmat, Diaqnostika
from mptt.admin import DraggableMPTTAdmin
# Register your models here.
class XidmatlarTabularInline(admin.TabularInline):
    model = Xidmatlar

class XidmatlarGroupAdmin(admin.ModelAdmin):
    inlines = [XidmatlarTabularInline]
    class Meta:
        model = XidmatlarGroup

#admin.site.register(XidmatlarGroup, XidmatlarGroupAdmin )





class DiaqnostikalarTabularInline(admin.TabularInline):
    model = Diaqnostikalar

class DiaqnostikalarGroupAdmin(admin.ModelAdmin):
    inlines = [DiaqnostikalarTabularInline]
    class Meta:
        model = DiaqnostikalarGroup

#admin.site.register(DiaqnostikalarGroup, DiaqnostikalarGroupAdmin )
admin.site.register(
     Xidmat,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(
     Diaqnostika,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)
