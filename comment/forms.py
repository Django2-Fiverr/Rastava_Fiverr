from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'نظر خود را بنویسید...', 'rows': '2', 'cols': '10'}))
    class Meta:
        model = Comment
        fields = ('content',)

class UpdateCommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'نظر خود را بنویسید...', 'rows': '2', 'cols': '10'}))
    class Meta:
        model = Comment
        fields = ('content',)