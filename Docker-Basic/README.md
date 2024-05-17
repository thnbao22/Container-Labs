# Introduction

In this part, you check if Docker is installed on the Ubuntu Linux, and download and run a standard container image of the popular web server **Nginx**.

1. Let's start by running docker --version to confirm that both the client and server are there and working.

```
Docker --version
```

![ConnectPrivate](/images/1.Docker-Basic/1.DockerBasic.png)

2. Docker containers are built using images. Let's run the command `docker pull nginx:latest` to pull down the latest nginx trusted image from Docker Hub.

```
docker pull nginx:latest
```

![ConnectPrivate](/images/1.Docker-Basic/1.DockerBasic.png)

3. Now run `docker images` to verify that the image is now on your local machine's Docker cache. If we start it then it won't have to pull it down from Docker Hub first.

```
docker images
```

![ConnectPrivate](/images/1.Docker-Basic/2.DockerBasic.png)