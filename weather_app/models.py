from django.db import models


class WeatherData(models.Model):
    # pk будет создан автоматически
    city = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    lon = models.FloatField()
    lat = models.FloatField()
    temp = models.FloatField()
    date_time_of_req = models.DateTimeField()       # время когда данные были запрошены с сайта
    site = models.CharField(max_length=20)

