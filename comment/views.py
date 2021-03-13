
# MOVED COMMENT VIEWS TO GIG (gig_detail)

"""
from django.shortcuts import render
from .forms import CommentForm
from django.utils import timezone
from django.shortcuts import redirect
from gig.models import Gig
from comment.models import Comment
from django.contrib.auth import get_user_model




User = get_user_model()

def post_comment(request):
    info = Comment.objects.all()
    if request.method == "POST":
        cmform = CommentForm(request.POST)
        if cmform.is_valid():
            comment = cmform.save(commit=False)
            comment.user = request.user
            comment.publish = timezone.now()
            comment.save()
            return redirect('/comments/commentform')
    else:
        cmform = CommentForm()
    
    context = {'info': info, 'cmform': cmform}
    return render(request, 'comment.html', context)

"""
