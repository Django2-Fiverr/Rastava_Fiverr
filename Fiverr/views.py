from django.shortcuts import render
from proFile.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


def home_page(request):
    if request.user.is_authenticated:
        if not hasattr(request.user, 'profile'):
            Profile.objects.create(user=request.user)
    return render(request, 'home.html')
