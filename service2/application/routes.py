from flask import Flask, render_template
import random 
from application import app

@app.route('/', methods=['GET'])
def city():

  cities = ["London", "Barcelona", "Milan", "Tokyo"]
  city = random.choice(cities)
  return Response(city, mimetype="text/plain")


