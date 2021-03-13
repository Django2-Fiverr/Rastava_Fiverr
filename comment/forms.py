from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    gig_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = (
            'content',
            'gig_id',
        )
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
