from rest_framework import viewsets

from api.api_weather_app.serializers import WeatherDataSerializer
from weather_app.views import WeatherData


# класс обработки апи. Он будет обрабатывать GET и POST для WeatherData без дополнительной работы
class WeatherViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
