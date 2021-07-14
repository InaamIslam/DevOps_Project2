from flask import Flask, Response, request
import random
from application import app


@app.route('/price', methods=['GET', 'POST'])

def price(): 

        data_sent = request.data.decode('utf-8')
        data = data_sent.split(" ")
        activity = data[0]
        city = data[1]

        if city == "London":
                if activity == 'Paintballing':
                        price = '£200 - £400'
                elif activity == 'Surfing':
                        price = '£400 - £800'
                elif activity == 'Scuba Diving':
                        price = '£800 - £1000'
                elif activity == 'Scuba Diving':
                        price = '£1000 - £2000'
        elif city == "Barcelona":
                if activity == 'Paintballing':
                        price = '£200 - £400'
                elif activity == 'Surfing':
                        price = '£400 - £800'
                elif activity == 'Scuba Diving':
                        price = '£800 - £1000'
                elif activity == 'Scuba Diving':
                        price = '£1000 - £2000'
        elif city == "Milan":
                if activity == 'Paintballing':
                        price = '£200 - £400'
                elif activity == 'Surfing':
                        price = '£400 - £800'
                elif activity == 'Scuba Diving':
                        price = '£800 - £1000'
                elif activity == 'Scuba Diving':
                        price = '£1000 - £2000'
        elif city == "Tokyo":
                if activity == 'Paintballing':
                        price = '£200 - £400'
                elif activity == 'Surfing':
                        price = '£400 - £800'
                elif activity == 'Scuba Diving':
                        price = '£800 - £1000'
                elif activity == 'Scuba Diving':
                        price = '£1000 - £2000'
                
        else:
                return "Random Holiday could not be generated" 

        return Response(price, mimetype="text/plain")





  