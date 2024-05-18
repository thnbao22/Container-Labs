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
