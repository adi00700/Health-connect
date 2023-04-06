from django.db import models
from userauth.models import PatientDetails,InsuranceDetails
from django.contrib.auth.models import User

# Create your models here.

class SubRequest(models.Model):
    insurer = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(PatientDetails,on_delete=models.CASCADE)
    healthscore = models.IntegerField(default=100)
    req_date = models.DateField(auto_now_add=True)
    pending = models.BooleanField(default=True)
    prem_cost = models.IntegerField(null=True,blank=True)
    pat_accept = models.BooleanField(default=False)
    pat_reject = models.BooleanField(default=False)

    def __str__(self):
        return self.insurer.name

class Subscriber(models.Model):
    insurer = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(PatientDetails,on_delete=models.CASCADE)
    healthscore = models.IntegerField(default=100)
    start_date = models.DateField(auto_now_add=True)
    prem_cost = models.IntegerField(null=True,blank=True)
    pay_pending = models.BooleanField(default=False)

    def __str__(self):
        return self.insurer.name
    
class Branches(models.Model):
    insurer = models.ForeignKey(User,on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.insurer.name