import random

from django.shortcuts import render
from django.contrib.auth import get_user_model

from category.models import Category
from gig.models import Gig
from proFile.models import Profile

User = get_user_model()


def get_random_items(obj_class, count):
    obj = obj_class.objects.all()
    result = random.sample(list(obj), count)
    return result


bestsellers_gigs = get_random_items(Gig, 8)
newest_gigs = get_random_items(Gig, 8)
most_popular_gigs = get_random_items(Gig, 8)


def home_page(request):
    if request.user.is_authenticated:
        if not hasattr(request.user, 'profile'):
            Profile.objects.create(user=request.user)

    gigs = bestsellers_gigs
    gigs2 = newest_gigs
    gigs3 = most_popular_gigs

    context = {
        'categories': Category.objects.all(),

        'bestsellers_gigs1': gigs[0:4],
        'bestsellers_gigs2': gigs[4:8],

        'newest_gigs1': gigs2[0:4],
        'newest_gigs2': gigs2[4:8],

        'most_popular_gigs1': gigs3[0:4],
        'most_popular_gigs2': gigs3[4:8],

        'active_users': get_random_items(User, 4),
        'most_popular_users': get_random_items(User, 4),
        'professional_users': get_random_items(User, 4),
        'graded_users': get_random_items(User, 4),
        'admins': get_random_items(User, 4),
    }

    return render(request, 'home.html', context)
