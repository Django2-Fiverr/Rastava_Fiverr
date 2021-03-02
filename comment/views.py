from django.shortcuts import render
from .forms import CommentForm

def ViewComment(request):
    cmform = CommentForm()
    return render(request, 'comment.html', {'cmform': cmform})