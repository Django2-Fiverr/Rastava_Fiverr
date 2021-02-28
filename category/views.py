from django.shortcuts import render
from category.models import Category,Post
from django.shortcuts import get_list_or_404

def category(request,hierarchy=''):
    category_slug = hierarchy.split('/')
    parent = ''
    root = Category.objects.all()

    for slug in category_slug[:-1]:
        parent = root.get(parent=parent, slug = slug)

    try:
        instance = Category.objects.get(parent=parent,slug=category_slug[-1])
    except:
        instance = get_list_or_404(Post, slug = category_slug[-1])
        return render(request, "postDetail.html", {'instance':instance})
    else:
        return render(request, 'categories.html', {'instance':instance})