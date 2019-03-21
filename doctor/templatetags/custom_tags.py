from doctor.models import Doctor
from clinic.models import Clinic
from django import template
# Create your views here.

register = template.Library()

@register.filter
def reviewscount(id):
    doctor = Doctor.objects.get(pk=id)
    reviewcount = doctor.reviews.filter(published__exact = 1).count()
    return reviewcount
