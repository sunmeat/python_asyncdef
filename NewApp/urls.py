# NewApp / NewApp / urls.py:
from django.urls import path, include

urlpatterns = [
    path('', include('weather.urls')), # всі маршрути з додатку weather будуть доступні на корені сайту
]