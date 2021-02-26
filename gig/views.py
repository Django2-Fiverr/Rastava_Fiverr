from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Gig
from .forms import GigForm


@login_required
def create_gig(request):
    if request.method == 'POST':
        form = GigForm(data=request.POST, files=request.FILES)
        context = {
            'form': form
        }
        if form.is_valid():
            data = form.cleaned_data
            Gig(user=request.user, **data).save()
    else:
        form = GigForm()
        context = {
            'form': form,
        }
    return render(request, 'gig.html', context)
