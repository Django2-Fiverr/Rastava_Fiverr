from django.urls import path, include
from . import views

app_name = "proFile"

urlpatterns = [
    path('', views.profile_view, name="profile"),
    path('edit/', views.edit_profile, name="edit"),
]
