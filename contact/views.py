from django.shortcuts import render
from contact.models import Contact
from contact.forms import ContactForm

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        print(data)
        Contact.objects.create(**data).save()
    else:
        print(form.data)
    
    context ={
        'form': ContactForm()
    }    
        
    return render(request,'contact/contact.html', context)

