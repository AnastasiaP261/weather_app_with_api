from django.urls import include, path
from rest_framework import routers

from .views import WeatherViewSet

# создает соответствующие пункты в меню ApiRoot по адресу http://127.0.0.1:8000/api/
router = routers.DefaultRouter()
router.register(r'get_weather_set', WeatherViewSet, basename='api_get_weather_set')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
