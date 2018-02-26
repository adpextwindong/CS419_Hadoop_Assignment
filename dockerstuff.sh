#!/bin/sh

docker pull cloudera/quickstart:latest

docker run --hostname=quickstart.cloudera --privileged=true -t -i -p 8888:8888 -p 80:80 -p 443:443 cloudera/quickstart /usr/bin/docker-quickstart
