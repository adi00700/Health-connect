from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import PatientDetails,MedicalDetails,InsuranceDetails
from django.contrib.auth.decorators import login_required
from random import randint

# Create your views here.
def patientloginpage(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in")
    return render(request,'auth/login_patient.html')

@login_required(login_url='auth/signuppage/patient')
def patientdetailspage(request,healthid):
    # Health Id sharing can be later shifted to email or sms type
    return render(request,'auth/patient_details.html',{'pageno':healthid})

def patientsignuppage(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in")
    return render(request,'auth/signup_patient.html')

def patientlogin(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in")
    if request.method=='POST':
        login_username=request.POST['username']
        login_password=request.POST['password']

        user=authenticate(username=login_username,password=login_password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect("/")
        else:
            messages.error(request,'Login Failed')
            return HttpResponse("Oops! Login Failed")
    else:
        return HttpResponse("Unsecured Login Error !!")

def patientsignup(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in")
    if request.method=='POST':
        # Obtaining Data From The HTML Form
        # Username multiple digit random generation
        # randint(1000000000,9999999999)
        healthid=randint(1000000000,9999999999)
        while len(User.objects.filter(username=healthid)) > 0:
            healthid=randint(1000000000,9999999999)
        username=healthid
        password=request.POST['password']
        cfpassword=request.POST['cfpassword']
        email=request.POST['email']
        name=request.POST['name']

        if password != cfpassword:
            messages.error(request,"Passwords do not match")
            return redirect("/user/signuppage")

        # Default User Auth Save
        newuser = User.objects.create_user(username,email,password)
        newuser.first_name=name
        newuser.last_name="Patient"
        newuser.save()
        user=authenticate(username=username,password=password)
        login(request,user)

        messages.success(request,"User Account Created Successfully. Update Profile Details Now")
        return patientdetailspage(request,healthid)
    else:
        return HttpResponse("Creating new user account failed !")

@login_required(login_url='auth/signuppage/patient')
def patientdetailssignup(request):
    if request.method=='POST':
        phone = request.POST['phone']
        age = request.POST['age']
        gender = request.POST['gender']
        blood = request.POST['blood']
        perm_address = request.POST['perm_address']
        emg_contact = request.POST['emg_contact']
        image = request.POST['profileimg']
        userd=PatientDetails(user=request.user,name=request.user.first_name,phone=phone,age=age,gender=gender,blood=blood,perm_address=perm_address,emg_contact=emg_contact,profile=image)
        userd.save()
        messages.success(request,'Profile Updated')
    else:
        messages.error(request,'Invalid Request')
    return redirect("/")

# Medical Institution SignUp
# InstType(pvt,govt,semipvt,indi), Name, Address, Telephone, Alt Tele, RegNo, Verified, Establisment, EstProof, Medical/Insurance

def instloginpage(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in")
    return render(request,'auth/login_inst.html')

def instsignuppage(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in")
    return render(request,'auth/signup_inst.html')

def instlogin(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in")
    if request.method=='POST':
        login_username=request.POST['username']
        login_password=request.POST['password']

        user=authenticate(username=login_username,password=login_password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect("/")
        else:
            messages.error(request,'Login Failed')
            return HttpResponse("Oops! Login Failed")
    else:
        return HttpResponse("Unsecured Login Error !!")

def instsignup(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in")
    if request.method=='POST':
        # Obtaining Data From The HTML Form
        password=request.POST['password']
        cfpassword=request.POST['cfpassword']
        email=request.POST['email']
        name=request.POST['name']
        address = request.POST['address']
        telephone = request.POST['telephone']
        alt_telephone = request.POST['alt_telephone']
        insttype = request.POST['insttype']
        establishment = request.POST['establishment']
        reg_no = request.POST['reg_no']
        estproof = request.POST['estproof']
        institute = request.POST['institute']

        postnum = email[:4].upper() + str(randint(1000000000,9999999999))
        while len(User.objects.filter(username=postnum)) > 0:
            postnum = email[:4].upper() + str(randint(1000000000,9999999999))

        username = postnum

        if password != cfpassword:
            messages.error(request,"Passwords do not match")
            return redirect("/user/signuppage")

        # Default User Auth Save
        newuser = User.objects.create_user(username,email,password)
        newuser.first_name=name
        if institute == 'medical':
            newuser.last_name = "medical"
        else:
            newuser.last_name = "insurance"
        newuser.save()
        user=authenticate(username=username,password=password)
        login(request,user)

        if institute == 'medical':
            MedicalDetails(user=user,name=name,address=address,telephone=telephone,alt_telephone=alt_telephone,insttype=insttype,establishment=establishment,reg_no=reg_no,estproof=estproof).save()
        else:
            InsuranceDetails(user=user,name=name,address=address,telephone=telephone,alt_telephone=alt_telephone,insttype=insttype,establishment=establishment,reg_no=reg_no,estproof=estproof).save()
        

        messages.success(request,"User Account Created Successfully.")
        return HttpResponse("Your Unique Username/Registration ID is " + str(postnum) + "<br><a href='/'>Return Home</a>")
    else:
        return HttpResponse("Creating new user account failed !")


def logoutuser(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect("/")