from django.urls import path
from .views import ping, datetime_epoch, datetime_iso, django_frontend

urlpatterns = [
    path("ping/", ping),
    path("datetime_e/", datetime_epoch),  # <- /api/datetime_e
    path("datetime/", datetime_iso),  # <- /api/datetime
    path("django_frontend/", django_frontend),
]