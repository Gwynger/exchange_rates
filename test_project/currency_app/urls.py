# currency_app/urls.py
from django.urls import path
from .views import get_current_usd

urlpatterns = [
    path('', get_current_usd, name='home'),
    path('get-current-usd/', get_current_usd, name='get_current_usd'),
]


