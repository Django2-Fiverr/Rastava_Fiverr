from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from extensions.constants import CATEGORY
from proFile.forms import UserEditForm
from proFile.forms import ProfileEditForm
from extensions.mainObjects import User




@login_required
def profile_view(request, pk):
    user = get_object_or_404(User, id=pk)
    context = {
        'profile': user.profile,
        'pk': pk,
        'categories': CATEGORY,
    }
    return render(request, 'profile_view.html', context)


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

    context = {'form': form,
               'profile_form': profile_form,
               'categories': CATEGORY,
               }
    return render(request, 'edit_profile.html', context)
