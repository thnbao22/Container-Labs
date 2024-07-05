# Dockerfile Best Practices

In this section, we will cover other recommended **best practices** for writing Dockerfiles.

## Using an approriate parent image
Using the appropriate base image is one of the `key recommendations` when building **efficient** Docker images.

For example, if you need the `JDK` (Java Development Kit) for your application , you can use the **openjdk** official Docker image instead of using the generic ubuntu image and installing the JDK on top of the ubuntu image:

| Inefficient Dockerfile                | Efficient Dockerfile |
| -------------------------------------:| --------------------:|
| FROM ubuntu                           | FROM openjdk         |
| RUN apt-get update && \               |                      |
|     apt-get install -y openjdk-8-jdk  |                      |

Avoid using the `latest` tag for the parent image when building Docker images for `production environments`. 
- The `latest` tag might get pointed to a newer version of the image as the new versions are released to the Docker Hub, and the newer version might not be ``backward compatible`` with your applications, leading to **failures** in your production environments. My suggestion is always use a specific versioned tag as the parent image:

| Inefficient Dockerfile                | Efficient Dockerfile |
| -------------------------------------:| --------------------:|
| FROM nginx:latest                     | FROM nginx:1.27      | 

Finally, using the `minimal version` of the parent image is **critical** to getting a minimal-sized Docker image.

| Inefficient Dockerfile                | Efficient Dockerfile |
| -------------------------------------:| --------------------:|
| FROM nginx:1.27                       | FROM nginx:1.27-perl | 

## Using a Non-Root user for better security
By default, Docker containers run with the root (**id = 0**) user. 

Running containers as a `non-root` user is a `recommended best practice` to **improve the security** of the Docker container.
- This will adhere to the principle of least privilege, which ensures that the application has only the bare minimum privileges to perform its tasks.

There are `two methods` that we can use to run a container as a `non-root`
user: with the `--user` (or -u) flag, and with the `USER` directive.

Example of using the --user flag with docker run command:

```
docker run --user = 9999 ubuntu:focal
```

Additionally, we can use the USER directive within the Dockerfile to define the
default user.
- However, this value can be overridden with the `--user` flag while starting the Docker container:
  
```
FROM ubuntu:focal
RUN apt-get update
RUN useradd charles-platform
USER charles-platform
CMD whoami
```

## Using DOCKERIGNORE
The `.dockerignore` file is a special text file within the Docker context that is used to specify a list of files to be `excluded` from the Docker context while building the Docker image.

Each time we build the Docker image, the build context will be sent to the Docker daemon. As this will take time and bandwidth during the Docker image build process, it is recommended to exclude all the files that are not needed in the final Docker image. The .dockerignore file can be used to achieve this purpose. In addition to saving time and bandwidth, the .dockerignore file is used to exclude the confidential files, such as `password` files and `key` files from the build context.

The .dockerignore file should be created in the `root` directory of the build
context.

Sample of .dockerignore file:

```
password.txt
!README.md
```

## Minimizing Layers
Each line in the Dockerfile will create a new layer that will take up space in
the Docker image.
- So, it is recommended to create as few layers as possible when building the Docker image.

To achieve this, combine the RUN directives whenever possible

As an example, consider the following Dockerfile, which will update the package
repository first and then install the redis-server and nginx packages:

```
FROM ubuntu:focal
RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y redis-server
```

This Dockerfile can be optimized by combining the three RUN directives:

```
FROM ubuntu:focal
RUN apt-get update \
    && apt-get install -y nginx redis-server
```

## Don't install unnecessary tools
Not installing unnecessary debugging tools (such as vim, curl, and telnet) and
removing unnecessary dependencies can help to create efficient Docker images that are small in size.