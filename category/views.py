from django.shortcuts import render
from .models import Category

def category(request):
    category = Category.objects.all()
    context = { 
        'category': category
    }
    return render(request, 'categoryApp/category.html', context)