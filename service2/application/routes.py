from flask import Flask, render_template
import random 


@app.route('/', methods=['GET'])
def city():

  cities = ["London", "Barcelona", "Milan", "Tokyo"]
  city = cities[random.choice]

  return city 