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
from django.urls import path, include
from doctor import views
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views
from clinic import views as clinic_views
from service import views as service_views
from diaqnostika import views as diaqnostika_views
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('i18n/', include('django.conf.urls.i18n')),
] 
urlpatterns += i18n_patterns(
    path('', views.homepage, name='homepage'),
    path('doctor/', views.doctor, name='doctor'),
    path('doctor/staj', views.doctorstaj, name='doctorstaj'),
    path('doctor/qiymet', views.doctorqiymet, name='doctorqiymet'),
    path('doctor/reyler', views.doctorreyler, name='doctorreyler'),
    path('doctor/reyting', views.doctorreyting, name='doctorreyting'),
    path('doctor/category/<int:id>', views.doctorspecific, name='doctorspecific'),
    path('muracietform/', views.muracietform, name='muracietform'),
    path('muracietform2/', views.muracietform2, name='muracietform2'),
    path('logindoc/', views.logindoc, name='logindoc'),
    path('loginclinic/', views.loginclinic, name='loginclinic'),
    path('clinic/', clinic_views.clinics, name='clinic'),
    path('clinic/reyler', clinic_views.clinicsreyler, name='clinicreyler'),
    path('clinic/qiymet', clinic_views.clinicsqiymet, name='clinicqiymet'),
    path('clinic/reyting', clinic_views.clinicsreyting, name='clinicreyting'),
    path('clinic/category/<int:id>', clinic_views.clinicsspecific, name='clinicsspecific'),
    path('clinic/<int:id>/profile', clinic_views.clinicprofile, name='clinicprofile'),
    path('diaqnostika/', diaqnostika_views.diaqnostika, name='diaqnostika'),
    path('diaqnostika/category/<int:id>', diaqnostika_views.diaqnostikaspecific, name='diaqnostikaspecific'),
    path('diaqnostika/reyler', diaqnostika_views.diaqnostikareyler, name='diaqnostikareyler'),
    path('diaqnostika/reyting', diaqnostika_views.diaqnostikareyting, name='diaqnostikareyting'),
    path('diaqnostika/qiymet', diaqnostika_views.diaqnostikaqiymet, name='diaqnostikaqiymet'),
    path('xidmetler/', service_views.xidmetler, name='xidmetler'),
    path('xidmetler/category/<int:id>', service_views.xidmetlerspecific, name='xidmetlerspecific'),
    path('xidmetler/dcategory/<int:id>', service_views.xidmetlerdiaqspecific, name='xidmetlerdiaqspecific'),
    path('doctor/<int:id>/detail', views.doctordetail, name='doctordetail'),
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('account/',accounts_views.account , name='account'),
    path('account/doctors',accounts_views.accountdoctors , name='accountdoctors'),
    path('account/settings',accounts_views.accountsettings , name='accountsettings'),
    path('account/settings/security',accounts_views.accountsettingssecurity , name='accountsettingssecurity'),
    path('account/settings/notifications',accounts_views.accountsettingsnotifications , name='accountsettingsnotifications'),
    path('account/settings/docpermissions',accounts_views.accountsettingsdocpermissions , name='accountsettingsdocpermissions'),
    path('account/settings/clinicpermissions',accounts_views.accountsettingsclinicpermissions , name='accountsettingsclinicpermissions'),
    path('account/settings/family',accounts_views.accountsettingsfamily , name='accountsettingsfamily'),
    path('account/settings/history',accounts_views.accountsettingshistory , name='accountsettingshistory'),
    path('account/settings/promotions',accounts_views.accountsettingspromotions , name='accountsettingspromotions'),
    path('account/clinics',accounts_views.accountclinics , name='accountcinics'),
    path('account/aptek',accounts_views.accountaptek , name='accountaptek'),
    path('account/doctordetail',accounts_views.accountdoctordetail , name='accountdoctordetail'),
    path('account/clinicdetail',accounts_views.accountclinicdetail , name='accountclinicdetail'),
    path('account/aptekdetail',accounts_views.accountaptekdetail , name='accountaptekdetail'),
    path('doctor/<int:id>/addtofavor', views.addtofavor, name='addtofavor'),
    path('doctor/<int:id>/removefavor', views.removefavor, name='removefavor'),
    path('doctor/doctoraddtofavor', views.doctoraddtofavor, name='doctoraddtofavor'),
    path('doctor/doctorremovefavor', views.doctorremovefavor, name='doctorremovefavor'),
    path('clinics/clinicaddtofavor', clinic_views.clinicaddtofavor, name='clinicaddtofavor'),
    path('clinics/clinicremovefavor', clinic_views.clinicremovefavor, name='clinicremovefavor'),
    prefix_default_language=False,
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
