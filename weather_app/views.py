import json
from datetime import datetime

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from local_properties.api_keys import API_KEYS
from .models import WeatherData


# класс для отображения страницы, реализует основной бизнес-процесс данного приложения
class ViewWeather(TemplateView):
    template_name = 'get_weather.html'
    model = WeatherData

    def get(self, request, *args, **kwargs):
        # по нажатию кнопки выполняется get-запрос с параметром click=1
        # этот параметр - индикатор того, была ли нажата кнопка(в таком случае нуэжо делать
        # запросы к апи сайтов) или было просто запрошена страница и ее надо просто отобразить
        req = self.request.GET
        if req:
            # для того, чтобы добавить метку времени получения записей
            date_time_of_req = datetime.now()

            # работа с апи сайтов и занесение информации в бд
            self.get_data_from_weatherbit(date_time_of_req)
            self.get_data_from_openweathermap(date_time_of_req)

            return HttpResponseRedirect(reverse('weather_app'))
        return render(request, self.template_name, {})

    def get_data_from_weatherbit(self, date_time_of_req):
        url = 'https://api.weatherbit.io/v2.0/current'
        params = {
            'lon': 37.61556,  # координаты Москвы
            'lat': 55.4507,  # координаты Москвы
            'key': API_KEYS["weatherbit"],
        }
        result = requests.get(url, params=params)

        item = json.loads(result.content)['data'][0]
        print(item)
        obj = self.model.objects.create(
            city=item['city_name'],
            date_time=item['ob_time'],
            lat=item['lat'],
            lon=item['lon'],
            temp=item['temp'],
            site="weatherbit",
            date_time_of_req=date_time_of_req,
        )
        obj.save()

    def get_data_from_openweathermap(self, date_time_of_req):
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'lon': 37.61556,  # координаты Москвы
            'lat': 55.4507,  # координаты Москвы
            'appid': API_KEYS["openweathermap"],
        }
        result = requests.get(url, params=params)

        item = json.loads(result.content)
        obj = self.model.objects.create(
            city=item['name'],
            # date_time=item['ob_time'],  # на этом сайте нет таймштампа
            lat=item['coord']['lat'],
            lon=item['coord']['lon'],
            temp=item['main']['temp'],
            site="openweathermap",
            date_time_of_req=date_time_of_req,
        )
        obj.save()
