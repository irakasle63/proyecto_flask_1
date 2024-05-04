from flask import Flask, request
from flask_cors import CORS
from .weather import *

app = Flask(__name__)
cors = CORS(app)


@app.route("/cities/<city_id>", methods=["GET"])
def get_city(city_id):
    return get_weather_by(city_id)


@app.route("/cities/<city_id>", methods=["DELETE"])
def delete_city(city_id):
    print("*****DELETE")
    delete_weather_by(city_id)
    return ""


@app.route("/cities/", methods=["GET"])
def all_cities():
    return list_weather_all()


@app.route("/cities/", methods=["POST"])
def new_city():
    data = request.get_json()
    print("****new_city", data)
    add_city(data)
    return ""


@app.route("/", methods=["GET"])
def hello_world():
    return "Hola coders"
