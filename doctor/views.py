from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from doctor.models import Doctor, Clinic
from .forms import ReviewForm
from django.db.models import Avg
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request, 'index.html')
def muracietform(request):
    return render(request, 'muracietiframe.html')
def muracietform2(request):
    return render(request, 'muracietiframe2.html')

def logindoc(request):
    return render(request, 'logindoc.html')
def loginclinic(request):
    return render(request, 'loginclinic.html')


def doctor(request):
    doctors_list = Doctor.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        doctors_list = doctors_list.filter(first_name__icontains=query)

    paginator = Paginator(doctors_list, 3)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    context = {
        "doctors": doctors
    }
    return render(request, 'doctor.html', context)


def aa(request):
    doctors_list = Doctor.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        doctors_list = doctors_list.filter(first_name__icontains=query)

    paginator = Paginator(doctors_list, 2)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    context = {
        "doctors": doctors
    }
    return render(request, 'aa.html', context)


def doctorpage2(request):
    doctors_list = Doctor.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        doctors_list = doctors_list.filter(first_name__icontains=query)



    paginator = Paginator(doctors_list, 4)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    context = {
        "doctors": doctors
    }
    return render(request, 'doctorpage2.html', context)


def doctorpage3(request):
    doctors_list = Doctor.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        doctors_list = doctors_list.filter(first_name__icontains=query)



    paginator = Paginator(doctors_list, 4)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    context = {
        "doctors": doctors
    }
    return render(request, 'doctorpage3.html', context)



def doctorpage4(request):
    doctors_list = Doctor.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        doctors_list = doctors_list.filter(first_name__icontains=query)



    paginator = Paginator(doctors_list, 4)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    context = {
        "doctors": doctors
    }
    return render(request, 'doctorpage4.html', context)



def doctorpage5(request):
    doctors_list = Doctor.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        doctors_list = doctors_list.filter(first_name__icontains=query)



    paginator = Paginator(doctors_list, 4)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    context = {
        "doctors": doctors
    }
    return render(request, 'doctorpage5.html', context)




def doctors(request):
    doctors_list = Doctor.objects.all()
    query = request.GET.get('q')
    querygeo = request.GET.get('geo')
    if query:
        doctors_list = doctors_list.filter(first_name__icontains=query)



    paginator = Paginator(doctors_list, 4)
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    context = {
        "doctors": doctors
    }
    return render(request, 'doctors.html', context)

def clinic(request):
    clinics_list = Clinic.objects.all()
    query_clinic = request.GET.get('q')
    querygeo_clinic = request.GET.get('geo')
    if query_clinic:
        clinics_list = clinics_list.filter(name__icontains=query)

    paginator_clinic = Paginator(clinics_list, 4)
    page_clinic = request.GET.get('page')
    clinics = paginator_clinic.get_page(page_clinic)

    context = {
        "clinics": clinics
    }
    return render(request, 'clinic.html', context)


def clinicpage2(request):
    return render(request, 'clinicpage2.html')


def clinicpage3(request):
    return render(request, 'clinicpage3.html')

def clinicpage4(request):
    return render(request, 'clinicpage4.html')


def clinicpage5(request):
    return render(request, 'clinicpage5.html')


def diaqnostika(request):
    return render(request, 'diaqnostika.html')


def diaqnostikapage2(request):
    return render(request, 'diaqnostikapage2.html')


def diaqnostikapage3(request):
    return render(request, 'diaqnostikapage3.html')


def diaqnostikapage4(request):
    return render(request, 'diaqnostikapage4.html')


def diaqnostikapage5(request):
    return render(request, 'diaqnostikapage5.html')



def xidmetler(request):
    return render(request, 'xidmetler.html')



def doctordetail(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    wishlist = doctor.wishlist.all()
    reviewaverage = 0
    reviewcount = 0
    if doctor.reviews.count()>0:
        reviewcount = doctor.reviews.count()
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
    return render(request, 'doctordetail.html', {'wishlist': wishlist,'doctor': doctor, 'form': form,'reviewcount': reviewcount})



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

def doctoraddtofavor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.wishlist.add(request.user)

    return redirect('doctor')

def doctorremovefavor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.wishlist.remove(request.user)

    return redirect('doctor')
