#!/bin/bash

# build server

docker build -t service_1_server service1

# build api's

docker build -t service_2_api service2
docker build -t service_3_api service3
docker build -t service_4_api service4

# create networks 

docker network create service_1_network 

# Run containers 

docker run -d -p 5000:5000 --name service_2_api --network service_1_network service_1_server

docker run -d -p 5000:5000 --name service_3_api --network service_1_network service_1_server

docker run -d -p 5000:5000 --name service_4_api --network service_1_network service_1_server



