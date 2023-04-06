from django.db import models
from django.contrib.auth.models import User
from userauth.models import MedicalDetails,InsuranceDetails

# Create your models here.

class Report(models.Model):
    patient = models.ForeignKey(User,on_delete=models.CASCADE)
    disease = models.CharField(max_length=100)
    organ_affected = models.CharField(max_length=100)
    disease_serious = models.IntegerField(default=1) # Set max = 10 in html form
    medicalinst = models.ForeignKey(MedicalDetails,on_delete=models.DO_NOTHING)
    doctor = models.CharField(max_length=100)
    treatment = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=True)
    treatment_done = models.BooleanField(default=False)
    treatment_time = models.IntegerField(default=-1)
    survived = models.BooleanField(default=True)
    insured = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.first_name
    

class Appointment(models.Model):
    patient = models.ForeignKey(User,on_delete=models.CASCADE)
    schedule = models.DateTimeField()
    institute = models.ForeignKey(MedicalDetails,on_delete=models.DO_NOTHING)
    doctor = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.first_name
