from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Content, Destination

def index(request):
    branches = Content()
    branches.name = 'Branches'
    branches.content1 ='Boracay'
    branches.content2 ='El Nido'
    branches.content3 ='ifugao'
    branches.content4 ='Intramuros'

    services = Content()
    services.name = 'Services'
    services.content1 ='Product'
    services.content2 ='Help and Support'
    services.content3 ='Pricing'
    services.content4 ='FAQ'

    contact_us = Content()
    contact_us.name = 'Contact Us'
    contact_us.content1 ='About Us'
    contact_us.content2 ='Our Team'
    contact_us.content3 ='Our Blog'
    contact_us.content4 ='Customers'

    content = [branches, services, contact_us]


    return render(request, 'app/index.html',{'content':content})

def faq(request):
    return render(request, 'app/faq.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    else:
      return render(request, 'app/login.html')

def registration(request):
  if request.method == 'POST':
     username = request.POST['username']
     email = request.POST['email']
     password = request.POST['password']
     confirm_password = request.POST['confirm_password']

     if password == confirm_password:
         if User.objects.filter(username=username).exists():
             messages.info(request, 'Username already taken')
             return redirect('registration')
         elif User.objects.filter(email=email).exists():
             messages.info(request, 'Email already taken')
             return redirect('registration')
         else:
             user = User.objects.create_user(username, email, password)
             user.save();
             return redirect('login')
     else:
         messages.info(request, 'Passwords do not match')
         return redirect('registration')
  else:
      return render(request, 'app/registration.html')

