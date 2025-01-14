# Docker

- allows us to deploy applications in containers - lightweight virtual machines
- instead of just shipping an application we ship the application and the environment it runs in

- virtual machines virtualize hardware - very heavy on resources and slow to boot up
- containers virtualize at the operating system level

  - still have isolation between containers through namespaces - appears as though each container has its own file/operating system
  - in reality a lot of resources are being shared

- docker image is the read-only definition of a container
- docker container is a virtualized read-write environment
- docker container is basically a docker image that's running

- docker hub is official cloud service for storing/sharing docker images
  - usually paired with cloud platform
  - AWS has ECR, GCP has Container Registry

`docker help`

`docker run -d -p 80:80 docker/getting-started:latest`

- use `-b` flag to choose different port

`docker stop CONTAINER_ID` or if doesn't work `docker kill CONTAINER_ID`

`docker ps`
`docker ps -a`

`docker images`

`docker exec CONTAINER_ID ls`
`docker exec -it CONTAINER_ID /bin/sh` (`exit`)

- use `-W` flag for timeout

`docker stats`

- many docker containers are stateless - don't store state from previous sessions
- to store state we use **storage volumes**
- `docker volume create NAME`
- `docker volume ls`
- `docker volume inspect NAME`

- pull images from docker hub
- `docker pull IMAGE`
- publish `docker push USERNAME/IMAGE`

- publish tags and latest, then push both
```
docker build -t username/imagename:0.0.0 -t username/imagename:latest .
docker push username/imagename --all-tags
```

- `docker rm CONTAINER_ID`
- `docker volume rm CONTAINER_ID`

- networking - put container in offline mode - turn off networking
  `docker run -d --network none IMAGE`

- docker allows us to create custom bridge networks so that our containers can communicate with each other if we want, but otherwise remain isolated

- Dockerfiles - text definition of images

- Docker compose - defines and runs multi-container applications - simplifies control of whole stack
- manage services, networks, volumes in a single file
