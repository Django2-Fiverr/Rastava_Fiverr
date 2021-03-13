from django import forms

from site_info.models import Contact


class ContactForm(forms.ModelForm):
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Contact
        fields = (
            'full_name',
            'email',
            'subject',
            'message',
        )

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if any([char.isdigit() for char in full_name]):
            raise forms.ValidationError('نام و نام خانوادگی نمی تواند شامل اعداد باشد.')
        else:
            return full_name
