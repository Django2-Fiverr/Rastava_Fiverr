from django.shortcuts import render
from comment.models import Comment, ReplyComment
from comment.forms import CommentForm
from proFile.models import Profile

def comment(request,my_id):
    comments = Comment.objects.filter(profile_id=my_id)
    is_active = True

    form = CommentForm(request.profile)
    
    if request.method == "PROFILE" and form.is_valid():
        instance = form.save(commit=True)
        instance.profile = obj
        instance.user = user
        instance.save()
        form = CommentForm()
    
        dic = {
        "object" : obj,
        "comments":comments,
        "is_active":is_active,
        "form" : form
        }
    print(form.as_p)
    return render(request, 'detail.html',dic)
