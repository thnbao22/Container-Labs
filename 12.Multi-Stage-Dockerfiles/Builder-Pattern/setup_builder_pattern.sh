#!/bin/bash

# Build the builder Docker image using the Dockerfile nmaed Dockerfile.build
docker build -t hellogo-build -f Dockerfile.build .

# docker container create or docker create
# Create a container from the build Docker image
docker create --name hellogo-build-container hellogo-build

# Copy build artifacts from the container to the local filesystem
docker cp hellogo-build-container:/myapp/hellogo .

# Build the runtime Docker image using the Dockerfile named Dockerfile.runtime
docker build -t hellogo -f Dockerfile.runtime . 

# Remove the builder Docker container
docker rm -f hellogo-build-container

# Remove the copied artifacts
rm hellogo