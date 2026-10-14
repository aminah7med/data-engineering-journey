# 08 — Troubleshooting

## A repeatable diagnosis workflow

1. Confirm the client and engine: `docker version`, `docker context show`, `docker info`.
2. Check state: `docker ps -a` or `docker compose ps`.
3. Read application output: `docker logs <name>` or `docker compose logs <service>`.
4. Inspect configuration: `docker inspect <name>`, image, mounts, environment names, ports, and networks.
5. Reproduce one failure at a time; make a targeted change and observe again.

## Common symptoms

- **Engine unavailable:** start Docker Desktop or the Linux service; check the selected Docker context and WSL 2/Hyper-V configuration on Windows. `docker version` should show server details.
- **Image pull failure:** check spelling/tag, registry access, authentication, network, rate limits, and architecture compatibility. `docker pull image:tag` exposes the error directly.
- **Container exits immediately:** the main process ended or failed. Check `docker ps -a`, `docker logs`, and exit code from `docker inspect`. A short one-shot command exiting with code 0 is normal; nonzero usually indicates failure, though codes are application-specific. Code 137 often indicates SIGKILL (including possible out-of-memory kill); it is not proof of OOM by itself.
- **Port conflict:** choose an unused host port, e.g. `-p 8081:80`; `docker ps` shows published mappings. The host and container ports are distinct.
- **App cannot reach database:** inside the app use Compose service DNS (`db`) and container port (`3306`); verify shared network, credentials, readiness, and logs. `localhost` is the app container itself.
- **Published port but no response:** confirm the container is running, the host-to-container mapping targets the application's actual listening port, and the application binds to a container-reachable address (often `0.0.0.0` rather than container loopback `127.0.0.1`). `EXPOSE` does not start a listener or publish a host port.
- **Works on host but not in container:** check that required files were included in the build context, dependencies were installed into the image, case-sensitive paths are correct, runtime variables were passed, and host-only `localhost` assumptions were removed.
- **Missing file / wrong build context:** run build from the directory whose files should be available; check `COPY` paths and `.dockerignore`. Docker cannot `COPY` files outside the build context.
- **Executable not found:** check image contents, `WORKDIR`, executable path, architecture, line endings, and execute permissions. Use `docker run --rm --entrypoint sh image` when the image includes a shell.
- **Permission errors:** check UID/GID, mount ownership, read-only flags, and host filesystem sharing settings. Avoid solving every permission issue by running as root.
- **Data did not persist:** confirm the expected volume/mount was attached at the database's data path. Container-layer writes disappear when the container is removed.
- **Compose starts too early:** `depends_on` alone may not indicate readiness. Add a health check and use a healthy dependency condition; applications should still retry transient connections.
- **Unexpected rebuild/cache:** inspect build context and `COPY` ordering. Changing a copied file invalidates that layer and later layers. Use `docker build --no-cache` for diagnosis, not as a routine fix.

Useful commands: `docker logs`, `docker inspect`, `docker stats`, `docker events`, `docker compose config`, `docker compose ps`, and `docker network inspect`.

For a short-lived process, run it in the foreground first so its output is visible, or inspect a detached container with `docker logs`. `docker inspect --format '{{.State.Status}} {{.State.ExitCode}} {{.State.Error}}' <name>` can help expose its final state. Exit codes are supplied by the process/runtime and are not a universal error dictionary: code 0 generally signals process success; nonzero signals an error according to that program; 137 is consistent with SIGKILL but alone does not prove OOM.

## References

[Troubleshooting Docker Desktop](https://docs.docker.com/desktop/troubleshoot-and-support/) · [Compose CLI](https://docs.docker.com/reference/cli/docker/compose/) · [Container logs](https://docs.docker.com/reference/cli/docker/container/logs/)
