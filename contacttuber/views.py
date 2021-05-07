from django.shortcuts import render,redirect
from .models import Contacttuber
from django.contrib import messages
# Create your views here.

def contacttuber(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        details = request.POST['details']

        contact = Contacttuber(username=username,phone=phone,email=email,company_name=company_name,subject=subject,details=details)
        contact.save()
        messages.success(request,'Contact Form submitted Successfully')
        return redirect('contact')
