from flask import Flask, Response, request
import random
from application import app


@app.route('/price', methods=['GET', 'POST'])

def price(): 

        price_network = request.data.decode('utf-8')
        data = price_network.split(" ")
        activity = data[1]
        city = data[0]

        if city == "London":
                if activity == 'Paintballing':
                        price = '200'
                elif activity == 'Surfing':
                        price = '400'
                elif activity == 'Snorkelling':
                        price = '600'
                elif activity == 'Skiing':
                        price = '800'
        elif city == "Barcelona":
                if activity == 'Paintballing':
                        price = '200'
                elif activity == 'Surfing':
                        price = '400'
                elif activity == 'Snorkelling':
                        price = '600'
                elif activity == 'Skiing':
                        price = '800'
        elif city == "Milan":
                if activity == 'Paintballing':
                        price = '200'
                elif activity == 'Surfing':
                        price = '400'
                elif activity == 'Snorkelling':
                        price = '600'
                elif activity == 'Skiing':
                        price = '800'
        elif city == "Tokyo":
                if activity == 'Paintballing':
                        price = '200'
                elif activity == 'Surfing':
                        price = '400'
                elif activity == 'Snorkelling':
                        price = '600'
                elif activity == 'Skiing':
                        price = '800'
        
        return Response(price, mimetype="text/plain")





  