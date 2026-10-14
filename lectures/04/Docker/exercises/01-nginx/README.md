# Exercise 01 — Nginx

Prerequisite: Docker Engine is running (`docker version`). Commands below work in a POSIX shell; run each command separately in PowerShell if `&&` is unavailable.

1. Pull a specific Nginx image: `docker pull nginx:1.27`.
2. List images: `docker image ls nginx`.
3. Run a named, detached container and publish host port 8080 to container port 80: `docker run --name study-nginx -d -p 8080:80 nginx:1.27`.
4. Open [http://localhost:8080](http://localhost:8080). Nginx's welcome page should appear if port 8080 is free.
5. Inspect output with `docker logs study-nginx`; inspect state/mappings with `docker inspect study-nginx`.
6. Try a shell: `docker exec -it study-nginx sh`. Official Nginx images commonly include `sh`; exit the shell to return to the host.
7. Lifecycle practice: `docker stop study-nginx`, `docker start study-nginx`, `docker restart study-nginx`.
8. Cleanup: `docker stop study-nginx` then `docker rm study-nginx`.

The image remains cached after container removal. If another service uses port 8080, select another host port such as `-p 8081:80` and browse to that port. The exercise stores no important data.
