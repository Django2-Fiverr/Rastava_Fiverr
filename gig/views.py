from django.shortcuts import render
from .models import Gig
# Create your views here.

def Gigs(request):
    context = {
            'gigs': Gig.objects.all()
    }

    return render(request, 'order/gig.html', context)