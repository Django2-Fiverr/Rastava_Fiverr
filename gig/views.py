from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404

from .forms import GigForm, TransactionForm
from .models import Gig
from order.models import Transaction
from order.forms import OrderForm
from extensions.constants import CATEGORY
from extensions.mainObjects import User


@login_required
def create_gig(request):
    if request.method == 'POST':
        form = GigForm(data=request.POST, files=request.FILES)
        context = {
            'form': form,
            'categories': CATEGORY,
        }
        if form.is_valid():
            data = form.cleaned_data
            Gig(user=request.user, **data).save()
            return redirect('gig:my_gigs')
    else:
        form = GigForm()
        context = {
            'form': form,
            'text': 'ایجاد گیگ',
            'operation': 'ایجاد گیگ جدید',
            'title': 'ایجاد گیگ',
            'categories': CATEGORY,
        }
    # return render(request, 'gigs/gig_operation.html', context)
    return render(request, 'gigs/gig_operation.html', context)


class GigList(ListView):
    model = Gig
    template_name = 'gigs/gig_list.html'
    context_object_name = 'gigs'
    paginate_by = 9

    def get_context_data(self, *args, **kwargs):
        context = super(GigList, self).get_context_data(*args, **kwargs)
        context['categories'] = CATEGORY
        return context

    def get_queryset(self):
        return Gig.objects.get_active_gigs()


def gig_detail(request, pk):
    gig = Gig.objects.get_by_id(pk)
    order_form = OrderForm(request.POST or None, initial={'deadline': 0, 'gig_id': pk})
    if not gig:
        raise Http404('یافت نشد')
    context = {
        'gig': gig,
        'order_form': order_form,
        'categories': CATEGORY,
    }
    return render(request, 'gigs/gig_detail.html', context)


class SearchGig(ListView):
    model = Gig
    template_name = 'gigs/gig_list.html'
    context_object_name = 'gigs'
    paginate_by = 9

    def get_context_data(self, *args, **kwargs):
        context = super(SearchGig, self).get_context_data(*args, **kwargs)
        context['categories'] = CATEGORY
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query:
            return Gig.objects.search(query)
        else:
            return Gig.objects.get_active_gigs()


class GroupingGigs(ListView):
    model = Gig
    template_name = 'gigs/gig_list.html'
    context_object_name = 'gigs'
    paginate_by = 9

    def get_context_data(self, *args, **kwargs):
        context = super(GroupingGigs, self).get_context_data(*args, **kwargs)
        context['categories'] = CATEGORY
        return context

    def get_queryset(self):
        title = self.kwargs.get('title')
        result = Gig.objects.grouping_gigs(title)
        return result if result else Gig.objects.none()


class MyGigList(LoginRequiredMixin, ListView):
    model = Gig
    template_name = 'components/my_gig.html'
    context_object_name = 'gigs'
    paginate_by = 9

    def get_context_data(self, *args, **kwargs):
        context = super(MyGigList, self).get_context_data(*args, **kwargs)
        context['categories'] = CATEGORY
        return context

    def get_queryset(self):
        request = self.request
        return Gig.objects.filter(user=request.user)


class UserGigList(ListView):
    model = Gig
    template_name = 'gigs/gig_list.html'
    context_object_name = 'gigs'
    paginate_by = 9

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(User, id=pk)
        return Gig.objects.filter(user=user, active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(UserGigList, self).get_context_data(*args, **kwargs)
        context['categories'] = CATEGORY
        return context


@login_required
def edit_gig(request, id):
    gig = get_object_or_404(Gig, id=id)
    if request.user != gig.user:
        return render(request, 'gigs/deny_edit.html')
    form = GigForm(instance=gig)
    if request.method == 'POST':
        form = GigForm(instance=request.user.gig_set.filter(id=id).first(),
                       files=request.FILES,
                       data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('gig:my_gigs')
    context = {
        'form': form,
        'text': 'اعمال ویرایش',
        'operation': 'ویرایش گیگ',
        'title': 'ویرایش گیگ',
        'categories': CATEGORY,
    }
    return render(request, 'gigs/gig_operation.html', context)


@login_required
def my_sales(request):
    gigs = Transaction.objects.filter(seller=request.user)
    form = TransactionForm()
    context = {
        'gigs': gigs,
        'form': form,
        'categories': CATEGORY,
    }
    return render(request, 'gigs/my_sales.html', context)


@login_required
def my_purchases(request):
    gigs = Transaction.objects.filter(client=request.user)
    context = {
        'gigs': gigs,
        'categories': CATEGORY,
    }
    return render(request, 'gigs/my_purchases.html', context)


@login_required
def delete_confirmation(request, pk):
    gig = get_object_or_404(Gig, id=pk)
    if request.user != gig.user:
        raise Http404('You dont have permission to modify others services')
    context = {
        'pk': pk,
        'categories': CATEGORY,
    }
    return render(request, 'gigs/delete_confirmation.html', context)


@login_required
def delete_gig(request, pk):
    gig = get_object_or_404(Gig, id=pk)
    if not gig.user == request.user:
        raise Http404('Not allowed')
    gig.delete()
    return redirect('gig:my_gigs')


@login_required
def deliver(request, pk):
    if request.method == 'POST':
        transaction = get_object_or_404(Transaction, id=pk)
        form = TransactionForm(instance=transaction, files=request.FILES, data=request.POST)
        if form.is_valid():
            transaction.delivery_status = True
            form.save()
    else:
        return redirect('gig:my-sales')
    return redirect('gig:my-sales')
