from flask import Flask, render_template
import random 


@app.route('/', methods=['GET'])
def activity():

  activities = ["Paintballing", "Surfing", "Scuba Diving", "Skiing"]
  activity = activities[random.choice]

  return activity  

  