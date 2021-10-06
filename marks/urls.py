from django.urls import path
from .views import *

urlpatterns = [
    path('upload-marks/', uploadMarks, name=None),
    path('students-marks/', studentsMarks, name=None),
]