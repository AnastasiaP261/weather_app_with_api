from rest_framework import serializers
from weather_app.models import WeatherData


class WeatherDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherData
        fields = ('city', 'date_time', 'lon', 'lat', 'temp', 'date_time_of_req', 'site')
