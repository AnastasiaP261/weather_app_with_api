from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework import status
from weather_app.models import WeatherData
from datetime import datetime

User = get_user_model()


class WeatherAppTestCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.table_str = WeatherData.objects.create(city='city_name',
                                                   date_time=datetime.now(),
                                                   lon=50.2,
                                                   lat=40.8,
                                                   temp=8,
                                                   date_time_of_req=datetime.now(),
                                                   site='site_name',
                                                   )

    def test_answer(self):
        """
        Проверяет ответ запроса get_weather_set.
        1) Проверка статуса
        2) Проверка длины выданных данных
        3) Проверка соответствия ключей полченных словарей с ожидаемым набором ключей
        """
        response = self.client.get(path='/api/get_weather_set/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        assert list(response.data[0].keys()) == ['city', 'date_time', 'lon', 'lat', 'temp', 'date_time_of_req', 'site'], \
            'Ключи возвращенного словаря не совпадают с ожидаемыми.'
