from django.shortcuts import render
from .models import Slider, Teams
from youtubers.models import Youtuber
# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    teams = Teams.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    youtubers = Youtuber.objects.order_by('-created_date')
    data = {
        'sliders': sliders,
        'teams': teams,
        'featured': featured_youtubers,
        'tubers': youtubers,
    }
    return render(request, 'webpages/home.html',data)

def about(request):
    teams = Teams.objects.all()
    data = {
        'teams' : teams,
    }
    return render(request, 'webpages/about.html',data)

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')
