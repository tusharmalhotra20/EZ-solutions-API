from django.urls import path, include
from .views import usersList, VerifyEmail

urlpatterns = [
   	path('auth/register', usersList.as_view(), name="register"),
   	path('auth/login', usersList.as_view(), name="login"),
   	path('email-verify', VerifyEmail.as_view(), name="email-verify"),
]