from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from proFile.models import Profile
from extensions.mainObjects import User
from extensions.constants import CATEGORY
from .forms import LoginForm, RegisterForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = LoginForm(request.POST or None)
    context = {
        'form': form,
        'categories': CATEGORY,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
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
        'form': form,
        'categories': CATEGORY,
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
