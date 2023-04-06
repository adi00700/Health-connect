from django.shortcuts import render
from userauth.models import InsuranceDetails
from django.contrib.auth.decorators import login_required
from .models import Branches,SubRequest,Subscriber

# Create your views here.

@login_required(login_url='/auth/loginpage/institute')
def profile(request):
    insurance = InsuranceDetails.objects.get(user = request.user)
    return render(request,'insurance/profile.html',{'insurance':insurance})

@login_required(login_url='/auth/loginpage/institute')
def dashboard(request):
    subscribed = Subscriber.objects.filter(insurer = request.user)
    pendings = SubRequest.objects.filter(insurer = request.user)
    ns = len(subscribed)
    np = len(pendings)
    total = 0
    for s in subscribed:
        total += s.prem_cost
    nc=0
    for s in subscribed:
        if s.pay_pending==True:
            continue
        nc += s.prem_cost
    collec = (nc/ns)*100
    return render(request,'insurance/dashboard.html',{'ns':ns,'np':np,'total':total,'collec':collec})

@login_required(login_url='/auth/loginpage/institute')
def works(request):
    pendings = SubRequest.objects.filter(insurer = request.user, pat_reject=False, pat_accept=False)
    subscribers = Subscriber.objects.filter(insurer = request.user)
    return render(request,'insurance/works.html',{'pendings':pendings,'subscribers':subscribers})