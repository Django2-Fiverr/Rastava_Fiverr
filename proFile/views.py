from django.shortcuts import render, redirect
from proFile.models import Profile
from proFile.forms import RegisterForm, UserEditForm
from proFile.forms import ProfileEditForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()


@login_required
def profile_view(request, pk):
    user = User.objects.filter(id=pk).first()
    context = {
        'profile': user.profile,
        'pk':pk
    }
    return render(request, 'profile_view.html', context)


# def registration_view(request):
#     if request.method == 'POST':
#         user_form = RegisterForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(
#                 user_form.cleaned_data['password')
#             new_user.save()
#             profile = Profile.objects.create(user=new_user)
#             return render(request, 'proFile/register_done.html', {'new_user': new_user})
#     else:
#         user_form = RegisterForm()
#     return render(request, 'proFile/register.html', {'user_form': user_form})


@login_required
def edit_profile(request):
    form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    if request.method == 'POST':
        form = UserEditForm(instance=request.user,
                            files=request.FILES,
                            data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       files=request.FILES,
                                       data=request.POST)

        if form.is_valid() and profile_form.is_valid():
            print('The are valid')
            profile_form.save()
            form.save()
            return redirect('proFile:profile', request.user.id)

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'edit_profile.html', context)
