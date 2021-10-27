from django.urls import path
from .views import *

urlpatterns = [
    path('upload-attendance/', uploadAttendance, name=None),
    path('students-attendance/', studentsAttendance, name=None),
    path('view-attendance/', viewAttendance, name=None),
    ]