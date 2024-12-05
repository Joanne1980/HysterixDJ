from django.urls import path
from .views import Tunes

urlpatterns = [

path('', Tunes.as_view(), name = 'music')
    
]