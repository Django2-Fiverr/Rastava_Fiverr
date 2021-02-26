from django.urls import path

from gig import views

app_name = 'gig'

urlpatterns = [
    path('create-gig/', views.create_gig, name='create_gig'),
    path('gigs-list/', views.GigList.as_view(), name='gig_list'),
    path('search/', views.SearchGig.as_view(), name='search'),
    path('gig-detail/<int:pk>/', views.gig_detail, name='gig_detail'),
    path('my-gigs/', views.MyGigList.as_view(), name='my_gigs'),
    path('create-gig/', views.create_gig, name='create_gig'),
]
