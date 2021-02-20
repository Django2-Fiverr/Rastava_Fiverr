from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="Username   * ",
                               widget=forms.TextInput(
                                   attrs={"class": "form-control", 'placeholder': 'Enter username'}))

    password = forms.CharField(required=True, label="Password   * ",
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control", "placeholder": "Enter password"}))


class RegisterForm(forms.Form):
    firstname = forms.CharField(required=True, label="First name ",
                                widget=forms.TextInput(
                                    attrs={"class": "form-control", 'placeholder': 'Enter first name'}))

    lastname = forms.CharField(required=True, label="Last name ",
                               widget=forms.TextInput(
                                   attrs={"class": "form-control", 'placeholder': 'Enter last name'}))

    username = forms.CharField(required=True, label="Username   * ",
                               widget=forms.TextInput(
                                   attrs={"class": "form-control", 'placeholder': 'pick a username'}))

    email = forms.EmailField(required=True, label="Email   * ",
                             widget=forms.EmailInput(
                                 attrs={"class": "form-control", 'placeholder': 'Enter Email'}))

    phone_number = forms.CharField(required=False, label="Phone number ",
                                   widget=forms.TextInput(
                                       attrs={"class": "form-control", 'placeholder': 'Enter phone number'}))

    age = forms.CharField(required=False, label="Age ",
                          widget=forms.TextInput(
                              attrs={"class": "form-control", 'placeholder': 'Enter your age'}))

    password = forms.CharField(required=True, label="Password   * ",
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control", "placeholder": "Enter password"}))

    password_again = forms.CharField(required=True, label="Confirm password   * ",
                                     widget=forms.PasswordInput(
                                         attrs={"class": "form-control", "placeholder": "Confirm password"}))

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password_again')
        if password != password2:
            raise forms.ValidationError('Passwords must match!!!')
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already used!!!')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username already taken!!!')
        return username
