from django import forms
from django.contrib.auth import get_user_model
from django.core import validators


# use the custom user table ( the default one in settings.py ) 
User = get_user_model()


# create custom login form ( username and password are required )
# This form has some validation conditions defiend by validators list
class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="Username   * ",
                                widget=forms.TextInput(
                                attrs={"class": "form-control", 'placeholder': 'Enter username'}),
                                validators=[validators.MaxLengthValidator(limit_value=20, message='Pick less than 20 charachters'),
                                validators.MinLengthValidator(limit_value=3, message='Pick more than 3 charachters')])

    password = forms.CharField(required=True, label="Password   * ",
                                widget=forms.PasswordInput(
                                attrs={"class": "form-control", "placeholder": "Enter password"}))


# create custom register form ( All fields are required but phoneNumber and age )
# This form has some validation conditions defiend by validators list
class RegisterForm(forms.Form):
    firstname = forms.CharField(required=True, label="First name  *",
                                widget=forms.TextInput(
                                attrs={"class": "form-control", 'placeholder': 'Enter first name'}))

    lastname = forms.CharField(required=True, label="Last name  * ",
                                widget=forms.TextInput(
                                attrs={"class": "form-control", 'placeholder': 'Enter last name'}))

    # validator excepts username which contains ( 5 < ch < 20 ) charachters
    username = forms.CharField(required=True, label="Username   * ",
                                widget=forms.TextInput(
                                attrs={"class": "form-control", 'placeholder': 'pick a username'}),
                                validators=[validators.MaxLengthValidator(limit_value=20, message='Pick less than 20 charachters'),
                                validators.MinLengthValidator(limit_value=5, message='Pick more than 3 charachters')])

    email = forms.EmailField(required=True, label="Email   * ",
                                widget=forms.EmailInput(
                                attrs={"class": "form-control", 'placeholder': 'Enter Email'}))

    phone_number = forms.CharField(required=False, label="Phone number ",
                                widget=forms.TextInput(
                                attrs={"class": "form-control", 'placeholder': 'Enter phone number'}))

    age = forms.CharField(required=False, label="Age ",
                                widget=forms.TextInput(
                                attrs={"class": "form-control", 'placeholder': 'Enter your age'}))

    # validator excepts passwords which contain more than 6 charachters
    password = forms.CharField(required=True, label="Password   * ",
                                widget=forms.PasswordInput(
                                attrs={"class": "form-control", "placeholder": "Enter password"}),
                                validators=[validators.MinLengthValidator(limit_value=6,message='Pick more than 6 charachters')])

    password_again = forms.CharField(required=True, label="Confirm password   * ",
                                widget=forms.PasswordInput(
                                attrs={"class": "form-control", "placeholder": "Confirm password"}))

# checks weather passwords are the same or not!
    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password_again')
        if password != password2:
            raise forms.ValidationError('Passwords must match!!!')
        return data

# checks weather the email is taken already or not !
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already used!!!')
        return email

# checks weather the username is taken already or not!
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username already taken!!!')
        return username
