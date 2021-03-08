from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)