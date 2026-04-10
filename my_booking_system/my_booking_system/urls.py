from django.contrib import admin
from django.urls import path, include
from appointments.views import book_appointment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointments/', include('appointments.urls')),
    path('', book_appointment, name='home'),
]
