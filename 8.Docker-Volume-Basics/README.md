# Introduction

In this lab, you will learn how to create a volume. You should than run a simple an thin container and attach a volume to it. Use the image selaworkshops/busybox:latest and use any name to the mounted volume directory. 

## Explain about the volume types

There are `two types` of volume.

Every volume is a mount point on the container directory tree to a location on the host directory tree, but the types differ in where that location is on the host.

- The first type of volume is a `bind mount`. Bind mount volumes use any `user-specified directory` or `file` on the `host OS`.

- The second type is a `managed volume`. Managed volumes use `locations that are created by the Docker daemon` in space controlled by the daemon, called `Docker managed space`.

![alt text](../images/8.Docker-Volume-Basics/Volume_types.png)

### Docker managed volumes
Managed volumes are different from bind mount volumes because the Docker daemon creates managed volumes in a portion of the host’s file system that’s owned by Docker. 

Managed volumes are created when you use the `-v` option (or `--volume`) on docker run but `only specify the mount point in the container directory tree`.

1. Create a new volume and call it `my-volume`.

```
docker volume create my-volume
```

![alt text](../images/8.Docker-Volume-Basics/1.Volumes.png)

2. Inspect the new volume to find the `mountpoint`.

```
docker inspect my-volume
```

![alt text](../images/8.Docker-Volume-Basics/2.Volumes.png)

3. Let’s run a container and mount the created volume to the root.

```
docker run -it -v my-volume:/data --name my-devops-container selaworkshops/busybox:latest
```

![alt text](../images/8.Docker-Volume-Basics/3.Volumes.png)

4. In the terminal of the container, create a new file under /data.

```
cd /data/
echo "Devops" > hi.txt
ls
``` 

![alt text](../images/8.Docker-Volume-Basics/4.Volumes.png)

5. Open other terminal instance and run other container with the same volume.

```
docker run -it -v my-volume:/data --name my-devops-container-2 selaworkshops/busybox:latest
```

![alt text](../images/8.Docker-Volume-Basics/5.Volumes.png)

6. In the terminal of the my-devops-container-2 container, type the following command.

```
cd data/ && ls
```

![alt text](../images/8.Docker-Volume-Basics/6.Volumes.png)

7. Exit from both containers and delete them. Use the following command to force remove the container.

![alt text](../images/8.Docker-Volume-Basics/7.Volumes.png)

![alt text](../images/8.Docker-Volume-Basics/8.Volumes.png)

```
docker rm -f my-devops-container my-devops-container-2
```

![alt text](../images/8.Docker-Volume-Basics/9.Volumes.png)

8. Ensure the containers were deleted.

```
docker ps -a
```

![alt text](../images/8.Docker-Volume-Basics/10.Volumes.png)

9. Delete the image.

![alt text](../images/8.Docker-Volume-Basics/11.Volumes.png)

### Bind mount volumes

Bind mount volumes are useful when the host provides some file or directory that needs to be mounted into the container directory tree at a specific point.

Note: Volume được gắn vào theo kiểu `bind mount` sẽ tạo mới đường dẫn được gắn hoặc nếu có đường dẫn rồi thì `ghi đè toàn bộ dữ liệu`.

1. Make a directory and name it `devops-docs`.

```
mkdir devops-docs
```

![alt text](../images/8.Docker-Volume-Basics/12.Managed.png)

2. Type the following command to start an Apache HTTP server where your new directory (devops-docs) is bind mounted to the server's document root.

```
docker run -d --name devopsweb -v ~/devops-docs:/usr/local/apache2/htdocs -p 80:80 httpd:latest
```

Here’s what each part of the command does:
- `-d`: Run a `detached mode` container.

- `--name`: we specify the name of the container is `devopsweb`.   

- -v ~/devops-docs:/usr/local/apache2/htdocs: This option mounts the local directory ~/devops-docs (on your host machine) to the directory /usr/local/apache2/htdocs inside the Docker container. Any changes made in the local directory will be reflected inside the container, and vice versa.


![alt text](../images/8.Docker-Volume-Basics/13.Managed.png)


# Conclusion
Bind mount volumes are **useful** if you want to `share data` with other processes running
outside a container, such as components of the host system itself.
