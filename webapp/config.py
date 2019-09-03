import os

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = "Tula,Russia"
WEATHER_API_KEY = "4471fd4436984d4e82a114400192308"
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, '..', 'webapp.db')




