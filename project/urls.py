
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("payment.urls")),
]
