from django.shortcuts import render
from .models import Order
# Create your views here.
def Orders(request):
    context = {
            'orders': Order.objects.filter(status = 'A', ).order_by('-id')
    }

    return render(request, 'order/order.html', context)

def DetailOrder(request, slug):
    context = {
            'detailorder': Order.objects.get(slug=slug)
    }

    return render(request, 'order/detailorder.html', context)