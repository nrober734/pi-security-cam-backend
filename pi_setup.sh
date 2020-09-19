#!/bin/bash

#--------------
#Intialize
#--------------
sudo apt-get -y update
sudo apt-get -y upgrade

#--------------
#Install conda
#--------------
curl "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-armv7l.sh" -o "Miniconda.sh"
bash ./Miniconda.sh
echo "yes yes" | ./Miniconda.sh

#--------------
#Install docker
#--------------
sudo apt-get -y install apt-transport-https ca-certificates software-properties-common -y
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker pi
echo 'deb https://download.docker.com/linux/raspbian/ stretch stable' | sudo tee -a /etc/apt/sources.list
sudo apt-get -y update
sudo apt-get -y upgrade
systemctcl start docker.service

#--------------
#Reboot to apply all changes
#--------------
reboot
