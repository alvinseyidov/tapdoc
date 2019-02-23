from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from clinic.models import Clinic, Clinic_branch
# Create your views here.

def clinicprofile(request, id):
    clinic = get_object_or_404(Clinic, id=id)
    return render(request, 'clinicprofile.html', {'clinic': clinic})

def clinicbranchprofile(request, id):
    clinicbranch = get_object_or_404(Clinic_branch, id=id)
    return render(request, 'clinicbranchprofile.html', {'clinicbranch': clinicbranch})


def clinics(request):
    clinics_list = Clinic.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        clinics_list = clinics_list.filter(name__icontains=query)

    paginator = Paginator(clinics_list, 3)
    page = request.GET.get('page')
    clinics = paginator.get_page(page)

    context = {
        "clinics": clinics
    }
    return render(request, 'clinics.html', context)
