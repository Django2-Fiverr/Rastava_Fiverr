from django.shortcuts import render
from .forms import CommentForm
from django.utils import timezone
from django.shortcuts import redirect
from gig.models import Gig


def post_comment(request):
    if request.method == "POST":
        cmform = CommentForm(request.POST)
        if cmform.is_valid():
            comment = cmform.save(commit=False)
            comment.user = request.user
            comment.publish = timezone.now()
            comment.save()
            return redirect('/gigs/gig-detail/1/')
    else:
        cmform = CommentForm()
    return render(request, 'comment.html', {'cmform': cmform})