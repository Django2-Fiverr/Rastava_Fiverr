from django.shortcuts import render
from contact.models import Contact
from django.contrib import messages

def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subgect']
        message = request.POST['message']
 
    return render(request,'contact/contact.html')
      

