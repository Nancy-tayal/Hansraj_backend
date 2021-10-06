from django.urls import path
from .views import *

urlpatterns = [
    path('add-subjects/', subjects, name=None),
    path('add-teachers/', teachers, name=None),
    path('add-subject-details/', subjectDetails, name=None),
    path('subjects-list/', subjectsList, name=None),
    path('students-details/', studentsDetails, name=None),
    ]