from django import forms
from django.contrib.auth import get_user_model
from django.core import validators

# use the custom user table ( the default one in settings.py )
User = get_user_model()


# create custom login form ( username and password are required )
# This form has some validation conditions defend by validators list
class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="نام کاربری",
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'نام کاربری را وارد کنید'}),
                               validators=[validators.MaxLengthValidator(limit_value=20,
                                                                         message='نام کاربری نمیتواند بیشتر از 20 کاراکتر باشد'),
                                           validators.MinLengthValidator(limit_value=5,
                                                                         message='نام کاربری نمیتواند کمتر از 5 کاراکتر باشد')])

    password = forms.CharField(required=True, label="کلمه ی عبور",
                               widget=forms.PasswordInput(
                                   attrs={"placeholder": "رمز خود را وارد کنید"}))


# create custom register form ( All fields are required but phoneNumber and age )
# This form has some validation conditions defend by validators list
class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True, label="نام",
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'نام خود را وارد کنید'}),
                                 validators=[validators.MaxLengthValidator(limit_value=20,
                                                                           message='نام نمیتواند بیشتر از 20 کاراکتر باشد'), ])

    last_name = forms.CharField(required=True, label="نام خانوادگی",
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'نام خانوادگی را وارد کنید'}),
                                validators=[validators.MaxLengthValidator(limit_value=30,
                                                                          message='نام خانوادگی نمیتواند بیشتر از 30 کاراکتر باشد'), ])

    # validator excepts username which contains ( 5 < ch < 20 ) characters
    username = forms.CharField(required=True, label="نام کاربری",
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'انتخاب نام کاربری'}),
                               validators=[validators.MaxLengthValidator(limit_value=20,
                                                                         message='نام کاربری نمیتواند بیشتر از 20 کاراکتر باشد'),
                                           validators.MinLengthValidator(limit_value=5,
                                                                         message='نام کاربری نمیتواند کمتر از 5 کاراکتر باشد')])

    email = forms.EmailField(required=True, label="آدرس ایمیل",
                             widget=forms.EmailInput(
                                 attrs={'placeholder': 'آدرس ایمیل را وارد کنید'}))

    phone_number = forms.CharField(required=False, label="شماره تماس",
                                   widget=forms.NumberInput(
                                       attrs={'placeholder': 'شماره تماس را وارد کنید (اختیاری)'}))

    age = forms.CharField(required=False, label="سن",
                          widget=forms.NumberInput(
                              attrs={'placeholder': 'سن خود را وارد کنید (اختیاری)'}))

    # validator excepts passwords which contain more than 6 characters
    password = forms.CharField(required=True, label="کلمه ی عبور",
                               widget=forms.PasswordInput(
                                   attrs={"placeholder": "انتخاب کلمه عبور"}),
                               validators=[validators.MinLengthValidator(limit_value=6,
                                                                         message='کلمه ی عبور نمیتواند کمتر از 6 کاراکتر باشد')])

    password_again = forms.CharField(required=True, label="تکرار کلمه ی عبور",
                                     widget=forms.PasswordInput(
                                         attrs={"placeholder": "تکرار کلمه ی عبور"}))

    # checks weather passwords are the same or not!

    def clean_password_again(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password_again')
        if password != password2:
            raise forms.ValidationError('عدم مطابقت کلمه ی عبور')
        return data

    # checks weather the email is taken already or not !
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('ایمیل توسط شخص دیگری استفاده شده است ')
        return email

    # checks weather the username is taken already or not!
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('نام کاربری توسط شخص دیگری استفاده شده است')
        return username
