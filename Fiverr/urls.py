"""Fiverr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from azbankgateways.urls import az_bank_gateways_urls
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import settings, views

urlpatterns = [
    path('googleauth', TemplateView.as_view(template_name='authApp/index.html')), # for django-allauth
    path('', views.home_page),
    path('', TemplateView.as_view(template_name='authApp/index.html')),
    path('payment/',include('payment.urls')),
    path('site-info/',include('site_info.urls')),
    path('categories/',include('category.urls')),
    path('accounts/', include('user.urls')),
    path('gigs/', include('gig.urls')),
    path('profile/', include('proFile.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('allauth.urls')),  # for django-allauth
    # path('comments/', include('comment.urls'))
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
