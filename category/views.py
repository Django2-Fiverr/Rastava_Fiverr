from django.views import generic

from extensions.constants import CATEGORY
from .models import Field


class FieldsView(generic.ListView):
    model = Field
    paginate_by = 9
    template_name = 'fields_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FieldsView,self).get_context_data(*args,**kwargs)
        context['categories'] = CATEGORY
        return context

    def get_queryset(self):
        name = self.kwargs.get('name')
        return Field.objects.get_fields(name)


