from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from clinic.models import Clinic, Gallery, Sertifikat, XidmetlerPrices, DiaqnostikalarPrices
from service.models import XidmatlarGroup, DiaqnostikalarGroup, Xidmatlar, Diaqnostikalar

# Create your views here.

def clinicprofile(request, id):
    clinic = get_object_or_404(Clinic, id=id)
    xidmetlerprices = XidmetlerPrices.objects.filter(klinika=clinic)
    xidmetlergroup = XidmatlarGroup.objects.all()
    groupsums = []
    for xidmetlermovcud in xidmetlerprices:
        groupsums.append(xidmetlermovcud.xidmet.service_group)
    xidmetlerlist = list(set(groupsums))

    diaqnostikalarprices = DiaqnostikalarPrices.objects.filter(klinika=clinic)
    diaqnostikalargroup = DiaqnostikalarGroup.objects.all()
    groupsums2 = []
    for diaqnostikalarmovcud in diaqnostikalarprices:
        groupsums2.append(diaqnostikalarmovcud.diaqnostika.diaqnostika_group)
    diaqnostikalarlist = list(set(groupsums2))


    gallery = Gallery.objects.filter(clinic=clinic)
    sertifikatlar = Sertifikat.objects.filter(clinic=clinic)
    context = {
        "clinic": clinic,
        "sertifikatlar": sertifikatlar,
        "gallery": gallery,
        "xidmetlerprices": xidmetlerprices,
        "xidmetlergroup": xidmetlergroup,
        "xidmetlerlist": xidmetlerlist,
        "diaqnostikalarlist": diaqnostikalarlist,
        "diaqnostikalarprices": diaqnostikalarprices
        }
    return render(request, 'clinicprofile.html', context)



def clinicsqiymet(request):
    clinics_list = Clinic.objects.filter(type='MRK')
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        clinics_list = clinics_list.filter(name__icontains=query)

    paginator = Paginator(clinics_list,3)
    page = request.GET.get('page')
    clinics = paginator.get_page(page)
    xidmetler = Xidmatlar.objects.all()
    diaqnostikalar = Diaqnostikalar.objects.all()
    context = {
        "clinics": clinics,
        "xidmetler": xidmetler,
        "diaqnostikalar": diaqnostikalar
    }
    return render(request, 'clinicsqiymet.html', context)

def clinicsreyler(request):
    clinics_list = Clinic.objects.filter(type='MRK')
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        clinics_list = clinics_list.filter(name__icontains=query)

    paginator = Paginator(clinics_list,3)
    page = request.GET.get('page')
    clinics = paginator.get_page(page)
    xidmetler = Xidmatlar.objects.all()
    diaqnostikalar = Diaqnostikalar.objects.all()
    context = {
        "clinics": clinics,
        "xidmetler": xidmetler,
        "diaqnostikalar": diaqnostikalar
    }
    return render(request, 'clinicsreyler.html', context)

def clinicsreyting(request):
    clinics_list = Clinic.objects.filter(type='MRK')
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        clinics_list = clinics_list.filter(name__icontains=query)

    paginator = Paginator(clinics_list,3)
    page = request.GET.get('page')
    clinics = paginator.get_page(page)
    xidmetler = Xidmatlar.objects.all()
    diaqnostikalar = Diaqnostikalar.objects.all()
    context = {
        "clinics": clinics,
        "xidmetler": xidmetler,
        "diaqnostikalar": diaqnostikalar
    }
    return render(request, 'clinicsreyting.html', context)

def clinics(request):
    clinics_list = Clinic.objects.filter(type='MRK')
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        clinics_list = clinics_list.filter(name__icontains=query)

    paginator = Paginator(clinics_list,3)
    page = request.GET.get('page')
    clinics = paginator.get_page(page)
    xidmetler = Xidmatlar.objects.all()
    diaqnostikalar = Diaqnostikalar.objects.all()
    context = {
        "clinics": clinics,
        "xidmetler": xidmetler,
        "diaqnostikalar": diaqnostikalar
    }
    return render(request, 'clinics.html', context)

def clinicsspecific(request, id):
    xidmet = Xidmatlar.objects.get(pk=id)
    clinics_list = xidmet.relate_name_xidmetler.all()
    paginator = Paginator(clinics_list,3)
    page = request.GET.get('page')
    clinics = paginator.get_page(page)
    xidmetler = Xidmatlar.objects.all()
    context = {
        "clinics": clinics,
        "xidmetler": xidmetler,
        "xidmet": xidmet

    }
    return render(request, 'clinicsspecific.html', context)
