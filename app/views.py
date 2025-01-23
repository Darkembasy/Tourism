from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Content, Destination, Review, Activity
from django.db.models import Avg

# CreateView
class TouristSpotCreateView(CreateView):
    model = Review
    fields = ['name', 'text', 'location', 'type_of_Activity', 'rating']
    template_name = 'tourist_spot_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activities'] = Activity.objects.all()  # Fetch all activities
        return context

# ListView
class TouristSpotListView(ListView):
    model = Review
    template_name = 'touristspot_list.html'
    context_object_name = 'tourist_spots'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filtering
        search_query = self.request.GET.get('search')
        if search_query:
            context['tourist_spots'] = context['tourist_spots'].filter(
                name__icontains=search_query
            ) | context['tourist_spots'].filter(location__icontains=search_query)

        # Ordering
        order_by = self.request.GET.get('order_by')
        if order_by == 'rating':
            context['tourist_spots'] = context['tourist_spots'].order_by('-rating')
        elif order_by == 'name':
            context['tourist_spots'] = context['tourist_spots'].order_by('name')
        elif order_by == 'date_created':
            context['tourist_spots'] = context['tourist_spots'].order_by('-date_created')

        # Aggregation
        average_rating = Review.objects.all().aggregate(Avg('rating'))['rating__avg']
        context['average_rating'] = average_rating

        return context

# DetailView
class TouristSpotDetailView(DetailView):
    model = Review
    template_name = 'tourist_spot_detail.html'

# UpdateView
class TouristSpotUpdateView(UpdateView):
    model = Review
    fields = '__all__'
    template_name = 'tourist_spot_update.html'

# DeleteView
class TouristSpotDeleteView(DeleteView):
    model = Review
    template_name = 'tourist_spot_confirm_delete.html'
    success_url = '/tourist-spots/'

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
def intramuros(request):
    return render(request, 'app/intramuros.html')
def chocolate_hills(request):
    return render(request, 'app/chocolate_hills.html')
def mayon_volcano(request):
    return render(request, 'app/mayon_volcano.html')
def elnido_palawan(request):
    return render(request, 'app/elnido_palawan.html')
def ifugao(request):
    return render(request, 'app/ifugao.html')
def boracay(request):
    return render(request, 'app/boracay.html')


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

