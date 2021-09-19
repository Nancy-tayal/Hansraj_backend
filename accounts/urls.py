from django.urls import path
from .views import LoginView, change_password, otp_verification

urlpatterns = [
    path('login/', LoginView, name=None),
    path('change_password/', change_password, name=None),
    path('otp_verification/', otp_verification, name=None),
]