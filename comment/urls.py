from django.urls import path
from . import views

urlpatterns = [
    path('commentform/', views.post_comment, name='post_comment')
]