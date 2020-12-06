#! /bin/bash

git clone https://github.com/Alex-Bane/wk9project.git
echo $PATH
cd ./wk9project
sudo /home/jenkins/.local/bin/ansible-playbook -i ansible/inventory ansible/playbook.yaml
