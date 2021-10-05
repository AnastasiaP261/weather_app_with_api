from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from local_properties.api_keys import API_KEYS
import sqlite3
import requests
import json
from datetime import datetime
import urllib
from .models import WeatherData
from django.urls import reverse


class ViewWeather(TemplateView):
    template_name = 'get_weather.html'
    model = WeatherData
# можно было оформить представления в виде классов, но
# так как в приложении нет страниц как таковых и весь функционал классов все равно
# не будет использоваться, я решила что это лишнее
    def get(self, request, *args, **kwargs):
        req = self.request.GET
        if req:
            date_time_of_req = datetime.now()       # для того, чтобы добавить метку времени получения записи

            self.get_data_from_weatherbit(date_time_of_req)
            self.get_data_from_openweathermap(date_time_of_req)




            return HttpResponseRedirect(reverse('weather_app'))
        return render(request, self.template_name, {})

    def get_data_from_weatherbit(self, date_time_of_req):
        url = 'https://api.weatherbit.io/v2.0/current'
        params = {
            # 'city_id': 524901,
            'lon': 37.61556,  # координаты Москвы
            'lat': 55.4507,  # координаты Москвы
            'lang': 'ru',
            'key': API_KEYS["weatherbit"],
        }
        result = requests.get(url, params=params)

        for item in json.loads(result.content)['data']:
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
        return result

    def get_data_from_openweathermap(self, date_time_of_req):
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            # 'city_id': 524901,
            'lon': 37.61556,    # координаты Москвы
            'lat': 55.4507,     # координаты Москвы
            'lang': 'ru',
            'appid': API_KEYS["openweathermap"],
        }
        result = requests.get(url, params=params)
        print(json.loads(result.content))
        for item in [json.loads(result.content)]:
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
        return result
