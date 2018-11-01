from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from doctor.models import Doctor, User
from .forms import SignUpForm

@login_required
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
@login_required
def account(request):
    doctors_list = Doctor.objects.all()
    wishlist1 = User.objects.first()
    wishlist = wishlist1.wishlist.all()
    context = {
        "doctors": wishlist
    }
    return render(request, 'account.html', context)
@login_required
def accountdoctors(request):
    return render(request, 'accountdoctors.html')
@login_required
def accountsettings(request):
    return render(request, 'settings.html')
@login_required
def accountclinics(request):
    return render(request, 'accountclinics.html')
@login_required
def accountdoctordetail(request):
    return render(request, 'accountdoctordetail.html')
@login_required
def accountclinicdetail(request):
    return render(request, 'accountclinicdetail.html')
