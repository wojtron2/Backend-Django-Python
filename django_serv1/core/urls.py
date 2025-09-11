from django.urls import path
from .views import ping, datetime_epoch

urlpatterns = [
    path("ping/", ping),
    path("datetime_e/", datetime_epoch),  # <- /api/datetime_e
    path("datetime/", datetime_iso),  # <- /api/datetime
]