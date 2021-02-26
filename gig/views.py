from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

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


class GigList(ListView):
    model = Gig
    template_name = 'gigs/gig_list.html'
    context_object_name = 'gigs'
    paginate_by = 9

    def get_queryset(self):
        return Gig.objects.get_active_gigs()


def gig_detail(request, pk):
    gig = Gig.objects.get_by_id(pk)
    if not gig:
        raise Http404('یافت نشد')
    context = {
        'gig': gig
    }
    return render(request, 'gigs/gig_detail.html', context)


class SearchGig(ListView):
    model = Gig
    template_name = 'gigs/gig_list.html'
    context_object_name = 'gigs'
    paginate_by = 9

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query:
            return Gig.objects.search(query)
        else:
            return Gig.objects.get_active_gigs()

