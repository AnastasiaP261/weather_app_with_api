# ЗАПУСК ПРИЛОЖЕНИЯ НА BASH:
### Способ 1:
(для запуска необходим предустановленный Docker)

`$ docker run --rm -p 8000:8000  nesteatea/test_for_proeshelon:0.0.0`

Для просмотра работы веб-приложения открыть в браузере страницу http://0.0.0.0:8000/
Для остановки ввести комбинацию Ctrl+C


### Способ 2:
Открыть bash-терминал в корневой папке проекта.
Ввести

`$ pip3 install -r requirements.txt`  
`$ python3 manage.py runserver`

Для просмотра работы веб-приложения открыть в браузере страницу http://0.0.0.0:8000/
Для остановки ввести комбинацию Ctrl+C

# ОПИСАНИЕ РАБОТЫ ПРИЛОЖЕНИЯ
На стартовой странице нажать кнопку отправки. Сервер приложения поочереди отправит запросы к апи сайтов
- https://openweathermap.org/current#current_JSON
- https://www.weatherbit.io/api/swaggerui/weather-api-v2#!/Current32Weather32Data/get_current_city_id_city_id  
  
и получит от них ответы в формате json(см. test_for_proeshelon/weather_app/views.py). Далее он обработает эти данные и отправит их в базу данных. Вернет пользователю ту же страниц, на которой он был.

При переходе по адресу http://0.0.0.0:8000/api/ будет отображена корневая страница апи приложения.
При нажатии на пункт http://0.0.0.0:8000/api/get_weather_set/ (или при get запросе по этом адресу) будет возвращен json-объект со всеми погодными данными, хранящимися в таблице.

# ОПИСАНИЕ АРХИТЕКТУРЫ
**test_for_proeshelon/manage.py** - основной скрипт всего приложения

**test_for_proeshelon/test_for_proeshelon** - пакет проекта, здесь находятся конфиги и главная URL-конфигурация, которая может передавать управления URL-конфигурациям приложений, которые, в свою очередь, вызовут нужные отображения.

**test_for_proeshelon/weather_app** - пакет приложения, реализующего основной бизнес-процесс: получение погодных данных с помощью апи сторонних сайтов.

**test_for_proeshelon/api/api_weather_app** - пакет приложения апи, в котором реализуется получение данных о погоде из бд приложения без предоставления прямого доступа к бд.

**test_for_proeshelon/local_properties** - здесть содержатся локальные конфиги(например, ключи), которые не должны стать публичными.
