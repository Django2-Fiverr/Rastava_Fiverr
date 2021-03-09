from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
import datetime

from gig.models import Gig
from order.forms import OrderForm
from order.models import Order, OrderDetail, Transaction


def check(request, pk):
    gig = get_object_or_404(Gig, id=pk)
    transaction = Transaction.objects.filter(client=request.user, gig=gig, expiration=False, delivery_status=False)
    if transaction:
        return True
    return False


@login_required
def add_order(request):
    order_form = OrderForm(request.POST or None)
    gig_id = order_form.data.get('gig_id')
    if check(request, gig_id):
        return render(request, 'deny_buy_same_gig.html')
    else:
        print('Hello man')
        if order_form.is_valid():
            order = Order.objects.filter(owner=request.user, paid=False).first()
            if not order:
                order = Order.objects.create(owner=request.user, paid=False)
            gig_id = order_form.cleaned_data['gig_id']
            gig = Gig.objects.get(id=gig_id)
            deadline = order_form.cleaned_data.get('deadline')
            price = gig.cost
            order.orderdetail_set.create(price=price, gig=gig, deadline=deadline)
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


def delete_order(request, pk):
    item = OrderDetail.objects.get(id=pk)
    item.delete()
    return redirect('order:order-details')


def create_time_object(time, deadline):
    delta = datetime.timedelta(days=deadline)
    return time + delta


def create_transaction(request, order):
    time = order.date_of_payment
    for item in order.orderdetail_set.all():
        seller = item.gig.user
        client = request.user
        gig = item.gig
        deadline = item.deadline
        transaction_deadline = create_time_object(time, deadline)
        Transaction.objects.create(seller=seller, client=client, gig=gig,
                                   date_of_transaction=time, deadline=transaction_deadline)
