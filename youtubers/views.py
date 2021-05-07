from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Youtuber

# Create your views here.
def youtubers(request):
    youtuber = Youtuber.objects.order_by('-created_date')
    data = {
        'youtubers': youtuber,
    }
    return render(request,'youtubers/tubers.html',data)

def search(request):
    tubers = Youtuber.objects.all()
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            tubers = tubers.filter(description__icontains=keywords)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)

    if 'camera' in request.GET:
        camera = request.GET['camera']
        if camera:
            tubers = tubers.filter(camera_type__iexact=camera)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)

    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_search': camera_search,
        'category_search': category_search,
    }

    return render(request,'youtubers/search.html',data)

def youtubers_detail(request,id):
    youtuberdets = get_object_or_404(Youtuber, pk = id)
    data = {
        'singledets' : youtuberdets,
    }
    return render(request,'youtubers/youtuber_details.html',data)