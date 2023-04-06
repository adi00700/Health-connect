from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('profile/',views.profile),
    path('dashboard/',views.dashboard),
    path('works/',views.works)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

