# NewApp / weather / urls.py:
from django.urls import path
from .views import ( # правильний явний імпорт подань з views.py
    hello_sync,
    time_sync,
    echo_sync,
    hello_async,
    fetch_weather_async,
)

urlpatterns = [
    # синхронні
    path('', hello_sync, name='hello-sync'),
    path('time-sync/', time_sync, name='time-sync'),
    path('echo-sync/', echo_sync, name='echo-sync'), # цей маршрут приймає POST-запити, тому гетом його не викликаємо, а тестуємо через curl або Postman

    # асинхронні
    path('hello-async/', hello_async, name='hello-async'),
    path('weather/', fetch_weather_async, name='weather'),
]