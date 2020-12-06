#! /bin/bash


cd ./wk9project

~./.local/bin/ansible-playbook -i ansible/inventory ansible/playbook.yaml
