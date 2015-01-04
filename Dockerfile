############################################################
# Dockerfile to build SRCTweb flask application 
# Based on Ubuntu
############################################################

# Instructions:
#
# Build: sudo docker build -t srctweb .
# Run: sudo docker run -p 8000:80 -i -t -d srctweb
# 
# You'll need to reverse proxy port 8000 via nginx

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Student-Run Computing and Technology - GMU

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip

# Install prereqs for ldap
RUN apt-get install -y libldap2-dev libsasl2-dev

# Clone down SRCT-Web
RUN git clone https://github.com/srct/srctweb.git srctweb

# Get pip to download and install requirements:
RUN pip install -r /srctweb/requirements.txt

# Expose ports
EXPOSE 80

# Set the default directory where CMD will execute
WORKDIR /srctweb/srctweb

# Use Gunicorn to serve the application
CMD gunicorn srctweb:website -b 0.0.0.0:80
