# Exercise 03 — Python + MySQL with Compose

This local environment runs a Python one-shot client and MySQL on an isolated Compose network. The app resolves `db` through Compose DNS and connects on the internal port 3306. MySQL is not published to the host because the exercise only needs app-to-database communication.

## Configure and start

From this directory, copy `.env.example` to `.env` and replace both placeholder passwords with local-only values. `.env` is excluded from the image build context. Do not commit it or use these local values in a real deployment. Compose uses the file for interpolation and explicitly passes needed variables to each service.

```bash
docker compose config
docker compose up --build -d
docker compose ps
docker compose logs -f db
docker compose logs app
```

The MySQL health check waits for connection and InnoDB initialization. Compose waits for the dependency's healthy status before starting the app, and the Python program also retries transient connections. `depends_on` startup order alone would not guarantee database readiness. The app prints the database name and server version, then exits successfully.

To run the app again, use `docker compose run --rm app`; to inspect the database container, run `docker compose exec db mysqladmin ping -h 127.0.0.1 -u root -p` and enter the local root password when prompted. Follow output with `docker compose logs -f` and review state with `docker compose ps`.

## Stop and clean up

`docker compose down` removes the containers and network but keeps the named `mysql-data` volume. On a later `up`, the existing database files are reused. To permanently remove the exercise database, first ensure nothing needs its contents, then run `docker compose down --volumes`; this deletes the volume and its database data. A backup should be made separately before destructive cleanup.

Delete the local `.env` file manually when no longer needed. Credentials here are placeholders for a local learning environment, not production secret management.
