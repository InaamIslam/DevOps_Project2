from flask import Flask, render_template
import random 
from application import app

@app.route('/', methods=['GET'])
def activity():

  activities = ["Paintballing", "Surfing", "Scuba Diving", "Skiing"]
  activity = random.choice(activities)

  return Response(activity, mimetype="text/plain")

  