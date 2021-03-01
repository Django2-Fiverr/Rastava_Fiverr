from django import forms
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
        )

    def clean_re_password(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password != re_password:
            raise forms.ValidationError("عدم مطابقت کلمه ی عبور")
        return re_password


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
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
    class Meta:
        model = Profile
        fields = (
            'bio',
            'skills',
            'birth',
            'image',
        )
        widgets = {
            'bio': forms.Textarea(attrs={'placeholder': 'بیو گرافی'}),
            'skills': forms.CheckboxSelectMultiple(),
            'birth': forms.SelectDateWidget(years=list(range(1300, 1399, 1))),

        }
        labels = {
            'bio': 'بیوگرافی',
            'skills': 'مهارت ها',
            'birth': 'تاریخ تولد',
        }
