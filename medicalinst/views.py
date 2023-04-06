from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request,'medicalinst/profile.html')

def dashboard(request):
    return render(request,'medicalinst/dashboard.html')

def works(request):
    return render(request,'medicalinst/works.html')