from doctor.models import ClinicSaatlar
from clinic.models import Clinic
from django import template
# Create your views here.

register = template.Library()

@register.filter
def clinicsaatlar(id):
    doctor = Doctor.objects.get(pk=id)
    clinicsaat = ClinicSaatlar.objects.filter(doctors=doctor)

    return clinicsaat
