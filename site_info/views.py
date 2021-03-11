from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import About
from category.models import Category

category = Category.objects.all()


def about_us(request):
    about = About.objects.all().first()
    context = {
        'about': about,
        'categories':category,
    }
    return render(request, 'about_us.html', context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('site-info:contact-us')
    else:
        form = ContactForm()
    context = {
        'form': form,
        'categories': category,
    }

    return render(request, 'contact_us.html', context)
