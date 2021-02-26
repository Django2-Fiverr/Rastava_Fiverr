from django import forms
from category.models import Category
from .models import Gig

# categories = Category.objects.all().values()
# CHOICES = [(category.get('name'), category.get('name').capitalize())
#            for category in categories]
# CHOICES2 = [(True, 'Available'), (False, 'Unavailable')]


# class GigForm(forms.Form):
#     category = forms.ChoiceField(choices=CHOICES)
#
#     cost = forms.IntegerField(required=True, widget=forms.TextInput(attrs={
#         'placeholder': 'Enter the price'}))
#
#     description = forms.CharField(required=True, widget=forms.Textarea(attrs={
#         'placeholder': 'Describe your service'}))
#
#     active = forms.ChoiceField(choices=CHOICES2)
#
#     Image = forms.ImageField()

class GigForm(forms.ModelForm):
    class Meta:
        model = Gig
        fields = ('category','cost','description','active','image')
