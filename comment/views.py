from django.shortcuts import render
from category.models import Category


def category(request, title):
    return render(request,'category.html')