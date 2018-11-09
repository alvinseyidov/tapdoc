"""tapdoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from doctor import views
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.homepage, name='homepage'),
    path('doctor/', views.doctor, name='doctor'),
    path('doctors/', views.doctors, name='doctors'),
    path('logindoc/', views.logindoc, name='logindoc'),
    path('loginclinic/', views.loginclinic, name='loginclinic'),
    path('clinic/', views.clinic, name='clinic'),
    path('clinic/<int:id>/detail', views.clinicdetail, name='clinicdetail'),
    path('diaqnostika/', views.diaqnostika, name='diaqnostika'),
    path('xidmetler/', views.xidmetler, name='xidmetler'),
    path('doctor/<int:id>/detail', views.doctordetail, name='doctordetail'),
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('account/',accounts_views.account , name='account'),
    path('account/doctors',accounts_views.accountdoctors , name='accountdoctors'),
    path('account/settings',accounts_views.accountsettings , name='accountsettings'),
    path('account/clinics',accounts_views.accountclinics , name='accountcinics'),
    path('account/doctordetail',accounts_views.accountdoctordetail , name='accountdoctordetail'),
    path('account/clinicdetail',accounts_views.accountclinicdetail , name='accountclinicdetail'),
    path('doctor/<int:id>/addtofavor', views.addtofavor, name='addtofavor'),
    path('doctor/<int:id>/removefavor', views.removefavor, name='removefavor'),
    path('doctor/<int:id>/doctoraddtofavor', views.doctoraddtofavor, name='doctoraddtofavor'),
    path('doctor/<int:id>/doctorremovefavor', views.doctorremovefavor, name='doctorremovefavor'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
