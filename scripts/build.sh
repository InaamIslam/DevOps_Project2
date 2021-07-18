#! /bin/bash
docker --version
docker-compose down --rmi all
docker-compose build
docker-compose push 