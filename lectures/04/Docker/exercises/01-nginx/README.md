# Exercise 01 — Nginx

## Prerequisites

Docker Desktop or Docker Engine must be running. Check that `docker version` shows both Client and Server information. This exercise uses the Docker Official Image `nginx:1.28.2`; its tag was checked against Docker Hub's official Nginx image listing on 2026-10-14. A versioned tag can still receive image updates or be republished; use a digest when exact content identity matters.

## Pull, run, and verify

Run commands from any directory. If you already have a container named `study-nginx`, remove it first with the cleanup commands below.

```bash
docker pull nginx:1.28.2
docker image ls nginx
docker run --name study-nginx -d -p 8080:80 nginx:1.28.2
docker ps
docker logs study-nginx
docker inspect study-nginx
```

Open [http://localhost:8080](http://localhost:8080). The Nginx welcome page should load. `-d` leaves the service running in the background; `-p 8080:80` forwards host port 8080 to Nginx's container port 80. The image's `EXPOSE` metadata alone would not publish it.

## Inspect and practice lifecycle

```bash
docker exec -it study-nginx sh
```

The official Nginx image includes `sh`. Type `exit` to leave the shell. `docker stop study-nginx` stops the service but keeps the container; `docker start study-nginx` starts that same container; `docker restart study-nginx` stops and starts it.

## Troubleshooting

- If the name is already in use, inspect it with `docker ps -a` and remove it if it is only this exercise's old container.
- If port 8080 is occupied, publish another host port, such as `-p 8081:80`, and browse to `http://localhost:8081`.
- If the page does not load, check `docker ps`, `docker logs study-nginx`, and the `Ports` field from `docker ps`; confirm the daemon is running and no firewall or proxy is interfering.
- If the container exited, `docker ps -a` and `docker logs study-nginx` show the state and main-process output.

## Cleanup and persistence

```bash
docker stop study-nginx
docker rm study-nginx
```

Removal deletes the container's writable layer, but keeps the downloaded Nginx image. This exercise mounts no volume and stores no data that needs preservation. To remove the image too, use `docker image rm nginx:1.28.2` after no container depends on it. On PowerShell, run commands one per line if shell chaining syntax differs.
