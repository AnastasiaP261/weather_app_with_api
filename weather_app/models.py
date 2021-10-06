from django.db import models


class WeatherData(models.Model):
    # pk будет создан автоматически
    city = models.CharField(max_length=50)
    date_time = models.DateTimeField(blank=True, null=True)     # поле может быть пустым тк на одном из сайтов отсутствует подобное поле
    lon = models.FloatField()                                   # долгота
    lat = models.FloatField()                                   # широта
    temp = models.FloatField()
    date_time_of_req = models.DateTimeField()               # время когда данные были запрошены с сайта
    site = models.CharField(max_length=20)

