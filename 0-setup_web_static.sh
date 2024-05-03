#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static.
sudo apt -y update
sudo apt -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "Hello from the test web page" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '/server_name _;/a \
\
    location /hbnb_static/ {\
    	alias /data/web_static/current/;\
    }' /etc/nginx/sites-available/default
sudo service nginx start
