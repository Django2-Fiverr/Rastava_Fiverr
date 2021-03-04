from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Gig
from .forms import GigForm
from django.shortcuts import redirect
from django.utils import timezone
from comment.models import Comment
from comment.forms import CommentForm


@login_required
def create_gig(request):
    if request.method == 'POST':
        form = GigForm(data=request.POST, files=request.FILES)
        context = {
            'form': form
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
        }
    # return render(request, 'gigs/gig_operation.html', context)
    return render(request, 'gigs/gig_operation.html', context)


class GigList(ListView):
    model = Gig
    template_name = 'gigs/gig_list.html'
    context_object_name = 'gigs'
    paginate_by = 9

    def get_queryset(self):
        return Gig.objects.get_active_gigs()


def gig_detail(request, pk):
    gig = Gig.objects.get_by_id(pk)
    
    info = Comment.objects.all()
    if request.method == "POST":
        cmform = CommentForm(request.POST)
        if cmform.is_valid():
            comment = cmform.save(commit=False)
            comment.user = request.user
            comment.publish = timezone.now()
            comment.save()
            return redirect('/')
    else:
        cmform = CommentForm()
        if not gig:
            raise Http404('یافت نشد')
    context = {'info': info, 
               'cmform': cmform,
               'gig': gig,
    }
    return render(request, 'gigs/gig_detail.html', context)


class SearchGig(LoginRequiredMixin, ListView):
    model = Gig
    template_name = 'gigs/gig_list.html'
    context_object_name = 'gigs'
    paginate_by = 9

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query:
            return Gig.objects.search(query)
        else:
            return Gig.objects.get_active_gigs()


class MyGigList(LoginRequiredMixin, ListView):
    model = Gig
    template_name = 'components/my_gig.html'
    context_object_name = 'gigs'
    paginate_by = 9

    def get_queryset(self):
        request = self.request
        return Gig.objects.filter(user=request.user)


@login_required
def edit_gig(request, id):
    form = GigForm(instance=request.user.gig_set.filter(id=id).first())
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
    }
    return render(request, 'gigs/gig_operation.html', context)

