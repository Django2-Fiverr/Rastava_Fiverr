from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from proFile.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


# def login_user(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     form = LoginForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         print(form.cleaned_data)
#         userName = form.cleaned_data.get("userName")
#         password = form.cleaned_data.get("password")
#         user = authenticate(request, username=userName, password=password)
#         if user is not None:
#             login(request, user)
#             context["form"] = LoginForm()
#             return redirect('/')
#         else:
#             print(User.objects.filter(username = userName,password=password))
#             print("Error")
#
#     return render(request, "login.html", context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            form.add_error('username', 'کاربری با مشخصات فوق یافت نشد')
    return render(request, 'login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')


def register_user(request):
    if request.user.is_authenticated:
        login(request, request.user)
        return redirect('/')

    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        data = form.cleaned_data
        data.popitem()
        User.objects.create_user(**data)
        user = authenticate(**data)
        Profile.objects.create(user=user)
        login(request, user)
        return redirect('/')
    return render(request, 'register.html', context)
