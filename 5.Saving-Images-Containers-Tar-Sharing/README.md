# Introduction

Imagine a scenario where you have built Docker images and containers that you would be interested to keep and share it with your other collaborators or colleagues. The below methods shall help you achieve it.

Four basic Docker CLI comes into action:
- The [docker export](https://docs.docker.com/reference/cli/docker/container/export/) - Export a container’s filesystem as a tar archive
- The [docker import](https://docs.docker.com/reference/cli/docker/image/import/) - Import the contents from a tarball to create a filesystem image
- The [docker save](https://docs.docker.com/reference/cli/docker/image/save/)   - Save one or more images to a tar archive (streamed to STDOUT by default)
- The [docker load](https://docs.docker.com/reference/cli/docker/image/load/)   - Load an image from a tar archive or STDIN