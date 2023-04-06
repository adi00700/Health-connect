from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
# Create your models here.

class PatientDetails(models.Model):
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
    BLOOD_GROUP = [
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-')
    ]
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    age=models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,default='Male')
    blood = models.CharField(max_length=5, choices=BLOOD_GROUP,default='B+')
    perm_address = models.CharField(max_length=200)
    emg_contact = models.CharField(max_length=10,null=True,blank=True)
    family_doctor = models.CharField(max_length=50,blank=True,null=True)
    profile = models.ImageField(upload_to='patientprofile/')

    def __str__(self):
        return self.name

@receiver(post_delete, sender=PatientDetails)
def patient_delete(sender,instance, **kwargs):
    if instance.profile:
        if os.path.isfile(instance.profile.path):
            os.remove(instance.profile.path)


# InstType(pvt,govt,semipvt,indi), Name, Address, Telephone, Alt Tele
# RegNo, Verified, Establisment, EstProof
class MedicalDetails(models.Model):
    INST_TYPE = [
        ('Private','Private'),
        ('Government','Government'),
        ('SemiPrivate','SemiPrivate'),
        ('Individual','Individual')
    ]
    MEDICAL_TYPE = [
        ('Allopathy','Allopathy'),
        ('Homeopathy','Homeopathy'),
        ('Naturopathy','Naturopathy'),
        ('Ayurvedic','Ayurvedic')
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=12)
    alt_telephone = models.CharField(max_length=12,null=True,blank=True)
    insttype = models.CharField(max_length=20,choices=INST_TYPE,default='Private')
    medicining = models.CharField(max_length=30,choices=MEDICAL_TYPE,default='Allopathy')
    establishment = models.DateField()
    reg_no = models.CharField(max_length=100)
    estproof = models.FileField(upload_to='instproof/')
    profile = models.ImageField(upload_to='medicalprofile/',blank=True,null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
@receiver(post_delete, sender=MedicalDetails)
def patient_delete(sender,instance, **kwargs):
    if instance.estproof:
        if os.path.isfile(instance.estproof.path):
            os.remove(instance.estproof.path)
    if instance.profile:
        if os.path.isfile(instance.profile.path):
            os.remove(instance.profile.path)



class InsuranceDetails(models.Model):
    INST_TYPE = [
        ('Private','Private'),
        ('Government','Government'),
        ('SemiPrivate','SemiPrivate'),
        ('Individual','Individual')
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=12)
    alt_telephone = models.CharField(max_length=12,null=True,blank=True)
    insttype = models.CharField(max_length=20,choices=INST_TYPE,default='Private')
    establishment = models.DateField()
    reg_no = models.CharField(max_length=100)
    estproof = models.FileField(upload_to='instproof/')
    profile = models.ImageField(upload_to='insureprofile/',blank=True,null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
@receiver(post_delete, sender=InsuranceDetails)
def patient_delete(sender,instance, **kwargs):
    if instance.estproof:
        if os.path.isfile(instance.estproof.path):
            os.remove(instance.estproof.path)
    if instance.profile:
        if os.path.isfile(instance.profile.path):
            os.remove(instance.profile.path)