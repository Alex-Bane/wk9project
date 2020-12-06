#! /bin/bash


cd ./wk9project

sudo ~./.local/bin/ansible-playbook -i ansible/inventory ansible/playbook.yaml
