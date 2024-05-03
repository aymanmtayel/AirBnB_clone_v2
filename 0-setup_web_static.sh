#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static.
sudo apt -y update
sudo apt -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo echo "Hello from the test web page" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/server_name _;/a \
\
    location /hbnb_static/ {\
    	alias /data/web_static/current/;\
    }' /etc/nginx/sites-available/default
sudo service nginx restart
