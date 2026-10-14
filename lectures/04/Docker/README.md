# Docker

This section builds practical Docker knowledge for local development and data engineering workflows. These notes are study material and hands-on exercises you can run locally. Status markers indicate study progress and are maintained by the author.

## Learning objectives

- Explain Docker architecture and the relationship between Dockerfile, image, container, registry, network, and volumes.
- Build small, reproducible, secure images and understand build cache and multi-stage builds.
- Run, inspect, troubleshoot, and clean up containers safely.
- Use Compose to operate a local multi-service application (app + database) for development and testing.
- Apply configuration and persistence practices suitable for data systems and local experiments.

## Prerequisites

- Comfortable with the command line (bash, PowerShell) and editing small text files.
- Basic knowledge of filesystems and TCP ports.
- Python knowledge helps for the examples included here.
- Install Docker Desktop (Windows/macOS) or Docker Engine (Linux). On Windows prefer the WSL 2 backend for Linux containers.
- Check that the daemon is reachable with `docker version` (the **Server** section should appear), and that Compose v2 is available with `docker compose version`.

## Recommended sequence (table of contents)

| # | Topic | Link | Status |
|---:|---|---|---|
| 01 | Docker fundamentals | [Read](01-docker-fundamentals.md) | ⚪ Not Started |
| 02 | Images and containers | [Read](02-images-and-containers.md) | ⚪ Not Started |
| 03 | Dockerfile and build | [Read](03-dockerfile-and-build.md) | ⚪ Not Started |
| 04 | Volumes and persistence | [Read](04-volumes-and-persistence.md) | ⚪ Not Started |
| 05 | Networking | [Read](05-networking.md) | ⚪ Not Started |
| 06 | Docker Compose | [Read](06-docker-compose.md) | ⚪ Not Started |
| 07 | Environment variables & secrets | [Read](07-environment-variables.md) | ⚪ Not Started |
| 08 | Troubleshooting | [Read](08-troubleshooting.md) | ⚪ Not Started |
| 09 | Best practices | [Read](09-docker-best-practices.md) | ⚪ Not Started |
| 10 | Interview guide (study) | [Study](10-docker-interview-questions.md) | ⚪ Not Started |

The table order is the suggested order: learn one lesson, run its related commands, then attempt the matching exercise before moving on. Status shows study progress, not whether a file exists.

## Practical exercises

1. [Run Nginx](exercises/01-nginx/README.md) and practice the container lifecycle.
2. [Build a Python container](exercises/02-python-container/README.md) and pass runtime configuration.
3. [Run Python with MySQL](exercises/03-python-mysql/README.md) using Compose, a health check, and persistent storage.

## Study completion checklist

- [ ] I can explain the client, daemon, image, container, registry, and kernel relationship in my own words.
- [ ] I can build an image, run and inspect a container, read its logs, and explain its exit status.
- [ ] I can explain the build context, `.dockerignore`, cache, `CMD`/`ENTRYPOINT`, and `EXPOSE`/published ports.
- [ ] I can choose between a writable layer, named volume, and bind mount, and describe the data lost by each cleanup command.
- [ ] I can connect Compose services by name and explain why `localhost` inside a container refers to itself.
- [ ] I can diagnose a database readiness failure and keep credentials out of source and images.
- [ ] I have run all three exercises and can troubleshoot them without copying the commands blindly.

## Commands to remember (with explanation)

```bash
# Show client and server version info
docker version

# Pull an image explicitly by tag
docker pull nginx:1.28.2

# List local images
docker image ls

# Build an image from the current directory (build context)
docker build -t sample:dev .

# Run a container in the background, map host port 8080 -> container 80
docker run --name web -d -p 8080:80 nginx:1.28.2

# Show running containers
docker ps

# Follow container logs (stdout/stderr)
docker logs -f web

# Inspect low-level runtime/configuration details
docker inspect web

# Run an interactive command inside a running container
docker exec -it web sh

# Stop and remove a container
docker stop web && docker rm web

# List and inspect volumes and networks
docker volume ls
docker network ls

# Compose commands (modern `docker compose` plugin)
docker compose up --build -d
docker compose ps
docker compose logs -f
# Remove containers and network but KEEP named volumes
docker compose down
# Remove containers, network AND named volumes (data lost)
docker compose down --volumes
```

Note: On PowerShell adjust quoting and escaping. `docker compose down` keeps named volumes by default. Deleting a volume permanently deletes its stored data unless backed up.

## Official references

- [Docker Docs](https://docs.docker.com/)
- [Get started](https://docs.docker.com/get-started/)
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Compose environment variables](https://docs.docker.com/compose/how-tos/environment-variables/)
- [Compose startup order](https://docs.docker.com/compose/how-tos/startup-order/)
- [Volumes](https://docs.docker.com/engine/storage/volumes/)
- [Networking in Compose](https://docs.docker.com/compose/how-tos/networking/)

Image families used in the examples (`python:3.12-slim`, `mysql:8.4`, and Nginx `1.28.2`) were checked against their official image listings on 2026-10-14. Version-family tags such as `3.12-slim` and `8.4` can move as patch releases are updated; use a digest when exact image identity is required, and update pinned content deliberately for security fixes.
