from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from clinic.models import Clinic
from service.models import Diaqnostikalar
# Create your views here.

def diaqnostika(request):
    diaqnostika_list = Clinic.objects.filter(type='MRK')
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        diaqnostika_list = diaqnostika_list.filter(name__icontains=query)

    paginator = Paginator(diaqnostika_list,4)
    page = request.GET.get('page')
    diaqnostika = paginator.get_page(page)

    context = {
        "diaqnostikas": diaqnostika
    }
    return render(request, 'diaqnostika.html', context)

def diaqnostikaspecific(request, id):
    xidmet_diaqnostik = Diaqnostikalar.objects.get(pk=id)
    diaqnostika_list = xidmet_diaqnostik.relate_name_diaqnostikalar.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        diaqnostika_list = diaqnostika_list.filter(name__icontains=query)

    paginator = Paginator(diaqnostika_list, 10)
    page = request.GET.get('page')
    diaqnostika = paginator.get_page(page)

    context = {
        "diaqnostikas": diaqnostika,
        "xidmetdiaqnostik": xidmet_diaqnostik
    }
    return render(request, 'diaqnostikaspecific.html', context)

def diaqnostikareyler(request):
    diaqnostika_list = Clinic.objects.filter(type='MRK')
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        diaqnostika_list = diaqnostika_list.filter(name__icontains=query)

    paginator = Paginator(diaqnostika_list, 2)
    page = request.GET.get('page')
    diaqnostika = paginator.get_page(page)

    context = {
        "diaqnostikas": diaqnostika
    }
    return render(request, 'diaqnostikareyler.html', context)

def diaqnostikaqiymet(request):
    diaqnostika_list = Clinic.objects.filter(type='MRK')
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        diaqnostika_list = diaqnostika_list.filter(name__icontains=query)

    paginator = Paginator(diaqnostika_list, 2)
    page = request.GET.get('page')
    diaqnostika = paginator.get_page(page)

    context = {
        "diaqnostikas": diaqnostika
    }
    return render(request, 'diaqnostikaqiymet.html', context)

def diaqnostikareyting(request):
    diaqnostika_list = Clinic.objects.filter(type='MRK')
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        diaqnostika_list = diaqnostika_list.filter(name__icontains=query)

    paginator = Paginator(diaqnostika_list, 2)
    page = request.GET.get('page')
    diaqnostika = paginator.get_page(page)

    context = {
        "diaqnostikas": diaqnostika
    }
    return render(request, 'diaqnostikareyting.html', context)
