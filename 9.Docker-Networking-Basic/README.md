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

### Use user-defined bridge networks

In this example, we again start two alpine containers, but attach them to a `user-defined network` called `alpine-net` which we have already created. These containers are not connected to the default bridge network at all. We then start a third alpine container which is `connected to the bridge network` but `not connected to alpine-net`, and a `fourth` alpine container which is `connected to both networks`.

1. Create the `alpine-net` network.

```
docker network create -d bridge alpine-net
```

![alt text](../images/9.Docker-Networking-Basic/13.Defined.png)

2. List Docker's networks using the following commad:

```
docker network ls
```

![alt text](../images/9.Docker-Networking-Basic/14.Defined.png)

3. Inspect the alpine-net network:

```
docker inspect alpine-net
```

![alt text](../images/9.Docker-Networking-Basic/15.Defined.png)

Notice that this network's gateway is `172.18.0.1`, as opposed to the default bridge network, whose gateway is `172.17.0.1`.

4. Create your four containers. Notice the --network flags.

```
docker run -dit --name alpine1 --network alpine-net alpine ash

docker run -dit --name alpine2 --network alpine-net alpine ash

docker run -dit --name alpine3 alpine ash

docker run -dit --name alpine4 --network alpine-net alpine ash

docker network connect bridge alpine4
```

![alt text](../images/9.Docker-Networking-Basic/16.Defined.png)

![alt text](../images/9.Docker-Networking-Basic/17.Defined.png)

![alt text](../images/9.Docker-Networking-Basic/18.Defined.png)

![alt text](../images/9.Docker-Networking-Basic/19.Defined.png)

![alt text](../images/9.Docker-Networking-Basic/20.Defined.png)

5. Verify that all containers are running:

```
docker ps 
```

![alt text](../images/9.Docker-Networking-Basic/21.Defined.png)

6. Inspect the `bridge` network and the `alpine-net` network again:

```
docker inspect bridge
```

```
docker inspect alpine-net
```

![alt text](../images/9.Docker-Networking-Basic/22.Defined.png)

![alt text](../images/9.Docker-Networking-Basic/23.Defined.png)

Containers `alpine3` and `alpine4` are connected to the `bridge` network.

![alt text](../images/9.Docker-Networking-Basic/24.Defined.png)

![alt text](../images/9.Docker-Networking-Basic/25.Defined.png)

Containers `alpine1`, `alpine2` and `alpine4` are connected to the `alpine-net` network.

7. Use the `docker attach` command to connect to `alpine1`.

```
docker attach alpine1
```

![alt text](../images/9.Docker-Networking-Basic/26.Defined.png)

8. Ping to the container named `alpine2`, `alpine4` and `alpine3`.

```
ping -c 2 alpine2
```

![alt text](../images/9.Docker-Networking-Basic/27.Defined.png)

![alt text](../images/9.Docker-Networking-Basic/28.Defined.png)

From alpine1, you should not be able to connect to alpine3 at all, since it is not on the `alpine-net` network.

![alt text](../images/9.Docker-Networking-Basic/29.Defined.png)

9. Ping to alpine3 by its IP address.

```
ping -c 2 172.17.0.2
```

![alt text](../images/9.Docker-Networking-Basic/30.Defined.png)

However, you will need to address `alpine3` by its IP address.

10. Use the `docker attach` command to connect to `alpine4`.

```
docker attach alpine4
```

![alt text](../images/9.Docker-Networking-Basic/31.Defined.png)

11. Perform ping to other container.

![alt text](../images/9.Docker-Networking-Basic/32.Defined.png)

12.  Type `Ctrl + pq` to exit the shell.

![alt text](../images/9.Docker-Networking-Basic/33.Defined.png)

13. Follow the following steps to remove the containers and images.

![alt text](../images/9.Docker-Networking-Basic/34.Defined.png)

![alt text](../images/9.Docker-Networking-Basic/35.Defined.png)