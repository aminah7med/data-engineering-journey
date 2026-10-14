# 07 — Environment Variables

Keep runtime configuration separate from application code. Environment variables are a common way to configure containerized processes. Dockerfile `ENV` provides image defaults; `docker run -e` and Compose `environment:` provide runtime values.

Compose reads a project `.env` file for **interpolation** of the Compose model. That does not automatically place every `.env` value inside every container: explicitly map required values under a service's `environment:` or `env_file:`. Use `.env.example` with safe placeholders to show required names.

```dotenv
# .env.example — copy to .env and replace locally
MYSQL_DATABASE=learning
MYSQL_USER=appuser
MYSQL_PASSWORD=replace-with-a-local-password
MYSQL_ROOT_PASSWORD=replace-with-a-local-root-password
```

Do not commit `.env` files containing credentials, bake secrets into image layers, place secrets in Dockerfile `ARG`/`ENV`, or print them in logs. Add `.env` to `.gitignore`. For production, use the deployment platform's secret manager or Docker secrets where applicable, restrict access, rotate credentials, and avoid unnecessary exposure. Environment variables can be visible to privileged users and process inspection, so they are not a complete secret-management solution.

The Compose exercise demonstrates required `${VARIABLE:?message}` interpolation and documents local setup. Never use example credentials in a real system.

**When a Data Engineer uses it:** provide database names, service hosts, feature options, and input locations as runtime configuration so the same image can run in a local exercise, a test job, or a deployment environment. Keep secrets in the chosen environment's secret store rather than source control.

**Common mistakes:** assuming `.env` is always copied into a container; committing the real local file; assuming a variable set in Compose interpolation is automatically a container variable; and putting a password in a Dockerfile where it can remain in image metadata or layers.

**Interview check:** Explain the difference between Compose interpolation and a service's `environment:` block. Why is a local `.env` file convenient, and why is it not a production secret manager?

## References

[Environment variables in Compose](https://docs.docker.com/compose/how-tos/environment-variables/) · [Set variables in containers](https://docs.docker.com/compose/how-tos/environment-variables/set-environment-variables/) · [Secrets in Compose](https://docs.docker.com/compose/how-tos/use-secrets/) · [Build secrets](https://docs.docker.com/build/building/secrets/)
