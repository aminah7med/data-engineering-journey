# 04 — Volumes and Persistence

Each container has a writable layer above its image layers. It is convenient for temporary runtime changes, but belongs to that container and disappears when it is removed.

## Storage choices

- **Named volume:** managed by Docker and stored outside a container's lifecycle. Good default for database files. It persists across container replacement until explicitly removed.
- **Bind mount:** maps a host path into a container. Useful for source-code development and host-managed files; paths and permissions vary by OS.
- **tmpfs:** temporary in-memory storage on supported Linux hosts. It is not persistent and is unavailable in the same way for all desktop configurations.

```bash
docker volume create db-data
docker run -d --name mysql-example \
  -e MYSQL_ROOT_PASSWORD=local-only-placeholder \
  -v db-data:/var/lib/mysql mysql:8.4
docker volume inspect db-data
docker stop mysql-example
docker rm mysql-example
# Recreate with -v db-data:/var/lib/mysql to reuse database files.
```

Prefer runtime secrets or local-only placeholders in examples; never use this placeholder for a real deployment. A read-only bind mount uses `-v "$PWD/config:/app/config:ro"` (PowerShell path syntax may differ) or `--mount type=bind,src=...,dst=...,readonly`. Read-only mounts prevent container writes through that mount.

## Safe persistence and backup

Database files should be stored on a named volume or deliberately managed persistent storage, not only in the container writable layer. Database backup should use database-aware tools and be stored separately; a volume is persistence, not a backup. Coordinate backups with the database to avoid inconsistent copies, and test restoration.

`docker compose down` removes containers and networks but keeps named volumes. `docker compose down --volumes` removes project-managed volumes and permanently deletes their contents. Inspect volume names and ensure a verified backup exists before cleanup.

## Common mistakes

- Writing important files into the container layer and expecting them to survive replacement.
- Mounting an empty volume over a populated image directory and hiding the image's files.
- Using a host bind path that does not exist or has unsuitable permissions.
- Assuming deleting a container also deletes its named volume (it normally does not).
- Assuming a volume is automatically backed up or encrypted.

## References

[Volumes](https://docs.docker.com/engine/storage/volumes/) · [Bind mounts](https://docs.docker.com/engine/storage/bind-mounts/) · [tmpfs mounts](https://docs.docker.com/engine/storage/tmpfs/)
