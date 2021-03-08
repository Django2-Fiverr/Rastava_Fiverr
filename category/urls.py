from django.urls import path
from category import views

urlpatterns = [
    path('', views.category),
    path('تبلیغات و بازاریابی/', views.FieldList.as_view()),
    path('تایپ، ترجمه و نویسندگی/', views.FieldList.as_view()),
    path('گرافیک/', views.FieldList.as_view()),
    path('یرنامه نویسی/', views.FieldList.as_view()),
    path('دستیار مجازی/', views.FieldList.as_view()),
    path('انیمیشن/', views.FieldList.as_view()),
    path('موسیقی و صدا/', views.FieldList.as_view()),
]