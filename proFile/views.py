from django.shortcuts import render, redirect
from django.http import HttpResponse
from proFile.models import Profile
from user.models import User
from proFile.forms import RegisterForm, SignInForm
# from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# User = get_user_model


# def SignInView(request):
#     form = SignInForm()
#     if request.method == 'POST':
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     return render(request,'proFile/signin.html', {'form':form})

def SignInView(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'],password = cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('finish')
            else:
                return HttpResponse("Username or password is incorrect!")
    else:
        form = SignInForm()
    return render(request, 'proFile/signin.html', {'form':form})


@login_required(login_url="proFile:SignIn")
def LogOutView(request):
    logout(request)
    return redirect('/')

def RegistrationView(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'proFile/register_done.html', {'new_user':new_user})
    else:
        user_form = RegisterForm()
    return render(request,'proFile/register.html', {'user_form':user_form})    