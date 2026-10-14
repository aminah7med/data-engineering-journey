# Docker

A practical introduction to Docker for local development and Data Engineering workflows. This section combines structured learning notes, command references, and hands-on exercises to help you understand containerization and apply it in practice.

> **Learning approach:** Read each lesson, run the relevant commands, complete the related exercises, and update your progress as you learn.

## Learning Objectives

By the end of this section, you should be able to:

- Explain Docker architecture and the relationships between Dockerfiles, images, containers, registries, networks, and volumes.
- Build reproducible container images and understand build contexts, caching, and multi-stage builds.
- Run, inspect, troubleshoot, and safely remove containers.
- Use Docker Compose to manage multi-service applications, including applications that depend on databases.
- Understand configuration, credentials, networking, and data persistence in local development environments.
- Apply Docker fundamentals to practical Data Engineering workflows.

## Prerequisites

Before starting, make sure you have:

- Basic command-line experience with Bash or PowerShell.
- A basic understanding of filesystems, processes, and TCP ports.
- Basic Python knowledge for the Python container exercises.
- Docker Desktop on Windows/macOS, or Docker Engine on Linux.
- Docker Compose v2 available in your environment.

On Windows, Docker Desktop with the WSL 2 backend is a common setup for running Linux containers.

Verify your installation:

```bash
docker --version
docker version
docker compose version
```

The `docker version` command displays client and server information. If the server information is missing or the daemon is unreachable, resolve that issue before continuing.

## Learning Roadmap

Follow the lessons in order. Practice the relevant commands and complete the exercises before moving to the next topic.

| # | Topic | Learning Material |
|---:|---|---|
| 01 | Docker Fundamentals | [Read Lesson 01](01-docker-fundamentals.md) |
| 02 | Images and Containers | [Read Lesson 02](02-images-and-containers.md) |
| 03 | Dockerfile and Image Building | [Read Lesson 03](03-dockerfile-and-build.md) |
| 04 | Volumes and Data Persistence | [Read Lesson 04](04-volumes-and-persistence.md) |
| 05 | Container Networking | [Read Lesson 05](05-networking.md) |
| 06 | Docker Compose | [Read Lesson 06](06-docker-compose.md) |
| 07 | Environment Variables and Secrets | [Read Lesson 07](07-environment-variables.md) |
| 08 | Troubleshooting | [Read Lesson 08](08-troubleshooting.md) |
| 09 | Docker Best Practices | [Read Lesson 09](09-docker-best-practices.md) |
| 10 | Interview Preparation | [Study the Interview Guide](10-docker-interview-questions.md) |

**Progress tracking:** The links above identify the intended study order. Track your personal completion status separately as you work through each lesson.

## Hands-on Exercises

The exercises provide opportunities to apply the concepts rather than only memorize commands.

| Exercise | What You Will Practice | Instructions |
|---|---|---|
| 01 — Nginx | Running a container, publishing ports, viewing logs, and managing the container lifecycle | [Open Exercise 01](exercises/01-nginx/README.md) |
| 02 — Python Container | Building a Python image and running a containerized application | [Open Exercise 02](exercises/02-python-container/README.md) |
| 03 — Python and MySQL | Connecting application and database services with Docker Compose, health checks, and persistent storage | [Open Exercise 03](exercises/03-python-mysql/README.md) |

Follow the instructions in each exercise's README. Commands and configuration requirements may differ between exercises.

## Study Checklist

Use this checklist to evaluate your understanding. Mark an item only when you can explain or demonstrate it independently.

- [ ] Explain the Docker client, daemon, images, containers, registries, and the role of the host kernel.
- [ ] Build an image and explain the build context, `.dockerignore`, image layers, and build cache.
- [ ] Run, inspect, stop, restart, and remove containers safely.
- [ ] Read container logs and investigate unexpected exit codes.
- [ ] Explain `CMD` versus `ENTRYPOINT` and `EXPOSE` versus published ports.
- [ ] Choose appropriately between a container writable layer, a named volume, and a bind mount.
- [ ] Explain container networking and why `localhost` inside a container refers to that container itself.
- [ ] Configure services in Docker Compose and understand startup order versus application readiness.
- [ ] Diagnose common application-to-database connection failures.
- [ ] Keep credentials out of source code and container images.
- [ ] Complete all three exercises and explain the commands you used.

## Essential Docker Commands

The following commands cover common tasks you will use while learning Docker.

### 1. Installation and Environment

```bash
# Display the Docker client version
docker --version

# Display client and server information
docker version

# Display Docker Engine configuration and system information
docker info

# Display the Docker Compose version
docker compose version
```

### 2. Images and Building

```bash
# Download an image from a registry
docker pull nginx:1.28.2

# List locally available images
docker image ls

# Build an image using the current directory as the build context
docker build -t sample:dev .

# Inspect image metadata
docker image inspect sample:dev
```

The final `.` in the build command specifies the build context. Files available to `COPY` and `ADD` must be within the permitted build context.

### 3. Running and Inspecting Containers

```bash
# Start a container in detached mode and publish host port 8080
# to container port 80
docker run --name web -d -p 8080:80 nginx:1.28.2

# List running containers
docker ps

# List all containers, including stopped containers
docker ps -a

# Follow the container logs
docker logs -f web

# Inspect container configuration and runtime state
docker inspect web

# Execute a shell inside a running container
docker exec -it web sh

# Display container resource usage
docker stats
```

If the Nginx container is running, open `http://localhost:8080` in your browser.

The `docker exec` command requires a running container. A minimal image may not include Bash, so `sh` is often a more portable first option.

### 4. Container Lifecycle and Cleanup

```bash
# Stop a running container
docker stop web

# Start an existing stopped container
docker start web

# Restart a container
docker restart web

# Remove a stopped container
docker rm web

# List available volumes and networks
docker volume ls
docker network ls
```

Stopping a container does not remove it. Removing a container removes its writable layer, but data stored in a separate volume can persist.

Be careful with cleanup commands. Understand what will be deleted before running them.

### 5. Docker Compose

Run these commands from the directory containing the Compose configuration file.

```bash
# Build images when needed and start services in the background
docker compose up --build -d

# List Compose services and their states
docker compose ps

# Follow logs from all Compose services
docker compose logs -f

# Stop and remove Compose containers and the default network
docker compose down

# Also remove named volumes declared in the Compose configuration
# WARNING: persistent data stored in those volumes will be deleted
docker compose down --volumes
```

By default, `docker compose down` does not remove named volumes. Adding `--volumes` can permanently delete database data stored in those volumes.

**Important:** Adapt commands to the current exercise and environment. Do not run destructive cleanup commands against data you need to preserve.

## Official Documentation

Use the official documentation when you need to verify command behavior, configuration options, or current recommendations.

- [Docker Documentation](https://docs.docker.com/)
- [Docker Get Started Guide](https://docs.docker.com/get-started/)
- [Dockerfile Reference](https://docs.docker.com/reference/dockerfile/)
- [Docker Compose File Reference](https://docs.docker.com/reference/compose-file/)
- [Compose Environment Variables](https://docs.docker.com/compose/how-tos/environment-variables/)
- [Compose Startup Order](https://docs.docker.com/compose/how-tos/startup-order/)
- [Docker Volumes](https://docs.docker.com/engine/storage/volumes/)
- [Docker Compose Networking](https://docs.docker.com/compose/how-tos/networking/)

## Notes on Image Versions

Examples in this section may use versioned image tags such as `nginx:1.28.2`, `python:3.12-slim`, and `mysql:8.4`.

Image tags and their availability can change over time. Before using a tag, verify it against the relevant official image listing. For reproducible environments, understand the difference between a version tag and an immutable image digest. Keep images updated deliberately to receive relevant security fixes.

## Recommended Study Workflow

1. Read one lesson and make sure you understand its core concepts.
2. Run the commands yourself instead of copying them without understanding.
3. Complete the corresponding practical exercise when applicable.
4. Use the troubleshooting lesson when something behaves unexpectedly.
5. Answer the relevant interview questions in your own words.
6. Update your study progress only after you can explain or demonstrate the material.

The goal is to develop practical Docker skills that support reliable local development and Data Engineering workflows, not simply to memorize commands.
