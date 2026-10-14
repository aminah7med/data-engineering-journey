# Exercise 02 — Python Container

This small application uses only Python's standard library. `requirements.txt` is included to show where dependencies belong; no installation step is needed.

Prerequisite: a running Docker daemon (`docker version` should show a Server section). The Dockerfile uses the maintained Python 3.12 slim official image family; `3.12-slim` tracks patch updates within Python 3.12 rather than pinning an immutable digest.

From this directory:

```bash
docker build -t study-greeting:dev .
docker image inspect study-greeting:dev
docker run --rm study-greeting:dev
docker run --rm -e GREETING="Welcome" -e LEARNER="Amina" study-greeting:dev
```

Expected output is `Hello, Docker learner!` by default, with the supplied values in the second run. `docker build` sends this directory as build context and creates an image from the Dockerfile. `docker run` creates a container, executes the Python entry point with runtime environment values, prints output, and exits. `--rm` removes that short-lived container while keeping the image.

The image uses a slim Python base, copies only the application, and runs with an unprivileged numeric user. The example contains no credentials. Rebuild after changing `app.py` with `docker build -t study-greeting:dev .`.

## Troubleshooting and cleanup

- A pull/build failure often means Docker Desktop is not running, registry access is unavailable, or the host cannot pull the selected image for its platform. Check the full build error and `docker version`.
- `docker run --rm` prints output and removes the short-lived container as soon as Python exits. Use `docker ps -a` only if you run without `--rm` and want to inspect a stopped container.
- If Python reports a missing file, build from this directory so `app.py` is in the build context.
- If a container name is in use, this example's `--rm` run has no persistent name; inspect other containers before removing anything.

No ports, volumes, or persistent data are used. The container is removed by `--rm`; the image remains until explicitly removed with `docker image rm study-greeting:dev`.
