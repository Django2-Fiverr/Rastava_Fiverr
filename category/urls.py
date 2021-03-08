from django.urls import path
from category import views

urlpatterns = [
    path('', views.category),
    path('تبلیغات و بازاریابی/', views.FieldList.as_view()),
]