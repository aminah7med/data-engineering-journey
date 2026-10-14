# 03 — Dockerfile and Build

A Dockerfile is a text recipe (not YAML) that Docker uses to build an image. The **build context** is the set of files sent to the builder; `COPY` paths are resolved from this context, not from arbitrary host paths.

```dockerfile
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY app.py .
USER 10001
EXPOSE 8000
ENTRYPOINT ["python", "app.py"]
CMD ["--help"]
```

- `FROM` selects the base image. Pin a maintained version; a digest pins exact content but needs deliberate updates. Mutable tags such as `latest` can change between builds.
- `WORKDIR` sets the working directory for following instructions.
- `COPY` copies build-context files. Prefer it for ordinary local files.
- `ADD` also supports archive handling and remote sources; use only when those features are intended.
- `RUN` executes build-time commands and creates a layer. Combine related package operations and clean package caches in the same instruction where appropriate.
- `ENV` sets image defaults, which can be overridden at runtime. Never put secrets here.
- `EXPOSE` documents the application's container port; it does not publish that port.
- `USER` selects the user for subsequent build steps and runtime defaults.
- `CMD` supplies default command or arguments; runtime arguments replace it.
- `ENTRYPOINT` defines the executable. With exec form, `CMD` commonly supplies its default arguments; `docker run image arg` replaces those arguments.

Use exec form (`["program", "arg"]`) for reliable signal handling. Shell-form entrypoints run through a shell and can interfere with signal delivery.

## Runnable Python example

Place these files in one directory:

```python
# app.py
import os

print(f"Hello, {os.getenv('GREETING', 'Docker learner')}!")
```

```dockerfile
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY app.py .
USER 10001
ENTRYPOINT ["python", "app.py"]
```

```text
# .dockerignore
.git
__pycache__/
.env
```

Build context and lifecycle:

```bash
docker build -t greeting:dev .
docker image inspect greeting:dev
docker run --rm -e GREETING="Data Engineer" greeting:dev
docker tag greeting:dev greeting:0.1.0
```

Each instruction may create a cached layer. Earlier stable dependency steps can be reused when later source changes. `.dockerignore` excludes unnecessary and sensitive files from the context, improving speed and reducing accidental inclusion.

## Optimization, multi-stage builds, security

Choose a suitable small maintained base, copy dependency manifests before frequently changing source, use `.dockerignore`, avoid unnecessary packages, and remove caches in the same layer that created them. Multi-stage builds keep compilers and build-only tools out of the final image:

```dockerfile
FROM golang:1.24 AS build
WORKDIR /src
COPY . .
RUN go build -o /out/service ./...
FROM gcr.io/distroless/static-debian12
COPY --from=build /out/service /service
ENTRYPOINT ["/service"]
```

Use trusted bases, update and scan dependencies, run as non-root where practical, and never copy credentials into an image. A build argument is not a safe secret store; use BuildKit secret mounts when a build truly requires secret access.

## References

[Dockerfile reference](https://docs.docker.com/reference/dockerfile/) · [Build context](https://docs.docker.com/build/concepts/context/) · [Build cache](https://docs.docker.com/build/cache/) · [Build secrets](https://docs.docker.com/build/building/secrets/)
