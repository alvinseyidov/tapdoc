from service.models import Diaqnostikalar
from clinic.models import Clinic, DiaqnostikalarPrices
from django import template
# Create your views here.

register = template.Library()

@register.filter
def diaqnostikaspecificprice(diaqid,clinicid):
    clinic = Clinic.objects.get(pk=clinicid)
    diaqnostika = Diaqnostikalar.objects.get(pk=diaqid)
    price = DiaqnostikalarPrices.objects.filter(klinika=clinic, diaqnostika=diaqnostika)[:1].get()
    return price.qiymet
