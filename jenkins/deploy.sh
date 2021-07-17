#! /bin/bash

ssh -i ~/.ssh/ansible_id_rsa jenkins@manager << EOF
sudo docker node ls
git clone https://github.com/InaamIslam/DevOps_Project2.git
cd 
docker login

#need to pull the services to deploy
sudo docker pull service1
sudo docker stack deploy -c docker-compose.yaml 
EOF
