#! /bin/bash

ssh swarm-manager << EOF
sudo docker pull alexbane/service1:latest
sudo docker pull alexbane/service2:latest
sudo docker pull alexbane/service3:latest
sudo docker pull alexbane/service4:latest
git clone https://github.com/Alex-Bane/wk9project.git
cd /wk9project
sudo docker stack deploy --compose-file docker-compose.yaml DNDApp
EOF
