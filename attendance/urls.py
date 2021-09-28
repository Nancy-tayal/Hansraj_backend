from django.urls import path
from .views import *

urlpatterns = [
    path('upload-attendance/', uploadAttendance, name=None),
    ]