#! /bin/bash
docker --version
curl https://get.docker.com | sudo bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
docker-compose down --rmi all
docker-compose build
docker-compose push 