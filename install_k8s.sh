#!/bin/bash

# Using for Ubuntu Linux x86_64

# Download the latest release
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
# Download the kubectl checksum file
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
# Validate the kubectl binary against the checksum file
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
# Install kubectl
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
