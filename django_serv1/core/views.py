from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.


def ping(_request):
    return JsonResponse({"status": "ok"})
    
def datetime_epoch(_request):
    epoch = int(timezone.now().timestamp())  # datetime in EPOCH format
    return JsonResponse({"epoch": epoch})

def datetime_iso(_request):
    iso_time = timezone.now().isoformat()
    return JsonResponse({"datetime": iso_time})
    
def django_frontend(request):
    context = {"title": "Django frontend page", "name": "django_front_test_user"}
    return render(request, "django_frontend.html", context)