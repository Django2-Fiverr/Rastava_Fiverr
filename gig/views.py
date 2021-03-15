from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
import datetime
from comment.models import Comment
from comment.forms import CommentForm, UpdateCommentForm
import urllib
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.urls import reverse
from django.contrib.auth import get_user_model
from order.models import Transaction, OrderDetail
from order.forms import OrderForm
from extensions.constants import CATEGORY, COMMENTS, set_comment_publish
from extensions.mainObjects import User
from .models import Gig
from .forms import GigForm, TransactionForm

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



# GIG + COMMENTS
def gig_detail(request, pk):
    user = User.objects.filter(id=pk).first()
    gig = Gig.objects.get_by_id(pk)
    order_form = OrderForm(request.POST or None, initial={'count': 0, 'gig_id': pk})
    info = Comment.objects.filter(status=True, gig=gig, reply=None)
    buyer = Transaction.objects.filter(gig=gig)
    if request.method == "POST":
        cmform = CommentForm(request.POST)
        if cmform.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(gig=gig, user=request.user, content=content, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(comment.gig.get_absolute_url())        
    else:
        cmform = CommentForm()
        if not gig:
            raise Http404('یافت نشد')
    
    context = {'info': info, 
               'cmform': cmform,
               'gig': gig,
               'order_form': order_form,
               'buyer': buyer,
    }
    # if request.is_ajax():
    #     html = render_to_string('gig/gig_detail.html', context, request=request)
    #     return JsonResponse({'form': html})
    return render(request, 'gigs/gig_detail.html', context)


@login_required
def update_comment(request, pk):
    gig = Gig.objects.get_by_id(pk)
    detail = Comment.objects.filter(status=True, pk=pk)
    comment = ''
    my_form = UpdateCommentForm(instance=Comment.objects.get(pk=pk))
    if request.method == 'POST':
        my_form = UpdateCommentForm(instance=Comment.objects.get(pk=pk) ,data=request.POST)
        if my_form.is_valid():
            comment = my_form.save(commit=False)
            comment.save()
            return HttpResponseRedirect(comment.gig.get_absolute_url())
    context = {
        'detail': detail,
        'my_form': my_form,
        'gig': gig,
        }
    return render(request, 'gigs/update_comment.html', context)


def delete_comment(request, id):
    context = {}
    obj = Comment.objects.get(id = id)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(obj.gig.get_absolute_url())
    return render(request, "delete_cm.html", context)


def reply_comment():
    pass



class SearchGig(LoginRequiredMixin, ListView):
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
    return redirect('gig:my-sales')
