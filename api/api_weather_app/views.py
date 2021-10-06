from rest_framework import viewsets

from weather_app.views import WeatherData
from api.api_weather_app.serializers import WeatherDataSerializer


# класс обработки апи. Он будет обрабатывать GET и POST для WeatherData без дополнительной работы
class ViewWeatherApi(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
