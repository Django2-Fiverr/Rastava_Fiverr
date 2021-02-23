from django.urls import path,include
from . import views

app_name = "proFile"

urlpatterns = [
    path('signin/',views.SignInView, name="SignIn"),
    path('register/',views.RegistrationView, name="Register"),
]
