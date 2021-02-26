from django.shortcuts import render, redirect
from django.http import HttpResponse
from proFile.models import Profile, Skills
from user.models import User
from proFile.forms import RegisterForm, UserEditForm, ProfileEditForm
# from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# User = get_user_model


# def signin_view(request):
#     if request.method == 'POST':
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username = cd['username'],password = cd['password'])
#             if user is not None:
#                 login(request, user)
#                 return render(request, 'proFile/home.html',{})
#             else:
#                 return HttpResponse("Username or password is incorrect!")
#     else:
#         form = SignInForm()
#     return render(request, 'proFile/signin.html', {'form':form})



# @login_required(login_url="proFile:SignIn")
# def logout_view(request):
#     logout(request)
#     return render(request, 'proFile/home.html',{})

@login_required
def dashboard(request):
    return render(request,'proFile/dashboard.html',{'section':'dashboard'})

def homepage(request):
    return render(request,'proFile/home.html')

def registration_view(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request,'proFile/register_done.html', {'new_user':new_user})
    else:
        user_form = RegisterForm()
    return render(request,'proFile/register.html', {'user_form':user_form})    

@login_required
def edit_view(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request,'proFile/edit_done.html',{})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'proFile/edit.html', {'user_form':user_form,'profile_form':profile_form})