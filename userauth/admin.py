from django.contrib import admin
from .models import PatientDetails,MedicalDetails,InsuranceDetails
# Register your models here.

admin.site.register(PatientDetails)
admin.site.register(MedicalDetails)
admin.site.register(InsuranceDetails)