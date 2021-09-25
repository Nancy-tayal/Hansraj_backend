from django.urls import path
from .views import * 

urlpatterns = [
    path('students/', studentdetails, name=None),
]