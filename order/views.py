from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from gig.models import Gig
from order.forms import OrderForm
from order.models import Order, Transaction


@login_required
def add_order(request):
    order_form = OrderForm(request.POST or None)
    gig_id = order_form.data.get('gig_id')
    if order_form.is_valid():
        print('valid data')
        order = Order.objects.filter(owner=request.user, paid=False).first()
        if not order:
            order = Order.objects.create(owner=request.user, paid=False)
        gig_id = order_form.cleaned_data['gig_id']
        count = order_form.cleaned_data['count']
        gig = Gig.objects.get(id=gig_id)
        price = gig.cost * count
        order.orderdetail_set.create(price=price, count=count, gig=gig)
        return redirect('gig:gig_detail', gig_id)
    return redirect('gig:gig_detail', gig_id)

@login_required
def order_details(requset):
    order = Order.objects.filter(owner_id=requset.user.id, paid=False).first()
    if order:
        order_items = order.orderdetail_set.all()
    else:
        order_items = None
    context = {
        'order': order,
        'order_items': order_items
    }
    return render(requset, 'order_details.html', context)

@login_required
def my_orders(request):
    buy_list = Transaction.objects.filter(client=request.user)
    context = {
        'buy_list': buy_list,
    }
    return render(request,'my_orders.html', context)