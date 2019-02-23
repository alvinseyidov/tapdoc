from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from clinic.models import Clinic, Clinic_branch
# Create your views here.

def diaqnostika(request):
    diaqnostika_list = Clinic.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        diaqnostika_list = diaqnostika_list.filter(name__icontains=query)

    paginator = Paginator(diaqnostika_list, 3)
    page = request.GET.get('page')
    diaqnostika = paginator.get_page(page)

    context = {
        "diaqnostikas": diaqnostika
    }
    return render(request, 'diaqnostika.html', context)
