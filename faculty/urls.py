from django.urls import path
from .views import *

urlpatterns = [
    path('subjects/', subjects, name=None),
    path('teachers/', teachers, name=None),
    path('subjectDetails/', subjectDetails, name=None),
]