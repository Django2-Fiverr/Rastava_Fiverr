from django import forms
<<<<<<< HEAD
from user.models import User
from proFile.models import Profile, Skills

# class SignInForm(forms.Form):
#     username = forms.CharField(required = True)
#     password = forms.CharField(required = True,widget = forms.PasswordInput)


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


class RegisterForm(forms.ModelForm):
    password = forms.CharField(required = True,widget = forms.PasswordInput)
    re_password = forms.CharField(required = True,widget = forms.PasswordInput)
    # email = forms.EmailField(required = True,widget = forms.EmailInput)
    # first_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            're_password',
            'email',
            'first_name',
            'last_name',
=======
# from user.models import User
from proFile.models import Profile, Skills
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class RegisterForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    re_password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            're_password',
>>>>>>> dev
        )

    def clean_re_password(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password != re_password:
<<<<<<< HEAD
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

    
=======
            raise forms.ValidationError("عدم مطابقت کلمه ی عبور")
        return re_password


>>>>>>> dev
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
<<<<<<< HEAD
        )

class ProfileEditForm(forms.ModelForm):
    # skills = forms.ChoiceField(choices=[
    #     (item.pk, item) for item in Skills.objects.all()])
    # skills = forms.ModelChoiceField(queryset = Skills.objects.all())
=======
            'age',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'شماره تماس'}),
            'age': forms.NumberInput(attrs={'placeholder': 'سن'}),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
            'age': 'سن',
        }


class ProfileEditForm(forms.ModelForm):
>>>>>>> dev
    class Meta:
        model = Profile
        fields = (
            'bio',
            'skills',
            'birth',
            'image',
<<<<<<< HEAD
        )
=======
        )
        widgets = {
            'bio': forms.Textarea(attrs={'placeholder': 'بیو گرافی'}),
            'skills': forms.CheckboxSelectMultiple(),
            'birth': forms.SelectDateWidget(years=list(range(1300, 1399, 1)))
        }
        labels = {
            'bio': 'بیوگرافی',
            'skills': 'مهارت ها',
            'birth': 'تاریخ تولد',
        }
>>>>>>> dev
