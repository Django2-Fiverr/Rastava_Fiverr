from django.urls import path,include
from . import views

app_name = "proFile"

urlpatterns = [
    path('register/',views.registration_view, name="Register"),
    path('edit/',views.edit_view, name="Edit"),
    path('dashboard/',views.dashboard, name="Dashboard"),
    path('home/',views.homepage, name="Home"),
]
