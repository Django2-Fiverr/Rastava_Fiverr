from django.shortcuts import render
from .models import Category

def category(request,hierarchy=''):
    root = Category.objects.all()
    return render(request, 'categories.html', category)