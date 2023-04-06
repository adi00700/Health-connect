from django.shortcuts import render
from django.http import HttpResponse
from main import MedRecommender
# Create your views here.

def profile(request):
    return render(request,'medicalinst/profile.html')

def dashboard(request):
    return render(request,'medicalinst/dashboard.html')

def works(request):
    return render(request,'medicalinst/works.html')

def test(request):
    condition = str(request.POST['condition'])
    return HttpResponse(MedRecommender(condition))