from django.urls import path
from .views import * 

urlpatterns = [
    path('add-students/', studentdetails, name=None),
]