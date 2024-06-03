# Overview

## Bridge network
In terms of Docker, a bridge network uses a software bridge which lets containers connected to the same bridge network communicate, while providing isolation from containers that aren't connected to that bridge network. The Docker bridge driver automatically installs rules in the host machine so that containers on different bridge networks can't communicate directly with each other.

Bridge networks apply to containers running on the `same Docker daemon host`.

### Use the default bridge network

In this part, you will learn how to use the `default bridge` network that Docker sets up for you automatically. This network is `not the best choice` for production systems.

1. Open the terminal, type the following command to list the current networks:

```
docker network ls
```

![alt text](../images/9.Docker-Networking-Basic/1.Default.png)

2. Run the following command to run two alpine containers running `ash`, which is Alpine's default shell rather than `bash`.

```
docker run -dit --name alpine1 alpine ash

docker run -dit --name alpine2 alpine ash
```

The `-dit` flag means to run the container on detached mode (in the background), interactive and with a TTY (so you can see the input and output).

![alt text](../images/9.Docker-Networking-Basic/2.Default.png)

![alt text](../images/9.Docker-Networking-Basic/3.Default.png)

3. Check that both containers are actually started by using the following command:

```
docker ps -a
```

![alt text](../images/9.Docker-Networking-Basic/4.Default.png)

4. Use the following command to inspect the `bridge` network:

```
docker inspect bridge
```

![alt text](../images/9.Docker-Networking-Basic/5.Default.png)

Under the `Containers` key, each connected container is listed, along with information about its IP address (172.17.0.2 for alpine1 and 172.17.0.3 for alpine2).

5. The containers are running in the background. Use the `docker attach` command to connect to `alpine1`.

```
docker attach alpine1
```

![alt text](../images/9.Docker-Networking-Basic/6.Default.png)

The prompt changes to `#` to indicate that you are the `root user` within the container. 

6. Use the `ip addr show` command to show the network interfaces for alpine1 as they look from within the container: 

```
ip addr show
```

![alt text](../images/9.Docker-Networking-Basic/7.Default.png)

7. From within `alpine1`, make sure you can connect to the internet by pinging `aws.amazon.com`.

```
ping -c 2 aws.amazon.com
```

![alt text](../images/9.Docker-Networking-Basic/8.Default.png)

8. Now try to ping the `second container`. First, ping it by its IP address, `172.17.0.3`:

```
ping -c 2 172.17.0.3
```

![alt text](../images/9.Docker-Networking-Basic/9.Default.png)

9. This succeeds. Next, try pinging the `alpine2` container by container name. This will fail.

```
ping -c 2 alpine2
```

![alt text](../images/9.Docker-Networking-Basic/10.Default.png)

10.  Detach from alpine1 without stopping it by using the detach sequence, hold down CTRL and type p followed by q.

11. Follow these steps to remove the containers and images.

![alt text](../images/9.Docker-Networking-Basic/11.Default.png)

![alt text](../images/9.Docker-Networking-Basic/12.Default.png)