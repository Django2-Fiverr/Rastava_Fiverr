from django import forms
from user.models import User
from proFile.models import Profile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(required = True,widget = forms.PasswordInput)
    re_password = forms.CharField(required = True,widget = forms.PasswordInput)
    email = forms.EmailField(required = True,widget = forms.EmailInput)
    first_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            're_password',
            'email',
            'first_name',
            'last_name',
        )

    def clean_re_password(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password != re_password:
            raise forms.ValidationError("Password does not match!")
        return re_password

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     get_email = User.objects.filter(email=email).exists()
    #     if "@" not in email:
    #         raise forms.ValidationError("Email is not valid!")
    #     elif get_email:
    #         raise forms.ValidationError("This email has been already used!")
    #     return email

    
class SignInForm(forms.Form):
    username = forms.CharField(required = True)
    password = forms.CharField(required = True,widget = forms.PasswordInput)


    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     get_user = User.objects.filter(username=username).exists()
    #     if not get_user:
    #         raise forms.ValidationError("This username does not exist.Register first!")
    #     return username

    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     get_password = User.objects.filter(password=password)
    #     if get_password != password :
    #         raise forms.ValidationError("Password is wrong!")
    #     return password