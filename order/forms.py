from django import forms


class OrderForm(forms.Form):
    gig_id = forms.IntegerField(widget=forms.HiddenInput())
    deadline = forms.IntegerField(widget=forms.NumberInput())

    def clean_deadline(self):
        count = self.cleaned_data.get('deadline')
        if count < 1:
            raise forms.ValidationError('مهلت نمیتواند کمتر از 1 روز باشد')
        return count
