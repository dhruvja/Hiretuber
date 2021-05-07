from django.shortcuts import render,redirect
from .models import Hiretubers
from django.contrib import messages
# Create your views here.


def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        city = request.POST['first_name']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        user_id = request.POST['user_id']

        hiretubers = Hiretubers(first_name=first_name, last_name=last_name,email = email,city = city,state=state,phone=phone,message=message,tuber_id=tuber_id,tuber_name=tuber_name,user_id=user_id)
        hiretubers.save()
        messages.success(request, 'Thanks for Contacting us')
        return redirect('youtubers')
