#! /bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@jenkins:/home/docker-compose.yaml

ssh -i ~/.ssh/id_rsa jenkins@jenkins
<< EOF
    export DATABASE_URI=${DATABASE_URI}
    export SECRET_KEY=${SECRET_KEY}
    docker stack deploy --compose-file docker-compose.yaml encounters
EOF



