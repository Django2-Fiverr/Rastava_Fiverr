import datetime

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from comment.models import Comment
from extensions.constants import CATEGORY
from gig.models import Gig
from .forms import CommentForm


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        gig_id = form.data.get('gig_id')
        gig = get_object_or_404(Gig, id=gig_id)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            time = datetime.datetime.now()
            Comment.objects.create(content=content, gig=gig, user=request.user, create=time)
        return redirect('gig:gig_detail', gig_id)
    else:
        raise Http404('Bad request')


@login_required
def delete_comment(request, pk, pk2):
    comment = get_object_or_404(Comment, id=pk)
    if request.user != comment.user:
        raise Http404('نمیتوان کامنت دیگران را حذف کرد')
    comment.delete()
    return redirect('gig:gig_detail', pk2)


@login_required
def reply(request, pk):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=pk)
        gig = get_object_or_404(Gig, id=comment.gig.id)
        form = CommentForm(request.POST)
        if form.is_valid():
            time = datetime.datetime.now()
            content = form.cleaned_data.get('content')
            Comment.objects.create(reply_to=comment, gig=gig, content=content, user=request.user, create=time)
            return redirect('gig:gig_detail', gig.id)

    form = CommentForm(initial={'gig_id': pk})
    context = {
        'comment_form': form,
        'option': 'ارسال',
        'categories': CATEGORY,
    }
    return render(request, 'comment_operation.html', context)


@login_required
def update_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if comment.user != request.user:
        raise Http404('نمیتوان نظرات دیگران را ویرایش کرد')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            comment.content = content
            comment.save()
            return redirect('gig:gig_detail',comment.gig.id)

    form = CommentForm(initial={'content': comment.content, 'gig_id': comment.gig.id})
    context = {
        'categories': CATEGORY,
        'comment_form': form,
        'option': 'ویرایش',
    }
    return render(request, 'comment_operation.html', context)
