from django.shortcuts import render
from .models import Xidmatlar, Diaqnostikalar
# Create your views here.


def xidmetler(request):
    xidmetler = Xidmatlar.objects.all()
    diaqnostikalar = Diaqnostikalar.objects.all()
    context = {
        "xidmetler": xidmetler,
        "diaqnostikalar": diaqnostikalar
    }
    return render(request, 'xidmetler.html', context)
