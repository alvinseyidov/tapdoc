from doctor.models import Doctor
from clinic.models import Clinic
from doctor.models import ClinicSaatlar
from django import template
# Create your views here.

register = template.Library()

@register.filter
def reviewscount(id):
    doctor = Doctor.objects.get(pk=id)
    reviewcount = doctor.reviews.filter(published__exact = 1).count()
    return reviewcount

@register.filter
def clinicsaatlar(id):
    doctor = Doctor.objects.get(pk=1)
    clinic = Clinic.objects.get(pk=1)
    clinicsaat = ClinicSaatlar.objects.get(doctors=doctor)

    return clinicsaat.evde_muayine
