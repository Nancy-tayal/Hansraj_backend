from django.urls import path
from .views import LoginView, change_password, otp_verification, send_otp

urlpatterns = [
    path('login/', LoginView, name=None),
    path('change_password/', change_password, name=None),
    path('send_otp/', send_otp, name=None),
    path('otp_verification/', otp_verification, name=None),
]