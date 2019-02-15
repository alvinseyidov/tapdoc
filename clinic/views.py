from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from clinic.models import Clinic
# Create your views here.

def clinicprofile(request, id):
    clinic = get_object_or_404(Clinic, id=id)
    return render(request, 'clinicprofile.html', {'clinic': clinic})
