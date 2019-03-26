from django.shortcuts import render
from .models import Xidmatlar, Diaqnostikalar
from service.models import XidmatlarGroup, DiaqnostikalarGroup
# Create your views here.


def xidmetler(request):
    xidmetgrouplar = XidmatlarGroup.objects.all()
    diaqnostikagrouplar = DiaqnostikalarGroup.objects.all()
    context = {
        "xidmetgrouplar": xidmetgrouplar,
        "diaqnostikagrouplar": diaqnostikagrouplar 
    }
    return render(request, 'xidmetler.html', context)



def xidmetlerspecific(request, id):
    xidmetdiaqnostikagroup = XidmatlarGroup.objects.get(pk=id)
    xidmetgrouplar = XidmatlarGroup.objects.all()
    diaqnostikagrouplar = DiaqnostikalarGroup.objects.all()

    context = {
        "xidmetdiaqnostikagroup": xidmetdiaqnostikagroup,
        "xidmetgrouplar": xidmetgrouplar,
        "diaqnostikagrouplar": diaqnostikagrouplar
    }
    return render(request, 'xidmetlerspecific.html', context)


def xidmetlerdiaqspecific(request, id):
    xidmetdiaqnostikagroup = DiaqnostikalarGroup.objects.get(pk=id)
    xidmetgrouplar = XidmatlarGroup.objects.all()
    diaqnostikagrouplar = DiaqnostikalarGroup.objects.all()

    context = {
        "xidmetdiaqnostikagroup": xidmetdiaqnostikagroup,
        "xidmetgrouplar": xidmetgrouplar,
        "diaqnostikagrouplar": diaqnostikagrouplar
    }
    return render(request, 'xidmetlerdiaqspecific.html', context)
