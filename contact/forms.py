from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(max_length=50, widget= forms.TextInput(attrs={'class': 'form-control'}), label='نام ونام خانوادگی')
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='ایمیل')
	subject = forms.CharField(max_length=50, widget= forms.TextInput(attrs={'class': 'form-control'}), label='موضوع')
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=500, label='متن پیام')
