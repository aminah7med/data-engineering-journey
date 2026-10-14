# 10 — Docker Interview Questions

This guide is designed for Docker fundamentals used in local development and data engineering. For each answer, explain the concept, give an example, and mention a limitation or common mistake.

## 1. Core concepts

### 1. What is Docker?
**Model answer:** Docker is a platform for building, distributing, and running applications in isolated containers created from images. It helps standardize dependencies and configuration across development, CI, and deployment. It reduces environment drift but cannot eliminate differences in host kernels, CPU architecture, networking, configuration, or external services.

Example: a team can run the same MySQL image locally instead of asking each developer to install and configure MySQL manually.

```bash
docker version
docker info
docker compose version
```

### 2. Image vs container?
**Model answer:** An image is a read-only, layered template. A container is an instance created from that image, with runtime configuration and a writable layer. Multiple containers can share the same image while using different names, ports, environment variables, and mounts.

```bash
docker pull nginx:1.28.2
docker run --name web-a -d -p 8080:80 nginx:1.28.2
docker run --name web-b -d -p 8081:80 nginx:1.28.2
docker ps
```

Common mistake: assuming stopping a container deletes it, or that removing a container necessarily removes its named volumes.

### 3. Containers vs virtual machines?
**Model answer:** A VM virtualizes hardware and runs a guest OS with its own kernel. A container isolates processes while sharing the relevant host kernel. Containers generally start quickly and have lower overhead; VMs provide a separate guest kernel and can be useful for different OS requirements or isolation boundaries. Neither is universally better.

On Windows, Docker Desktop commonly runs Linux containers in a lightweight Linux environment through WSL 2 or Hyper-V.

### 4. What is a registry? What is Docker Hub?
**Model answer:** A registry stores and distributes container images. Docker Hub is one registry; organizations can use private registries as well. Tags are human-readable references and can move; digests identify exact image content.

```bash
docker pull nginx:1.27
docker tag my-app:dev registry.example/my-app:1.0
docker push registry.example/my-app:1.0
```

The push requires authentication and permission. Pinning content improves reproducibility but should not prevent planned security updates.

### 5. What happens when `docker run` executes?
**Model answer:** Docker resolves the image, pulls it if needed, creates a container with the requested configuration, and starts its main process. The container usually stops when that process exits.

```bash
docker run --name web -d -p 8080:80 nginx:1.28.2
docker ps
docker logs web
```

`-d` runs in the background; `-p 8080:80` publishes host port 8080 to container port 80.

## 2. Dockerfile and builds

### 6. What is a Dockerfile? Is it YAML?
**Model answer:** A Dockerfile is a text recipe used to build an image. It is normally named `Dockerfile` without an extension and is not YAML. Compose configuration, commonly `compose.yaml`, is YAML.

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY app.py .
USER 10001
CMD ["python", "app.py"]
```

Build from the directory containing the Dockerfile and `app.py`:

```bash
docker build -t greeting:dev .
docker run --rm greeting:dev
```

The final dot selects the current directory as the build context.

### 7. Explain common Dockerfile instructions.
| Instruction | Meaning |
|---|---|
| `FROM` | Selects the base image. |
| `WORKDIR` | Sets the working directory for following instructions. |
| `COPY` | Copies files from the build context into the image. |
| `RUN` | Executes a build-time command. |
| `ENV` | Sets an image environment-variable default. |
| `EXPOSE` | Documents a container port; it does not publish the port. |
| `USER` | Selects the user for later build steps and runtime defaults. |
| `CMD` | Supplies a default command or arguments. |
| `ENTRYPOINT` | Defines the executable. |

Never put credentials in ordinary Dockerfile `ENV` or build arguments.

### 8. `CMD` vs `ENTRYPOINT`?
**Model answer:** `ENTRYPOINT` specifies the executable; `CMD` supplies a default command or arguments. With exec-form `ENTRYPOINT`, the `CMD` array commonly supplies default arguments, and arguments passed after the image name replace those defaults.

```dockerfile
ENTRYPOINT ["python", "app.py"]
CMD ["--help"]
```

The default is `python app.py --help`. Prefer exec form for predictable signal handling.

### 9. `COPY` vs `ADD`?
**Model answer:** `COPY` copies build-context files. `ADD` also has additional behavior, including local archive handling and remote-source features. Prefer `COPY` for ordinary copies because its intent is clearer. Docker cannot copy arbitrary files outside the build context.

### 10. What is a build context and `.dockerignore`?
**Model answer:** The build context is the set of files made available to the builder. `.dockerignore` excludes unnecessary or sensitive files from it, reducing build work and the risk of accidentally including local files.

```text
.git
__pycache__/
.env
.venv/
```

### 11. How does build cache work?
**Model answer:** Docker can reuse unchanged build steps when instructions and relevant inputs remain the same. A changed input invalidates that step and can invalidate later steps. Copy dependency manifests and install dependencies before copying frequently changed application source to improve cache reuse.

Cache improves speed; it is not a substitute for updating or scanning dependencies.

### 12. What is a multi-stage build?
**Model answer:** It uses multiple `FROM` stages so build tools and intermediate artifacts can be excluded from the final runtime image. This can reduce image size and attack surface, especially for compiled applications. It is not required for every small interpreted-language app.

## 3. Container lifecycle and diagnosis

### 13. `stop`, `start`, `restart`, `pause`, and `rm`?
- `stop`: asks the main process to terminate gracefully, then may kill it after a timeout.
- `start`: starts an existing stopped container.
- `restart`: stops and starts the existing container.
- `pause` / `unpause`: freeze and resume container processes.
- `rm`: removes a stopped container; `rm -f` forcibly stops and removes it.

Stopping preserves the container and its writable layer. Removing it deletes that layer. Separately mounted volume data normally remains until the volume is removed.

### 14. `logs`, `inspect`, and `exec`?
**Model answer:** `logs` shows stdout/stderr from the main process, `inspect` shows detailed state and configuration, and `exec` starts another process in a running container.

```bash
docker logs -f web
docker inspect web
docker exec -it web sh
```

Not every image includes Bash or even a shell. `exec` requires the container to be running.

### 15. What does `-p 8080:80` mean? What does `EXPOSE 80` mean?
**Model answer:** `-p 8080:80` publishes host port 8080 to container port 80. `EXPOSE 80` documents the intended container port in image metadata; it does not publish a host port. Containers on a shared network generally use the container/service port for peer-to-peer communication.

### 16. What do you check if a container exits immediately?
Check state, logs, and exit code:

```bash
docker ps -a
docker logs <container-name>
docker inspect <container-name>
```

A one-shot job exiting with code 0 may be normal. Exit code 137 often indicates SIGKILL and can be consistent with an out-of-memory kill, but does not prove that was the cause.

## 4. Storage, networking, and Compose

### 17. Named volume vs bind mount vs writable layer?
| Storage | Typical use | Lifecycle |
|---|---|---|
| Container writable layer | Temporary container-local changes | Removed with the container |
| Named volume | Database files and persistent local state | Remains until the volume is removed |
| Bind mount | Source code and host-managed files | Uses a specific host path and its permissions |

A volume provides persistence, not a backup. Database backups should be created with suitable database-aware methods, stored separately, and tested.

**Danger:** `docker compose down --volumes` removes project volumes and their data. Check before running it.

### 18. How do containers find each other?
**Model answer:** Attach them to a shared network. User-defined bridge networks provide name-based discovery; Compose registers service names in its project network. An app connecting to a Compose MySQL service normally uses hostname `db` and container port `3306`.

Inside a container, `localhost` means that same container—not another service and not automatically the host.

### 19. Dockerfile vs Docker Compose?
**Model answer:** A Dockerfile describes how to build an image. Compose describes how related services, networks, configuration, and volumes run together, usually from `compose.yaml`.

```bash
docker compose config
docker compose up --build -d
docker compose ps
docker compose logs -f
docker compose down
```

`docker compose down` normally keeps named volumes; `docker compose down --volumes` can delete their data.

### 20. Does `depends_on` guarantee database readiness?
**Model answer:** Not by itself. Basic `depends_on` controls startup order, not necessarily readiness. Where appropriate, configure a health check and a healthy dependency condition. The application should still handle transient connection failures with bounded retries and backoff.

A health check reports a condition; it does not repair a broken service.

### 21. How should configuration and secrets be handled?
**Model answer:** Keep runtime configuration separate from code. Compose uses a project `.env` file for interpolation, but values are not automatically placed inside every container unless mapped with `environment:` or `env_file:`.

Do not commit real `.env` files, bake secrets into image layers, or print credentials in logs. Environment variables can be visible to privileged users and process inspection; use appropriate secret-management facilities, restrict access, and rotate credentials. Use safe placeholders in `.env.example`.

## 5. Scenario questions

### 22. The app cannot connect to MySQL in Compose. What do you investigate?
1. Check both services' status, health, and logs.
2. Confirm the app uses hostname `db` and port `3306`, not `localhost`.
3. Confirm both services share a network.
4. Check credentials, variable names, and database initialization.
5. Test DNS and TCP connectivity from the app container.
6. Keep bounded retry logic for transient failures.

MySQL does not need a published host port for app-to-database communication on the Compose network.

**Reasoning:** published ports serve clients outside the Compose network. Two services on the same network use internal DNS and the database's listening port. First confirm the app container has the expected `DB_HOST`, `DB_PORT`, database name, user, and password, then compare service health and logs. A typo and an unready server can produce similar connection errors, so check both configuration and readiness.

```bash
docker compose ps
docker compose logs app db
docker compose exec app python -c "import socket; print(socket.getaddrinfo('db', 3306))"
```

The last command only checks name resolution; it does not prove that MySQL accepted authentication or that a SQL query succeeds.

### 23. Database records disappeared after recreation. Why?
Data may have been written only to the container layer, the volume may have been mounted at the wrong path, a different volume may have been used, or the volume may have been removed. Inspect mounts and volume names. Use a named volume for local persistence, but keep separate verified backups for important data.

### 24. A build is slow or the image is large. What do you do?
Review build context size, `.dockerignore`, layer order, base image, and retained build artifacts. Copy stable dependency manifests before frequently changing source. Use multi-stage builds when build tools do not belong in the runtime image. Use `docker build --no-cache` for diagnosis, not as a routine optimization.

### 25. A port is published, but the application is unreachable. What do you check?
First confirm the container is running and the host mapping is present (`docker ps` or `docker port <name>`). Read application logs. Confirm the process listens on the container interface, commonly `0.0.0.0:<container-port>`, rather than only `127.0.0.1` inside the container; check that the container port in `-p host:container` matches the listener. Then test the host port and check for host firewall or port conflicts. `EXPOSE` metadata does not create a listener or a host mapping.

### 26. An application works on the host but fails in a container. Why?
Compare the runtime environment rather than assuming Docker changed the code: verify that dependencies were installed into the image, required files are inside the build context and not ignored, configured paths and filename case match, environment variables were passed at runtime, the app listens on the expected interface, and the image architecture is compatible. Rebuild after Dockerfile or dependency changes, and inspect the container's logs. Host-only paths and services at `localhost` are common causes.

### 27. A Compose app starts before its dependency is ready. What is the fix?
Use a database health check that tests a meaningful readiness condition and set the app's `depends_on` condition to `service_healthy`. Keep bounded retry/backoff in the application: the database may restart after startup or become temporarily unavailable. Verify the health status and database logs rather than increasing a fixed sleep blindly.

### 28. How do you investigate high CPU or memory use?
Use `docker stats` to identify resource use, then inspect logs, application behavior, and resource configuration. Distinguish an application leak or workload spike from host pressure. Set appropriate resource limits and measure after changes.

```bash
docker stats
docker inspect <container-name>
docker logs --tail 200 <container-name>
```

### 29. What are practical Docker security practices?
Use trusted, maintained base images; update dependencies deliberately; run as non-root where practical; minimize capabilities and unnecessary packages; keep secrets out of images; scan images; and restrict registry and runtime access. Pinning improves reproducibility but should not stop security updates. Containers are not automatically secure sandboxes.

### 30. How does Docker help a Data Engineer?
Docker provides repeatable environments for local databases, brokers, ingestion jobs, and integration tests. It can package Python jobs and help standardize development and CI. Compose can run a small set of related services locally.

Docker does not replace orchestration, data-quality design, monitoring, backups, access control, or production operations. A containerized pipeline can still fail due to bad data, unavailable dependencies, poor retry logic, or resource limits.

### 31. Docker vs Kubernetes?
**Model answer:** Docker provides tools for building and running containers. Kubernetes orchestrates workloads across a cluster. Compose is useful for defining and running multi-container environments, especially locally; it is not a universal replacement for Kubernetes. For Docker fundamentals, understand the distinction without studying Kubernetes administration in depth.

### 32. Why use an image digest instead of a tag?
**Model answer:** Tags are convenient references but can move to different image content. A digest identifies exact content and improves artifact traceability and reproducibility. Teams still need a deliberate process for reviewing and adopting updated images rather than pinning forever.

## Hands-on practice

Try these without looking at the answers first:

1. Run Nginx detached on host port 8080; inspect it, read logs, stop/start it, then remove it.
2. Explain `docker image ls`, `docker ps`, and `docker ps -a`.
3. Build the Python exercise image, pass an environment variable, and explain what `--rm` removes.
4. Demonstrate named-volume persistence across container replacement and explain how removing the volume differs from removing a container.
5. Run Python and MySQL with Compose. Explain `db:3306`, readiness checks, and why MySQL need not publish a host port for app-to-database traffic.
6. Cause a container to fail intentionally, diagnose it with status and logs, and explain the fix.
7. Explain why a volume is not a backup and why secrets should not be copied into an image.

## Suggested interview-answer structure

1. **Definition:** Explain the concept in one or two sentences.
2. **Mechanism:** Describe how it works.
3. **Example:** Give a realistic command or scenario.
4. **Trade-off:** Mention a limitation or common mistake.

Do not memorize wording without understanding it. Be ready to explain why a command is appropriate and what can go wrong.
