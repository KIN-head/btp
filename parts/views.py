from django.shortcuts import render
from django.utils import timezone
from .models import Request

# Create your views here.
def request_list(request):
    #return render(request, 'parts/request_list.html', {})
    requests = Request.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'parts/request_list.html', {'requests': requests})

def index(request):
    return render(request, 'parts/index.html', {})
