from django.urls import path
from .views import ping, datetime_epoch

urlpatterns = [
    path("ping/", ping),
    path("datetime/", datetime_epoch),  # <- /api/datetime
]