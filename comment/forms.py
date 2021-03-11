from django import forms

from .models import Comment
from .models import ReplyComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'content',
        )
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = ReplyComment
        fields = (
            'content',
        )

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }
