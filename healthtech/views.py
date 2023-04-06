from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request,'homepage.html')

@login_required(login_url="/auth/loginpage/patient")
def checkuser(request):
    if request.user.last_name == "Patient":
        return redirect('/patient/profile')
    elif request.user.last_name == "medical":
        return redirect('/medicalinst/profile')
    else:
        return redirect('/insurance/profile')