#from .weather_repository_sqlite import *
from .weather_repository import *

def add_city(weather):
    # weather = {"id": "MAD", "name": "Madrid", "temperature": 37}
    #rain_probability = 0.7
    #weather["rain_probability"] = rain_probability
    create(weather)


def get_weather_by(id):
    return read(id)


def list_weather_all():
    return read_all()


def delete_weather_by(id):
    delete(id)
