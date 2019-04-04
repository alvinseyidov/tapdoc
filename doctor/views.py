from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from doctor.models import Doctor, Sertifikat, Profession
from .forms import ReviewForm
from django.db.models import Avg
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import to_locale, get_language

# Create your views here.


def homepage(request):
    professions = Profession.objects.all()
    lang = get_language()
    context = {
        "professions": professions,
        "lang": lang
    }
    return render(request, 'index.html',context)
def muracietform(request):
    return render(request, 'muracietiframe.html')
def muracietform2(request):
    return render(request, 'muracietiframe2.html')

def logindoc(request):
    return render(request, 'logindoc.html')
def loginclinic(request):
    return render(request, 'loginclinic.html')


def doctor(request):
    lang = get_language()
    doctors_list = Doctor.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        doctors_list = doctors_list.filter(first_name__icontains=query)

    paginator = Paginator(doctors_list, 10)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)
    professions = Profession.objects.order_by('name')
    context = {
        "doctors": doctors_list,
        "professions": professions,
        "lang": lang
    }
    return render(request, 'doctor.html', context)

def doctorstaj(request):
    doctors_list = Doctor.objects.order_by('-tecrube')
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        doctors_list = doctors_list.filter(first_name__icontains=query)

    paginator = Paginator(doctors_list, 10)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    professions = Profession.objects.order_by('name')
    context = {
        "doctors": doctors,
        "professions": professions
    }
    return render(request, 'doctorstaj.html', context)

def doctorreyler(request):
    doctors_list = Doctor.objects.all().annotate(num_reviews=Count('reviews')).order_by('-num_reviews')
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        doctors_list = doctors_list.filter(first_name__icontains=query)

    paginator = Paginator(doctors_list, 10)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    professions = Profession.objects.order_by('name')
    context = {
        "doctors": doctors,
        "professions": professions
    }
    return render(request, 'doctorreyler.html', context)

def doctorqiymet(request):
    doctors_list = Doctor.objects.order_by('-qebula_yazilma')
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        doctors_list = doctors_list.filter(first_name__icontains=query)

    paginator = Paginator(doctors_list, 10)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    professions = Profession.objects.order_by('name')
    context = {
        "doctors": doctors,
        "professions": professions
    }
    return render(request, 'doctorqiymet.html', context)

def doctorreyting(request):
    doctors_list = Doctor.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        doctors_list = doctors_list.filter(first_name__icontains=query)

    paginator = Paginator(doctors_list, 10)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    professions = Profession.objects.order_by('name')
    context = {
        "doctors": doctors,
        "professions": professions
    }
    return render(request, 'doctorreyting.html', context)

def doctorspecific(request, id):
    profession = Profession.objects.get(pk=id)
    doctors_list = profession.doctors.all()
    paginator = Paginator(doctors_list, 10)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    professions = Profession.objects.order_by('name')
    context = {
        "doctors": doctors,
        "profession": profession,
        "professions": professions
    }
    return render(request, 'doctorspecific.html', context)





def doctordetail(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    wishlist = doctor.wishlist.all()
    reviewaverage = 0
    reviewcount = doctor.reviews.filter(published__exact = 1).count()
    reviews = doctor.reviews.filter(published__exact = 1)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.doctor = doctor
                post.starter = request.user
                post.published = '0'
                post.save()
                return redirect('doctordetail', id=id)
        else:
            return redirect('login')
    else:
        form = ReviewForm()

    sertifikatlar = Sertifikat.objects.filter(doctor=doctor)
    endirimli_qiymet = int(doctor.qebula_yazilma) - (int(doctor.qebula_yazilma) * int(doctor.qebula_yazilma_endirim_faiz)/100)
    endirimli_qiymet = int(endirimli_qiymet)
    context = {
        'wishlist': wishlist,
        'doctor': doctor,
        'sertifikatlar': sertifikatlar,
        'form': form,
        'endirimli_qiymet': endirimli_qiymet,
        'reviewcount': reviewcount,
        'reviews': reviews
    }
    return render(request, 'doctordetail.html',context)



def clinicdetail(request):
    doctorid = 1
    return render(request, 'clinicdetail.html')


def clinicdetailnerimanov(request):
    doctorid = 1
    return render(request, 'clinicdetailnerimanov.html')


def clinicdetailnesimi(request):
    doctorid = 1
    return render(request, 'clinicdetailnesimi.html')


def clinicdetailyasamal(request):
    doctorid = 1
    return render(request, 'clinicdetailyasamal.html')


def clinicdetailistanbul(request):
    doctorid = 1
    return render(request, 'clinicdetailistanbul.html')


def clinicdetailvital(request):
    doctorid = 1
    return render(request, 'clinicdetailvital.html')





def addtofavor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.wishlist.add(request.user)

    return redirect('doctordetail', id=id)

def removefavor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.wishlist.remove(request.user)

    return redirect('doctordetail', id=id)




def doctoraddtofavor(request):

    if request.method == 'GET':
        post_id = request.GET['post_id']
        doctor = get_object_or_404(Doctor, id=post_id)
        doctor.wishlist.add(request.user)
        return HttpResponse("Success!") # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")


def doctorremovefavor(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        doctor = get_object_or_404(Doctor, id=post_id)
        doctor.wishlist.remove(request.user)
        return HttpResponse("Success!") # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")
