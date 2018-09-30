from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from doctor.models import Doctor, User
from .forms import SignUpForm

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

def account(request):
    doctors_list = Doctor.objects.all()
    wishlist1 = User.objects.first()
    wishlist = wishlist1.wishlist.all()
    context = {
        "doctors": wishlist
    }
    return render(request, 'account.html', context)
