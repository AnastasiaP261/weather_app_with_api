from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class WeatherAppTestCases(TestCase):
    def test_checking_redirects(self):
        """
        Проверка того, что при выполнении запроса
        GET /get_weather_data/?click=1
        произойдет редирект на
        GET /get_weather_data/
        """
        response = self.client.get(path=reverse('weather_app'),
                                   data={'click': 1})
        self.assertRedirects(response=response,
                             expected_url=reverse('weather_app'),
                             status_code=302,
                             target_status_code=200)
