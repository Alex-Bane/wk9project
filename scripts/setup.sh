#! /bin/bash


pwd
cd ./wk9project
pwd
sudo /home/jenkins/.local/bin/ansible-playbook -i ansible/inventory ansible/playbook.yaml
