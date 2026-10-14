# 09 — Docker Best Practices

- Choose a small, appropriate, maintained base image. Keep the runtime compatible with application needs.
- Pin base-image versions (and consider digests for strict reproducibility); schedule updates so pinning does not freeze vulnerable dependencies.
- Order layers so stable dependency inputs are copied before frequently changing source. Use `.dockerignore` for VCS metadata, caches, local environments, and secrets.
- Use multi-stage builds to exclude compilers and build tools from runtime images.
- Run as a non-root user where practical, minimize capabilities, and use trusted images. Scan images and dependencies with a maintained vulnerability scanner; review findings and update deliberately.
- Manage configuration at runtime. Never commit credentials or bake them into images. Use appropriate secret-management facilities.
- Put durable state in managed storage and keep tested backups outside the container/volume failure domain.
- Add health checks where meaningful. Remember a health check reports status; it does not repair a broken service.
- Log to stdout/stderr for collection by the platform. Set resource expectations and monitor CPU, memory, disk, and logs.
- Lock or pin application dependencies using the ecosystem's supported mechanism and review updates.
- Keep development conveniences such as source mounts, debug tools, and sample credentials out of production configuration.

Avoid running a whole unrelated stack in one container, storing important state only in a writable layer, using `latest` as an unnoticed deployment pin, using `privileged` without a clear need, putting secrets in image build arguments, and treating a successful image build as a security review.

## References

[Docker build best practices](https://docs.docker.com/build/building/best-practices/) · [Docker security](https://docs.docker.com/engine/security/) · [Image attestations](https://docs.docker.com/build/metadata/attestations/)
