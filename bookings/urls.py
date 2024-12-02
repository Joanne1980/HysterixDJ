from django.urls import path
from .views import Playing

urlpatterns = [
    path('', Playing.as_view(), name = 'bookings')

]