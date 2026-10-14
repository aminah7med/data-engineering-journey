# Docker

This section builds practical Docker knowledge for local development and data engineering workflows. Notes are study material; their existence does not indicate that a topic has been completed.

## Learning objectives

- Explain Docker's architecture and the relationship between images, containers, registries, networks, and volumes.
- Build small, reproducible, appropriately secured images.
- Run, inspect, troubleshoot, and clean up containers safely.
- Use Compose to operate a local multi-service application.
- Apply configuration and persistence practices suitable for data systems.

## Prerequisites

Basic command-line use, filesystems, networking, and Python are helpful. Install Docker Desktop on Windows (typically using its WSL 2 backend; Hyper-V is another supported configuration) or Docker Engine on Linux. Confirm the engine is running with `docker version` and `docker compose version`.

## Recommended sequence and table of contents

| # | Topic | Notes | Status |
|---:|---|---|---|
| 01 | Docker fundamentals | [Read](01-docker-fundamentals.md) | ⚪ Not Started |
| 02 | Images and containers | [Read](02-images-and-containers.md) | ⚪ Not Started |
| 03 | Dockerfile and build | [Read](03-dockerfile-and-build.md) | ⚪ Not Started |
| 04 | Volumes and persistence | [Read](04-volumes-and-persistence.md) | ⚪ Not Started |
| 05 | Networking | [Read](05-networking.md) | ⚪ Not Started |
| 06 | Docker Compose | [Read](06-docker-compose.md) | ⚪ Not Started |
| 07 | Environment variables | [Read](07-environment-variables.md) | ⚪ Not Started |
| 08 | Troubleshooting | [Read](08-troubleshooting.md) | ⚪ Not Started |
| 09 | Best practices | [Read](09-docker-best-practices.md) | ⚪ Not Started |
| 10 | Interview questions | [Study](10-docker-interview-questions.md) | ⚪ Not Started |

Suggested sequence: fundamentals → images/containers → Dockerfile/build → persistence and networking → Compose and configuration → troubleshooting and best practices → interview review.

## Practical exercises

1. [Run Nginx](exercises/01-nginx/README.md) and practice the container lifecycle.
2. [Build a Python container](exercises/02-python-container/README.md) and pass runtime configuration.
3. [Run Python with MySQL](exercises/03-python-mysql/README.md) using Compose, a health check, and persistent storage.

## Commands to remember

```bash
docker version
docker pull nginx:1.27
docker image ls
docker build -t sample:dev .
docker run --name web -d -p 8080:80 nginx:1.27
docker ps -a
docker logs -f web
docker inspect web
docker exec -it web sh
docker stop web && docker rm web
docker volume ls
docker network ls
docker compose up --build -d
docker compose ps
docker compose logs -f
docker compose down                 # keeps named volumes
docker compose down --volumes       # removes project volumes and their data
```

On PowerShell, run chained commands on separate lines if shell syntax differs. `docker compose down` preserves named volumes; deleting a volume permanently deletes its stored data unless backed up elsewhere.

## Official references

- [Docker Docs](https://docs.docker.com/)
- [Get started](https://docs.docker.com/get-started/)
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Volumes](https://docs.docker.com/engine/storage/volumes/)
- [Networking](https://docs.docker.com/engine/network/)
