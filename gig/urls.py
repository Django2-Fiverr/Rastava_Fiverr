from django.urls import path

from gig import views

urlpatterns = [
    path('create-gig/', views.create_gig, name='create_gig')
]
