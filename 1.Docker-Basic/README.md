# Introduction

In this part, you check if Docker is installed on the Ubuntu Linux, and download and run a standard container image of the popular web server **Nginx**.

1. Let's start by running docker --version to confirm that both the client and server are there and working.

```
Docker --version
```


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

4. Now let's try `docker run -d -p 8080:80 --name nginx nginx:latest` to instantiate the nginx image as a background daemon with port 8080 on the host forwarding through to port 80 within the container.

```
docker run -d -p 8080:80 --name nginx nginx:latest
```

Specify some flags in the Docker command:
   - `-d`: Means **detached** mode,  we want to instantiate the nginx image as a **background daemon**.
   - `--name`: The **--name** flag is used to specify the name of the container. This means that the command `docker run --name nginx` will create and run a new container from the nginx image, and the name of this container will be nginx.
   - `-p`: to map port 8080 with port 80 within the container.

![ConnectPrivate](/images/1.Docker-Basic/3.DockerBasic.png)

5. Now, let's run `docker ps` to see that our container is running.
- `docker ps` is a command to list containers. 

```
docker ps
``` 

![ConnectPrivate](/images/1.Docker-Basic/4.DockerBasic.png)

6. Try `curl http://localhost:8008` to use the the nginx container and verify it is working with its default `index.html`.
- `curl` is a command line tool that enables data exchange between a device and a server through a terminal.

```
curl http://localhost:8080
```

![ConnectPrivate](/images/1.Docker-Basic/5.DockerBasic.png)

7. Running `docker logs nginx` shows us the logs produced by nginx and the container.
- `docker logs` command batch-retrieves logs present at the time of execution.

![ConnectPrivate](/images/1.Docker-Basic/6.DockerBasic.png)

8. Use `docker exec -it nginx /bin/bash` to start an interactive shell into the container's filesystem and constraints.
- The `docker exec` command runs a new command in a running container.

![ConnectPrivate](/images/1.Docker-Basic/7.DockerBasic.png)

9. From within the container, run `cd /usr/share/nginx/html` and `cat index.html` to see the content the nginx is serving which is part of the container.

```
cd /usr/share/nginx/html
cat index.html
```

![ConnectPrivate](/images/1.Docker-Basic/8.DockerBasic.png)

10. Type `exit` to exit our shell within the container.

```
exit   
```

![ConnectPrivate](/images/1.Docker-Basic/9.DockerBasic.png)

11. Run `docker stop nginx` to stop the container. Before you can remove a container, you must stop the container first.
- The `docker stop` command is used to stop a running container. 

```
docker stop nginx
```

![ConnectPrivate](/images/1.Docker-Basic/10.DockerBasic.png)


12. Run `docker ps -a` command and you should see that our container is still there but stopped.
- The `docker ps -a` command is used to see all containers running or not.

```
docker ps -a
```

![ConnectPrivate](/images/1.Docker-Basic/13.DockerBasic.png)  


13. Run `docker rm nginx` to completely remove the container once and for all.
- The `docker rm` command is used to remove one or more containers. 

```
docker rm nginx
```

![ConnectPrivate](/images/1.Docker-Basic/11.DockerBasic.png)

14. Now, you can use `docker rmi nginx:latest` to remove the nginx image from our machine's local cache. You must ensure that no containers are running off of that image before attempting to remove the image.
- The `docker rmi` command is used to remove the image.

```
docker rmi nginx:latest
```

![ConnectPrivate](/images/1.Docker-Basic/12.DockerBasic.png)