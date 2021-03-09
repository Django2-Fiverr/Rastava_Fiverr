from django.urls import path

from gig import views

app_name = 'gig'

urlpatterns = [
    path('create-gig/', views.create_gig, name='create_gig'),
    path('gigs-list/', views.GigList.as_view(), name='gig_list'),
    path('search/', views.SearchGig.as_view(), name='search'),
    path('grouping/<title>', views.GroupingGigs.as_view(), name='grouping'),
    path('gig-detail/<int:pk>/', views.gig_detail, name='gig_detail'),
    path('my-gigs/', views.MyGigList.as_view(), name='my_gigs'),
    path('user-gigs/<int:pk>', views.UserGigList.as_view(), name='user-gigs'),
    path('create-gig/', views.create_gig, name='create_gig'),
    path('delete-confirmation/<int:pk>/', views.delete_confirmation, name='delete-confirmation'),
    path('delete-gig/<int:pk>', views.delete_gig, name='delete-gig'),
    path('my_sales/', views.my_sales, name='my-sales'),
    path('my_purchases/', views.my_purchases, name='my-purchases'),
    path('edit-gig/<int:id>', views.edit_gig, name='edit_gig'),
]
