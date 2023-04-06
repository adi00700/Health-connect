from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userauth.models import PatientDetails
from .models import Report,Appointment

# Create your views here.

@login_required(login_url='/auth/loginpage/patient')
def profile(request):
    patient = PatientDetails.objects.get(user = request.user)
    return render(request,'health/profile.html',{'patient':patient})

@login_required(login_url='/auth/loginpage/patient')
def dashboard(request):
    patient = PatientDetails.objects.get(user = request.user)
    appointments = Appointment.objects.filter(patient = request.user)
    return render(request,'health/dashboard.html',{'patient':patient,'appointments':appointments})

@login_required(login_url='/auth/loginpage/patient')
def works(request):
    reports = Report.objects.all()
    return render(request,'health/works.html',{'reports':reports})