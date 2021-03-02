from django.urls import path
from . import views

urlpatterns = [
    path('createcm/', views.ViewComment, name='ViewComment'),
]