from django.urls import path

from order import views

app_name = 'order'

urlpatterns = [
    path('add-order/', views.add_order, name='add-order'),
    path('delete-order/<int:pk>', views.delete_order, name='delete-order'),
    path('order-details/', views.order_details, name='order-details'),
]
