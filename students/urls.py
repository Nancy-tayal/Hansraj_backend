from django.urls import path
from .views import * 

urlpatterns = [
    path('add-students/', studentdetails, name=None),
    path('subject-teachers-details/', subjectTeachers, name=None),
]