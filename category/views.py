from django.shortcuts import render
from category.models import Category
from django.shortcuts import get_list_or_404

def category(request,hierarchy=''):
    root = Category.objects.all()
