# Exercise 02 — Python Container

This small application uses only Python's standard library. `requirements.txt` is included to show where dependencies belong; no installation step is needed.

From this directory:

```bash
docker build -t study-greeting:dev .
docker image inspect study-greeting:dev
docker run --rm study-greeting:dev
docker run --rm -e GREETING="Welcome" -e LEARNER="Amina" study-greeting:dev
```

Expected output is `Hello, Docker learner!` by default, with the supplied values in the second run. `docker build` sends this directory as build context and creates an image from the Dockerfile. `docker run` creates a container, executes the Python entry point with runtime environment values, prints output, and exits. `--rm` removes that short-lived container while keeping the image.

The image uses a slim Python base, copies only the application, and runs with an unprivileged numeric user. The example contains no credentials. Rebuild after changing `app.py` with `docker build -t study-greeting:dev .`.
