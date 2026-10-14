# 06 — Docker Compose

Docker Compose describes and operates a multi-container application using a `compose.yaml` file. It makes local services, networks, configuration, and storage repeatable. Compose is useful for development and testing; production orchestration needs depend on the system and is not solved universally by Compose.

Compose **services** describe containers. `image` selects an image; `build` builds from a Dockerfile. `ports` publishes ports; `environment` configures runtime variables; `networks` control connectivity; `volumes` attach persistent or host storage; `depends_on` controls startup ordering and can use health conditions. A Dockerfile describes how to build one image; Compose describes how related services run together.

```bash
docker compose up --build -d
docker compose ps
docker compose logs -f
docker compose exec app python -c "print('running')"
docker compose build
docker compose restart app
docker compose down                 # containers and network; named data volume remains
docker compose down --volumes       # also deletes project volumes and their data
```

The complete Python + MySQL example is in [Exercise 03](exercises/03-python-mysql/README.md). It uses a MySQL health check and application retries: `depends_on` alone only orders startup and does not mean a database is ready to accept connections.

For routine operations: start with `up`, inspect with `ps`, follow logs, use `exec` for diagnosis, rebuild after source/image changes, and stop with `down`. Before any cleanup command that removes volumes, inspect the configured volume and confirm the data can be deleted.

## References

[Compose overview](https://docs.docker.com/compose/) · [Compose file reference](https://docs.docker.com/reference/compose-file/) · [Startup order](https://docs.docker.com/compose/how-tos/startup-order/)
