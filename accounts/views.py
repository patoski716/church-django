from django.shortcuts import render
from django.contrib import messages
from .models import *
# Create your views here.
def home(request):
    return render (request,'home.html')

def donate(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        number = request.POST['number']
        amount = request.POST['amount']
    
        contact = Donate(last_name=last_name,first_name=first_name, email=email, number=number, amount=amount)
        contact.save()
        return render(request,"success.html")
    messages.success(request, 'Your message has been submitted, we will get back to you soon')
    return render (request,'donate.html')

def contact(request):
    if request.method == 'POST':    
        last_name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
    
        contact = Contact(name=last_name, email=email, number=number, message=message)
        contact.save()
        return render(request,"sent.html")
    messages.success(request, 'Your message has been submitted, we will get back to you soon')
    return render(request,'contact.html')