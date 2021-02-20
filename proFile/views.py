from django.shortcuts import render
from .models import Profile
from user.models import User
from .forms import SignInForm

def SignIn(request):
    form = SignInForm()
    if request.method == 'POST':
        form =  SignInForm(request.POST)
        if form.is_valid():
            form.save()
            return ProfileView(request)
    return render(request,'Profile/signin.html',{'form':form})


def ProfileView(request):
    current_user=request.user
    # profile = Profile.objects.get(id)
    return render(request,'Profile/profile.html')