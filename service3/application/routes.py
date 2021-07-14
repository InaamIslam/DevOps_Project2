from flask import Flask, render_template, Response
import random 
from application import app

@app.route('/activity', methods=['GET'])
def activity():

  activities = ["Paintballing", "Surfing", "Scuba Diving", "Skiing"]
  activity = random.choice(activities)

  return Response(activity, mimetype="text/plain")

  