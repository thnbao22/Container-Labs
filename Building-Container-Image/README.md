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