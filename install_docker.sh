#!bin/bash

# Update system packages
sudo apt update

# Upgrade system packages
sudo apt upgrade

#  Install required dependencies for Docker
sudo apt install lsb-release ca-certificates apt-transport-https software-properties-common -y

# import the Docker GPG key required for connecting to the Docker repository
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# adding the Docker repository to your Ubuntu 20.04
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update system packages
sudo apt update

# Install Docker
sudo apt install docker-ce

# Verify Docker Status
sudo systemctl status docker