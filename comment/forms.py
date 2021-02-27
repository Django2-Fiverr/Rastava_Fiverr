from django import forms
from .models import Comment

class CommentForm(form.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'profile',
            'user',
            'comment',
        ]