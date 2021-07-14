from flask import Flask, render_template, Response
import random 
from application import app

@app.route('/city', methods=['GET'])
def city():

  cities = ["London", "Barcelona", "Milan", "Tokyo"]
  city = random.choice(cities)
  return Response(city, mimetype="text/plain")


