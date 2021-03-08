from django.shortcuts import render
from .models import Category, Field
from django.views.generic import ListView


def category(request):
    category = Category.objects.all()
    context = { 
        'category': category
    }
    return render(request, 'categoryApp/category.html', context)


class FieldList(ListView):
    model = Field
    template_name = 'categoryApp/field_list.html'
    context_object_name = 'fields'
    paginate_by = 9

    def get_queryset(self):
        return Field.objects.all()