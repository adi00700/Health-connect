from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('loginpage/patient',views.patientloginpage),
    path('signuppage/patientdetails',views.patientdetailspage),
    path('signuppage/patient',views.patientsignuppage),
    path('login/patient',views.patientlogin),
    path('signup/patient',views.patientsignup),
    path('signup/patientdetails',views.patientdetailssignup),
    path('signuppage/institute',views.instsignuppage),
    path('loginpage/institute',views.instloginpage),
    path('signup/institute',views.instsignup),
    path('login/institute',views.instlogin),
    path('logout/user',views.logoutuser)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
