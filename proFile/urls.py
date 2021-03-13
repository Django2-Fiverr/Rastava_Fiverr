from django.urls import path, include
from . import views

app_name = "proFile"

urlpatterns = [
    path('<int:pk>/', views.profile_view, name="profile"),
    path('edit/', views.edit_profile, name="edit"),
]
