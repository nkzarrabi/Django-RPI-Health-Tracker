from django.shortcuts import render
from django.http import JsonResponse
from .models import SleepData
from datetime import datetime, timedelta

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page")


def check_updates(request):
    last_checked = request.GET.get('last_checked')
    if last_checked:
        last_checked_time = datetime.strptime(last_checked, '%Y-%m-%dT%H:%M:%S')
    else:
        last_checked_time = datetime.now() - timedelta(days=1)  # default to 1 day ago if not specified

    updates = SleepData.objects.filter(updated_at__gt=last_checked_time).exists()
    return JsonResponse({'has_updates': updates})