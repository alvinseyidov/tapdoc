from doctor.models import Doctor
from clinic.models import Clinic
from django import template
# Create your views here.

register = template.Library()

@register.filter
def clinicreviewscount(id):
    clinic = Clinic.objects.get(pk=id)
    clinicreviewcount = clinic.clinicreviews.filter(published__exact = 1).count()
    return clinicreviewcount
