#!/bin/bash

ssh root@142.93.116.229 <<EOF
  apt-get update -y
  git pull
  cd project1
  source /opt/envs/project1/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
  #./manage.py migrate
  sudo service apache2 restart 
  exit
EOF
