from django.urls import re_path
from django.shortcuts import HttpResponse

urlpatterns = [
    re_path(r'^payment/?$', lambda req:HttpResponse("Payment page")),
]