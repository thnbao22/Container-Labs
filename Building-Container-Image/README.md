# Introduction

In this part, you use a Dockerfile to build a container image onto the instance. This sample uses an image that includes the Nginx webserver to serve a simple html page.

1. Let's start by creating a working directory for our container image. Make a directory and named it `container-image`  then navigate to it.

![ConnectPrivate](/images/2.Building-a-Container-Image/1.ContainerImage.png)

2. Use `touch Dockerfile` to create a Dockerfile

```
touch Dockerfile
```

![ConnectPrivate](/images/2.Building-a-Container-Image/2.ContainerImage.png)

3. Run the below command to update the Dockerfile content.

```
cat <<EOF > Dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html
EOF
```

- `FROM nginx:latest`: this command specifies the base image that Docker will use to build the new container.

- `COPY index.html /usr/share/nginx/html`: This command copies the index.html file from the current directory on the host machine into the /usr/share/nginx/html directory in the container.

![ConnectPrivate](/images/2.Building-a-Container-Image/3.ContainerImage.png)

4. Run `touch index.html` to create a blank HTML file which will contain a simple message. Use the `echo` command line tool to pipe a simple message in to our index.html file.

```
touch index.html
echo "Hello, my name is Charles Thien and this is my first Dockerfile" > index.html
```

![ConnectPrivate](/images/2.Building-a-Container-Image/4.ContainerImage.png)

5. Use `docker build -t nginx:1.0 .` to build the nginx container image from our Dockerfile.
- The `docker build` command builds Docker images from a Dockerfile and a "context".

```
docker build -t nginx:1.0 .
```

- `docker build -t` in Docker is used to build a Docker image from the instruction in the `Dockerfile`
  
- `-t` is used to assign a tag to the Docker image you just create from the Dockerfile
  
- The dot `.` represents the build context. When you run `docker build -t nginx:1.0 .`, the dot indicates that the `current directory` (where your Dockerfile is located) serves as the build context.

![ConnectPrivate](/images/2.Building-a-Container-Image/5.ContainerImage.png)

![ConnectPrivate](/images/2.Building-a-Container-Image/6.ContainerImage.png)

6. You can now use `docker history nginx:1.0` to see all the steps and base containers that our `nginx:1.0` is built on.
- The `docker history` command shows the history of an image

```
docker history nginx:1.0
```

![ConnectPrivate](/images/2.Building-a-Container-Image/7.ContainerImage.png)

![ConnectPrivate](/images/2.Building-a-Container-Image/8.ContainerImage.png)

7. Type `docker run -p 8080:80 --name nginx nginx:1.0` to run our new container.
- Note that we didn't specify the `-d` to make it a `daemon` which means it holds control of our terminal and outputs the containers logs to there which can be handy in debugging.

```
docker run -p 8080:80 --name nginx nginx:1.0
```

The command `docker run -p 8080:80 --name nginx nginx:1.0` has the following components:
- `docker run`: Is the basic command of Docker, used to run a container from a Docker image.
  
- `-p 8080:80`: This command maps port 8080 of the host (the machine you are running Docker on) to port 80 of the Docker container. This means that if you visit localhost:8080 on your server's web browser, you will be redirected to the application running on port 80 of the Docker container.
  
- `--name nginx`: This command names the Docker container nginx. This helps you easily manage and manipulate containers.
  
- `nginx:1.0`: This command names the Docker container nginx. This helps you easily manage and manipulate containers.

So, the command `docker run -p 8080:80 --name nginx nginx:1.0` will run a Docker container from Docker image `nginx:1.0`, name the container `nginx` and map the host's port 8080 to port 80 of Docker containers.

![ConnectPrivate](/images/2.Building-a-Container-Image/9.ContainerImage.png)

8. Open another terminal and type the following command.

```
curl http://localhost:8080
```

![ConnectPrivate](/images/2.Building-a-Container-Image/10.ContainerImage.png)

9. Go back to the first tab and see the log lines sent right out to STDOUT.

![ConnectPrivate](/images/2.Building-a-Container-Image/11.ContainerImage.png)

10. Type `Ctrl-C` to exit the log output. Note that the container has been stopped but is still there by running a `docker ps -a`.

![ConnectPrivate](/images/2.Building-a-Container-Image/12.ContainerImage.png)

```
docker ps -a
```

![ConnectPrivate](/images/2.Building-a-Container-Image/13.ContainerImage.png)

11. Use `docker inspect nginx` to see lots of info about our stopped container.
- The `docker inspect` finds details on a container

```
docker inspect nginx
```

12. Now, use `docker rm nginx` to delete the container.

```
docker rm nginx
```
![ConnectPrivate](/images/2.Building-a-Container-Image/14.ContainerImage.png)

13. For our last magic trick, we're going to try mounting some files from the host into the container rather than embedding them in the image.

```
docker run -d -p 8080:80 -v /home/charles/container-image/index.html:usr/share/nginx/html/index.html\:ro --name nginx nginx:latest
```

![ConnectPrivate](/images/2.Building-a-Container-Image/15.ContainerImage.png)

14. Now try a `curl http://localhost:8080`. Note that even though this is the upstream nginx image from Docker Hub our content is there.

```
curl http://localhost:8080
```

![ConnectPrivate](/images/2.Building-a-Container-Image/16.ContainerImage.png)

15. Edit the index.html file and add some more things.

```
echo "Docker" >> index.html
```

![ConnectPrivate](/images/2.Building-a-Container-Image/17.ContainerImage.png)

16. Try another `curl http://localhost:8080` and note the immediate changes.

```
curl http://localhost:8080
```

![ConnectPrivate](/images/2.Building-a-Container-Image/18.ContainerImage.png)

17. Finally, run `docker stop nginx and docker rm nginx` to stop and remove our last container.

```
docker stop nginx && docker rm nginx
```

![ConnectPrivate](/images/2.Building-a-Container-Image/19.ContainerImage.png)

18. You can check if the container has stopped running by using `docker ps -a`. 

```
docker ps -a
```

![ConnectPrivate](/images/2.Building-a-Container-Image/20.ContainerImage.png)