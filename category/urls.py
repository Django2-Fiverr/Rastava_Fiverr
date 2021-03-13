from django.urls import path
from . import views

app_name = 'category'

urlpatterns = (
    path('<name>/', views.FieldsView.as_view(), name='fields-list'),
)