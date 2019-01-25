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

@login_required(login_url='/admin/')
def doctor(request):
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
    return render(request, 'doctor.html', context)

@login_required(login_url='/admin/')
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

@login_required(login_url='/admin/')
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


@login_required(login_url='/admin/')
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


@login_required(login_url='/admin/')
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



@login_required(login_url='/admin/')
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

@login_required(login_url='/admin/')
def clinic(request):
    return render(request, 'clinic.html')

@login_required(login_url='/admin/')
def clinicpage2(request):
    return render(request, 'clinicpage2.html')

@login_required(login_url='/admin/')
def clinicpage3(request):
    return render(request, 'clinicpage3.html')

@login_required(login_url='/admin/')
def clinicpage4(request):
    return render(request, 'clinicpage4.html')

@login_required(login_url='/admin/')
def clinicpage5(request):
    return render(request, 'clinicpage5.html')

@login_required(login_url='/admin/')
def diaqnostika(request):
    return render(request, 'diaqnostika.html')

@login_required(login_url='/admin/')
def diaqnostikapage2(request):
    return render(request, 'diaqnostikapage2.html')

@login_required(login_url='/admin/')
def diaqnostikapage3(request):
    return render(request, 'diaqnostikapage3.html')

@login_required(login_url='/admin/')
def diaqnostikapage4(request):
    return render(request, 'diaqnostikapage4.html')

@login_required(login_url='/admin/')
def diaqnostikapage5(request):
    return render(request, 'diaqnostikapage5.html')


@login_required(login_url='/admin/')
def xidmetler(request):
    return render(request, 'xidmetler.html')


@login_required(login_url='/admin/')
def doctordetail(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    wishlist = doctor.wishlist.all()
    reviewaverage = 0
    reviewcount = 0
    if doctor.reviews.count()>0:
        reviewaverage= round(doctor.reviews.aggregate(Avg('star'))['star__avg'])
        reviewcount = doctor.reviews.count()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            reviewclinicid = request.POST.get('clinic')
            reviewclinic = Clinic.objects.get(id=reviewclinicid)
            if form.is_valid():
                post = form.save(commit=False)
                post.doctor = doctor
                post.starter = request.user
                post.clinic = reviewclinic
                post.save()
                return redirect('doctordetail', id=id)
        else:
            return redirect('login')
    else:
        form = ReviewForm()
    return render(request, 'doctordetail.html', {'wishlist': wishlist,'doctor': doctor, 'form': form, 'reviewcount': reviewcount, 'reviewaverage':reviewaverage})


@login_required(login_url='/admin/')
def clinicdetail(request):
    doctorid = 1
    return render(request, 'clinicdetail.html')

@login_required(login_url='/admin/')
def clinicdetailistanbul(request):
    doctorid = 1
    return render(request, 'clinicdetailistanbul.html')

@login_required(login_url='/admin/')
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
