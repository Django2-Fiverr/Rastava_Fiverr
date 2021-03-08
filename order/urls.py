from django.urls import path, re_path
from . import views

app_name = "order"

urlpatterns = [
    path('orders/', views.Orders, name="orders"),
    path('orders/<slug:slug>/', views.DetailOrder, name="detailorders"),
]