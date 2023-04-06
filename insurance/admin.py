from django.contrib import admin
from .models import Branches,SubRequest,Subscriber
# Register your models here.

admin.site.register(Branches)
admin.site.register(SubRequest)
admin.site.register(Subscriber)