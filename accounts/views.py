from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from doctor.models import Doctor, User
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='/admin/')
def account(request):
    doctors_list = Doctor.objects.all()
    wishlist1 = User.objects.first()
    wishlist = wishlist1.wishlist.all()
    context = {
        "doctors": wishlist
    }
    return render(request, 'account.html', context)

@login_required(login_url='/admin/')
def accountdoctors(request):
    return render(request, 'accountdoctors.html')

@login_required(login_url='/admin/')
def accountsettings(request):
    return render(request, 'settings.html')

@login_required(login_url='/admin/')
def accountsettingssecurity(request):
    return render(request, 'settingssecurity.html')

@login_required(login_url='/admin/')
def accountsettingsnotifications(request):
    return render(request, 'settingsnotifications.html')

@login_required(login_url='/admin/')
def accountsettingsdocpermissions(request):
    return render(request, 'settingsdocpermissions.html')

@login_required(login_url='/admin/')
def accountsettingsclinicpermissions(request):
    return render(request, 'settingsclinicpermissions.html')

@login_required(login_url='/admin/')
def accountsettingsfamily(request):
    return render(request, 'settingsfamily.html')

@login_required(login_url='/admin/')
def accountsettingshistory(request):
    return render(request, 'settingshistory.html')

@login_required(login_url='/admin/')
def accountsettingspromotions(request):
    return render(request, 'settingspromotions.html')


@login_required(login_url='/admin/')
def accountclinics(request):
    return render(request, 'accountclinics.html')

@login_required(login_url='/admin/')
def accountaptek(request):
    return render(request, 'accountaptek.html')

@login_required(login_url='/admin/')
def accountdoctordetail(request):
    return render(request, 'accountdoctordetail.html')

@login_required(login_url='/admin/')
def accountclinicdetail(request):
    return render(request, 'accountclinicdetail.html')

@login_required(login_url='/admin/')
def accountaptekdetail(request):
    return render(request, 'accountaptekdetail.html')
