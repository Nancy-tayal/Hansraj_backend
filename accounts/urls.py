from django.urls import path
from .views import LoginView, change_password

urlpatterns = [
    path('login/', LoginView, name=None),
    path('change_password/', change_password, name=None),
]