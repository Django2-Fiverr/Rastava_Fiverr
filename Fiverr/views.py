from django.shortcuts import render

from extensions.functions import get_random_items
from extensions.mainObjects import User
from extensions.constants import CATEGORY
from gig.models import Gig
from proFile.models import Profile

bestsellers_gigs = get_random_items(Gig, 8)
newest_gigs = get_random_items(Gig, 8)
most_popular_gigs = get_random_items(Gig, 8)


def home_page(request):
    if request.user.is_authenticated:
        if not hasattr(request.user, 'profile'):
            Profile.objects.create(user=request.user)

    context = {
        'categories': CATEGORY,

        'bestsellers_gigs1': bestsellers_gigs[0:4],
        'bestsellers_gigs2': bestsellers_gigs[4:8],

        'newest_gigs1': newest_gigs[0:4],
        'newest_gigs2': newest_gigs[4:8],

        'most_popular_gigs1': most_popular_gigs[0:4],
        'most_popular_gigs2': most_popular_gigs[4:8],

        'active_users': get_random_items(User, 4),
        'most_popular_users': get_random_items(User, 4),
        'professional_users': get_random_items(User, 4),
        'graded_users': get_random_items(User, 4),
        'admins': get_random_items(User, 4),
    }

    return render(request, 'home.html', context)
