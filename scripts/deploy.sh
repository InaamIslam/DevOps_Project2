#! /bin/bash
ssh -i ~/.ssh/ansible_id_rsa jenkins@ansible << EOF
sudo docker node ls
git clone https://github.com/InaamIslam/DevOps_Project2.git
cd DevOps_Project2
docker login 
sudo docker pull inaamiii/random_holiday_service1
sudo docker pull inaamiii/service_2_api
sudo docker pull inaamiii/service_3_api
sudo docker pull inaamiii/service_4_api
sudo docker stack deploy -c docker-compose.yaml 
EOF



