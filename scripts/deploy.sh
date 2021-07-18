#! /bin/bash
ssh -i ~/.ssh/ansible_id_rsa jenkins@ansible << EOF
docker-compose up -d

# sudo docker node ls
# git clone 
# cd W9_-SoloProject
# docker login
# sudo docker pull (pull service images)
# sudo docker stack deploy -c docker-compose.yaml 
# EOF



