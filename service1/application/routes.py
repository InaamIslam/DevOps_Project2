from flask import Flask, render_template, request
import requests
from application import app, db


@app.route('/', methods=['GET','POST'])
def index():
    #get the name of the city 
    city = requests.get("http://service2:5001/city")
    #get the activty 
    activity = requests.get("http://service3:5002/activity")

    price_network = str(city.text) + " " + str(activity.text) 
   
    price = request.post("http://service4:5003/price", data=price_network)
    
   
    return render_template('index.html', title='Holiday Generator', city = city.text, 
  activity=activity.text, price = price.text, price_network=price_network)



   
