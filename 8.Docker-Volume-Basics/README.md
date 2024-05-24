# Introduction

In this lab, you will learn how to create a volume. You should than run a simple an thin container and attach a volume to it. Use the image selaworkshops/busybox:latest and use any name to the mounted volume directory. 

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