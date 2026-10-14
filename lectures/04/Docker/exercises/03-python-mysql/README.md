# Exercise 03 — Python + MySQL with Compose

This local environment runs a Python one-shot client and MySQL on an isolated Compose network. The app resolves `db` through Compose DNS and connects on the internal port 3306. MySQL is not published to the host because the exercise only needs app-to-database communication. It uses the official `mysql:8.4` image family and `mysql-connector-python==9.2.0` in the client. The MySQL 8.4 image family was present in the official Docker Hub listing when checked on 2026-10-14; the family tag can move to later 8.4 patch releases.

## Configure and start

From this directory, copy `.env.example` to `.env` and replace both placeholder passwords with local-only values. Bash: `cp .env.example .env`. PowerShell: `Copy-Item .env.example .env`. `.env` is excluded from Git and from the image build context. Do not commit it or use these local values in a real deployment. Compose uses the file for interpolation and explicitly passes needed variables to each service. Check that `git status --short` does not list `.env` before committing.

```bash
docker compose config
docker compose up --build -d
docker compose ps
docker compose logs -f db
docker compose logs app
```

The health check runs `mysqladmin ping` against MySQL over TCP using `CMD-SHELL`. The official MySQL image does not provide the MariaDB-specific `healthcheck.sh` script; this command is selected for the MySQL image and Compose's `$$` defers expansion of the root password variable until the health-check runs inside that container. `mysqladmin ping` indicates that the server responds; it is not an authentication test for the app account. The actual Python query checks that separately. Compose waits for the dependency's healthy status before starting the app, and the Python program also retries transient connections. `depends_on` startup order alone would not guarantee database readiness. The app prints `Connected to database learning on MySQL ...` (server patch version varies), then exits successfully.

The named volume is mounted at `/var/lib/mysql`, the official MySQL data directory. On first initialization, the image creates the configured database and non-root user. Initialization environment variables are ignored for an already initialized data directory: changing the `.env` values does not reset an existing database password or recreate its schema. To apply such changes, use SQL against the existing database or deliberately remove the data volume after deciding that its contents can be lost.

To run the app again, use `docker compose run --rm app`; it should exit with status 0 after printing its connection message. To inspect the database container, run `docker compose exec db mysqladmin ping -h 127.0.0.1 -u root -p` and enter the local root password when prompted. `mysqld is alive` indicates the server responds. Follow output with `docker compose logs -f` and review state with `docker compose ps`.

If the app exits unsuccessfully, run `docker compose logs app db` and check `docker compose ps` for the DB health status. Confirm the `.env` variable names are exact and the app is using `db:3306`, not `localhost`. If health remains `starting` or becomes `unhealthy`, read the MySQL log and check the health test with `docker compose exec db mysqladmin ping -h 127.0.0.1 -u root -p`. The initial database setup can take time; do not assume that a running container is ready.

`mysqladmin ping` can return success when the server responds but rejects authentication; that behavior means the server process is reachable. Use the Python app query and its error/log output to check the exercise user's credentials and database access.

## Stop and clean up

`docker compose down` removes the containers and network but keeps the named `mysql-data` volume. On a later `up`, the existing database files are reused. To permanently remove the exercise database, first ensure nothing needs its contents, then run `docker compose down --volumes`; this deletes the project volume and its database data. This is destructive and cannot be undone without a separate backup. A backup should be made separately before volume cleanup. `docker compose stop` only stops containers and keeps both the containers and volume.

Delete the local `.env` file manually when no longer needed. Credentials here are placeholders for a local learning environment, not production secret management.

Reference: [MySQL Official Image documentation](https://hub.docker.com/_/mysql) (initialization variables and existing data directory behavior) and the [MySQL 8.4 `mysqladmin` reference](https://dev.mysql.com/doc/refman/8.4/en/mysqladmin.html) (`ping` behavior).
