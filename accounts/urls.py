from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView, name=None),
    path('change-password/', change_password, name=None),
    path('send-otp/', send_otp, name=None),
    path('otp-verification/', otp_verification, name=None),
    path('forget-password/', forget_password, name=None),
    path('add-users/', addUsers, name=None),
]