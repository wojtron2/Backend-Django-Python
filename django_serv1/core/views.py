from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def ping(_request):
    return JsonResponse({"status": "ok"})
    
def datetime_epoch(_request):
    epoch = int(timezone.now().timestamp())  # datetime in EPOCH format
    return JsonResponse({"epoch": epoch})