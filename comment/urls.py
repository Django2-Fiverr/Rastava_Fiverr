from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('add-comment/', views.add_comment, name='add-comment'),
    path('delete-comment/<int:pk>/<int:pk2>/', views.delete_comment, name='delete-comment'),
    path('reply-comment/<int:pk>/', views.reply, name='reply-comment'),
    path('update-comment/<int:pk>/', views.update_comment, name='update-comment'),
]
