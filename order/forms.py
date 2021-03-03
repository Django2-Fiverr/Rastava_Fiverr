from django import forms
from django.core import validators

from order.models import OrderDetail


# class OrderForm(forms.ModelForm):
#     gig_id = forms.IntegerField(
#         widget=forms.HiddenInput()
#     )
#
#     class Meta:
#         model = OrderDetail
#         fields = (
#             'gig_id',
#             'count',
#         )
#
#     def clean_count(self):
#         count = self.cleaned_data.get('count')
#         if int(count) < 1:
#             raise forms.ValidationError('تعداد محصول نمیتواند کمتر از 1 باشد')
#         return count


class OrderForm(forms.Form):
    gig_id = forms.IntegerField(widget=forms.HiddenInput())
    count = forms.IntegerField(widget=forms.NumberInput)

    def clean_count(self):
        count = self.cleaned_data.get('count')
        if count < 1:
            raise forms.ValidationError('تعداد نمیتواند کمتر از 1 باشد')
        return count

