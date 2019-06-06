from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from clinic.models import Clinic, Gallery, Sertifikat, XidmetlerPrices, DiaqnostikalarPrices
from service.models import XidmatlarGroup, DiaqnostikalarGroup, Xidmatlar, Diaqnostikalar
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/admin/')
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


    reviewaverage = 0
    reviewcount = clinic.clinicreviews.filter(published__exact = 1).count()
    reviews = clinic.clinicreviews.filter(published__exact = 1)

    context = {
        "clinic": clinic,
        "sertifikatlar": sertifikatlar,
        "gallery": gallery,
        "xidmetlerprices": xidmetlerprices,
        "xidmetlergroup": xidmetlergroup,
        "xidmetlerlist": xidmetlerlist,
        "diaqnostikalarlist": diaqnostikalarlist,
        "diaqnostikalarprices": diaqnostikalarprices,
        'reviewcount': reviewcount,
        'reviews': reviews
        }
    return render(request, 'clinicprofile.html', context)


@login_required(login_url='/admin/')
def clinicsqiymet(request):
    clinics_list = Clinic.objects.filter(type='MRK')
    clinicsall = Clinic.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        clinics_list = clinics_list.filter(name__icontains=query)

    paginator = Paginator(clinics_list,10)
    page = request.GET.get('page')
    clinics = paginator.get_page(page)
    xidmetler = XidmatlarGroup.objects.order_by('group_name')
    diaqnostikalar = Diaqnostikalar.objects.all()
    context = {
        "clinics": clinics,
        "clinicsall": clinicsall,
        "xidmetler": xidmetler,
        "diaqnostikalar": diaqnostikalar
    }
    return render(request, 'clinicsqiymet.html', context)

@login_required(login_url='/admin/')
def clinicsreyler(request):
    clinics_list = Clinic.objects.filter(type='MRK')
    clinicsall = Clinic.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        clinics_list = clinics_list.filter(name__icontains=query)

    paginator = Paginator(clinics_list,3)
    page = request.GET.get('page')
    clinics = paginator.get_page(page)
    xidmetler = XidmatlarGroup.objects.order_by('group_name')
    diaqnostikalar = Diaqnostikalar.objects.all()
    context = {
        "clinics": clinics,
        "clinicsall": clinicsall,
        "xidmetler": xidmetler,
        "diaqnostikalar": diaqnostikalar
    }
    return render(request, 'clinicsreyler.html', context)

@login_required(login_url='/admin/')
def clinicsreyting(request):
    clinics_list = Clinic.objects.filter(type='MRK')
    clinicsall = Clinic.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        clinics_list = clinics_list.filter(name__icontains=query)

    paginator = Paginator(clinics_list,3)
    page = request.GET.get('page')
    clinics = paginator.get_page(page)
    xidmetler = XidmatlarGroup.objects.order_by('group_name')
    diaqnostikalar = Diaqnostikalar.objects.all()
    context = {
        "clinics": clinics,
        "clinicsall": clinicsall,
        "xidmetler": xidmetler,
        "diaqnostikalar": diaqnostikalar
    }
    return render(request, 'clinicsreyting.html', context)

@login_required(login_url='/admin/')
def clinics(request):
    clinics_list = Clinic.objects.filter(type='MRK')
    clinicsall = Clinic.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        clinics_list = clinics_list.filter(name__icontains=query)

    paginator = Paginator(clinicsall,10)
    page = request.GET.get('page')
    clinics = paginator.get_page(page)
    xidmetler = XidmatlarGroup.objects.order_by('group_name')
    diaqnostikalar = Diaqnostikalar.objects.all()
    context = {
        "clinics": clinics,
        "clinicsall": clinicsall,
        "xidmetler": xidmetler,
        "diaqnostikalar": diaqnostikalar
    }
    return render(request, 'clinics.html', context)

@login_required(login_url='/admin/')
def clinicsspecific(request, id):
    xidmet = Xidmatlar.objects.get(pk=id)
    clinics_list = xidmet.relate_name_xidmetler.all()
    clinicsall = Clinic.objects.all()
    paginator = Paginator(clinics_list,3)
    page = request.GET.get('page')
    clinics = paginator.get_page(page)
    xidmetler = XidmatlarGroup.objects.order_by('group_name')
    context = {
        "clinics": clinics,
        "clinicsall": clinicsall,
        "xidmetler": xidmetler,
        "xidmet": xidmet

    }
    return render(request, 'clinicsspecific.html', context)



@login_required(login_url='/admin/')
def clinicaddtofavor(request):

    if request.method == 'GET':
        post_id = request.GET['post_id']
        clinic = get_object_or_404(Clinic, id=post_id)
        clinic.wishlist.add(request.user)
        return HttpResponse("Success!") # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")

@login_required(login_url='/admin/')
def clinicremovefavor(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        clinic = get_object_or_404(Clinic, id=post_id)
        clinic.wishlist.remove(request.user)
        return HttpResponse("Success!") # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")
