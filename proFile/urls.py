<<<<<<< HEAD
from django.urls import path,include
=======
from django.urls import path, include
>>>>>>> dev
from . import views

app_name = "proFile"

urlpatterns = [
<<<<<<< HEAD
    path('register/',views.registration_view, name="Register"),
    path('edit/',views.edit_view, name="Edit"),
    path('dashboard/',views.dashboard, name="Dashboard"),
    path('home/',views.homepage, name="Home"),
=======
    path('', views.profile_view, name="profile"),
    path('edit/', views.edit_profile, name="edit"),
>>>>>>> dev
]
