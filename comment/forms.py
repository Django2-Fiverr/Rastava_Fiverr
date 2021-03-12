from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    pk = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = (
            'content',
            'pk',
        )
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
